from bottle import get, template
import x
import utils.formatNumber as fn
import utils.getPrettyTweet as pt

@get("/")
def _():
    try:
        x.disable_cache()
        #Get cookie if exists
        logged_user = x.request_cookie()

        #Open database
        db = x.db()

        #Fetch 10 latest tweets
        tweets = db.execute("""
        SELECT t.*, GROUP_CONCAT(ti.tweet_image_url) AS tweet_images, GROUP_CONCAT(ti.tweet_image_order) AS image_orders
        FROM users_and_tweets AS t
        LEFT JOIN tweet_images AS ti ON t.tweet_id = ti.tweet_image_tweet_fk
        GROUP BY t.tweet_id
        ORDER BY t.tweet_created_at DESC
        LIMIT 10
        """
        ).fetchall()

        #Format tweets
        tweets = pt.get_pretty_tweet(tweets)
        
        #Fetch trends
        trends = db.execute("SELECT * FROM trends").fetchall()

        #If cookie exists then decode
        if logged_user:
            logged_user = x.decode_cookie(logged_user)
            username = logged_user["user_name"]
            user_id = logged_user["user_id"]

            #Get users that are not the logged in user and are not already followed
            fsugg = db.execute("""
                SELECT * FROM follower_suggestions
                WHERE user_name != ? 
                AND user_id NOT IN (
                SELECT followee_fk
                FROM following
                WHERE follower_fk = ?
                )""", (username, user_id)).fetchall()
            
        else:
            fsugg = ""

        #Format trends numbers
        for i in range(len(trends)):
            if trends[i]['trend_total_tweets']:
                trends[i]['trend_total_tweets'] = fn.human_format(trends[i]['trend_total_tweets'])
        

        return template("index", max_tweet=x.TWEET_MAX_LEN, max_img=x.TWEET_MAX_IMG_SIZE, max_imgs=x.TWEET_MAX_IMG_NO, tweets=tweets, trends=trends, fsugg=fsugg, logged_user=logged_user)
    except Exception as ex:
        print("error", ex)
        return "error"

    finally:
        if "db" in locals(): db.close()