from bottle import get, template
import x
import utils.formatNumber
import utils.getPrettyTweet as pt

@get("/explore")
def _():
    try:
        x.disable_cache()

        logged_user = x.request_cookie()

       
        #Open database
        db = x.db()

        if logged_user:
            logged_user = x.decode_cookie(logged_user)
            #Fetch follower suggestions
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

        #Fetch trends
        trends = db.execute("SELECT * FROM trends").fetchall()

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

        #Format trends numbers
        for i in range(len(trends)):
            if trends[i]['trend_total_tweets']:
                trends[i]['trend_total_tweets'] = utils.formatNumber.human_format(trends[i]['trend_total_tweets'])

        return template("explore", logged_user=logged_user, trends=trends, fsugg=fsugg, tweets=tweets)
    except Exception as ex:
        print(ex)
        return "error"

    finally:
        if "db" in locals(): db.close()