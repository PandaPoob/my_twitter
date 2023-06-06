from bottle import get, template
import time
import calendar
import x
import utils.formatNumber

@get("/")
def _():
    try:
        x.disable_cache()
        #Get cookie if exists
        logged_user = x.request_cookie()

        #Open database
        db = x.db()

        #Fetch 10 latest tweets
        tweets = db.execute("SELECT * FROM users_and_tweets ORDER BY users_and_tweets.tweet_created_at DESC LIMIT 0, 10").fetchall()
      
        #Fetch images of tweets 
        for i in range(len(tweets)):
            if tweets[i]["tweet_field_images"] > 0:
                tweet_images = db.execute("SELECT * FROM tweet_images WHERE tweet_images.tweet_image_tweet_fk=? ORDER BY tweet_images.tweet_image_order ASC", (tweets[i]["tweet_id"],)).fetchall()
                #Declare new key and add image list
                tweets[i]['tweet_images'] = tweet_images
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
           
        #Format tweet numbers
        for i in range(len(tweets)):
            if tweets[i]['tweet_total_replies']:
                tweets[i]['tweet_total_replies'] = utils.formatNumber.human_format(tweets[i]['tweet_total_replies'])
        
            if tweets[i]['tweet_total_likes']:
                tweets[i]['tweet_total_likes'] = utils.formatNumber.human_format(tweets[i]['tweet_total_likes'])
            
            if tweets[i]['tweet_total_retweets']:
                tweets[i]['tweet_total_retweets'] = utils.formatNumber.human_format(tweets[i]['tweet_total_retweets'])
            
            if tweets[i]['tweet_total_views']:
                tweets[i]['tweet_total_views'] = utils.formatNumber.human_format(tweets[i]['tweet_total_views'])
           
            if tweets[i]['tweet_created_at']:
                month = time.strftime('%#m', time.localtime(tweets[i]['tweet_created_at']))
                day = time.strftime('%#d', time.localtime(tweets[i]['tweet_created_at']))
                tweets[i]['tweet_created_at'] = f"{calendar.month_abbr[int(month)]} {day}"
        
        #Format trends numbers
        for i in range(len(trends)):
            if trends[i]['trend_total_tweets']:
                trends[i]['trend_total_tweets'] = utils.formatNumber.human_format(trends[i]['trend_total_tweets'])
      
        return template("index", max_tweet=x.TWEET_MAX_LEN, max_img=x.TWEET_MAX_IMG_SIZE, max_imgs=x.TWEET_MAX_IMG_NO, tweets=tweets, trends=trends, fsugg=fsugg, logged_user=logged_user)
    except Exception as ex:
        print("error", ex)
        return "error"

    finally:
        if "db" in locals(): db.close()