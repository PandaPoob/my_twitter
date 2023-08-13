from bottle import get, template
import x
from datetime import datetime
import utils.getPrettyTweet as pt

@get("/<username>/status/<slug>")
def _(username, slug):
    try:

        x.disable_cache()
        
        #Get cookie if exists
        logged_user = x.request_cookie()

        if logged_user:
            logged_user = x.decode_cookie(logged_user)

        #Open database
        db = x.db()

        #Fetch trends
        trends = db.execute("SELECT * FROM trends").fetchall()
        
        #Fetch 10 latest tweets
        tweet = db.execute("""
        SELECT t.*, GROUP_CONCAT(ti.tweet_image_url) AS tweet_images, GROUP_CONCAT(ti.tweet_image_order) AS image_orders
        FROM users_and_tweets AS t
        LEFT JOIN tweet_images AS ti ON t.tweet_id = ti.tweet_image_tweet_fk
        WHERE tweet_slug=?
        GROUP BY t.tweet_id
        ORDER BY t.tweet_created_at DESC
        """, (slug,)
        ).fetchall()

        saved_epoch = tweet[0]['tweet_created_at']
        #Format tweets
        tweet = pt.get_pretty_tweet(tweet)

        #Convert epoch into datetime obj
        dt = datetime.fromtimestamp(saved_epoch)

        #%I-Hour(12-hour clock) %M-Minute %p-AM/PM %b-Abbre month %d-Day(zero) %Y-Year(four)
        tweet[0]['tweet_created_at'] = dt.strftime("%I:%M %p · %b %d, %Y")
        
        print(tweet[0])
        return template("tweet", logged_user=logged_user, trends=trends, tweet=tweet[0])

    except Exception as ex:
        print(ex)
        return "error"

    finally:
        pass