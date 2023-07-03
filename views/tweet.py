from bottle import get, template
import x
import time
import calendar
import utils.formatNumber
from datetime import datetime

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

        tweet = db.execute("SELECT * FROM users_and_tweets WHERE tweet_slug=?", (slug,)).fetchone()
        
        #Fetch tweets
        if tweet["tweet_field_images"] > 0:
            tweet_images = db.execute("SELECT * FROM tweet_images WHERE tweet_images.tweet_image_tweet_fk=? ORDER BY tweet_images.tweet_image_order ASC", (tweet["tweet_id"],)).fetchall()
            #Declare new key and add image list
            tweet['tweet_images'] = tweet_images

        if tweet['tweet_total_replies']:
            tweet['tweet_total_replies'] = utils.formatNumber.human_format(tweet['tweet_total_replies'])
        
        if tweet['tweet_total_likes']:
            tweet['tweet_total_likes'] = utils.formatNumber.human_format(tweet['tweet_total_likes'])
        
        if tweet['tweet_total_retweets']:
            tweet['tweet_total_retweets'] = utils.formatNumber.human_format(tweet['tweet_total_retweets'])
        

        #Convert epoch into datetime obj
        dt = datetime.fromtimestamp(tweet['tweet_created_at'])

        #%I-Hour(12-hour clock) %M-Minute %p-AM/PM %b-Abbre month %d-Day(zero) %Y-Year(four)
        tweet['tweet_created_at'] = dt.strftime("%I:%M %p · %b %d, %Y")

        

        return template("tweet", logged_user=logged_user, trends=trends, tweet=tweet)

    except Exception as ex:
        print(ex)
        return "error"

    finally:
        pass