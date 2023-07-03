from bottle import get, template, request, response
import x
import time
import utils.formatNumber
import calendar
import utils.getPrettyTweet as pt

@get("/search")
def _():
    try:
        x.disable_cache()
        query = request.query.query

        logged_user = x.request_cookie()
    
        if not logged_user:
            response.status = 303
            response.set_header("Location", "/login")
            return

        if logged_user:
            logged_user = x.decode_cookie(logged_user)

        if not query:
            response.status = 303
            response.set_header("Location", "/explore")
            return

        #Open database
        db = x.db()

        #Fetch trends
        trends = db.execute("SELECT * FROM trends").fetchall()

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
        
        #Preparing the search query
        exequery = "%" + query + "%"  
        #Fetch people
        #@todo make this smarter?
        people_result = db.execute("""
    SELECT 
        active_users.user_name, 
        active_users.user_twitter_status, 
        active_users.user_full_name, 
        active_users.user_img_avatar, 
        active_users.user_bio_text, 
            CASE WHEN following.followee_fk IS NULL THEN 0 ELSE 1 END AS is_followed
    FROM active_users
    LEFT JOIN following ON active_users.user_id = following.followee_fk AND following.follower_fk = ?
    WHERE active_users.user_name LIKE ? OR active_users.user_full_name LIKE ?
    ORDER BY active_users.user_name LIKE ? DESC, active_users.user_full_name LIKE ? DESC
    LIMIT 3
    """, (user_id, exequery, exequery, exequery, exequery)).fetchall()


        #Fetch tweets
        tweets = db.execute("""
        SELECT t.*, GROUP_CONCAT(ti.tweet_image_url) AS tweet_images, GROUP_CONCAT(ti.tweet_image_order) AS image_orders
        FROM users_and_tweets AS t
        LEFT JOIN tweet_images AS ti ON t.tweet_id = ti.tweet_image_tweet_fk
        WHERE tweet_field_text LIKE '%' || ? || '%'
        GROUP BY t.tweet_id
        ORDER BY tweet_field_text LIKE ? DESC
        LIMIT 0, 10
        """, (query, query)
        ).fetchall()

        #Format tweets
        tweets = pt.get_pretty_tweet(tweets)  

        #Format trends numbers
        for i in range(len(trends)):
            if trends[i]['trend_total_tweets']:
                trends[i]['trend_total_tweets'] = utils.formatNumber.human_format(trends[i]['trend_total_tweets'])

        return template("search", query=query, logged_user=logged_user, trends=trends, fsugg=fsugg, people_result=people_result, tweets=tweets)
    except Exception as ex:
        print(ex)
        return "error"

    finally:
        if "db" in locals(): db.close()