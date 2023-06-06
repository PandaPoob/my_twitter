from bottle import get, template, request, response
import x
import time
import utils.formatNumber
import calendar

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

        #Fetch tweets
        tweets = db.execute("SELECT * FROM users_and_tweets ORDER BY users_and_tweets.tweet_created_at DESC, users_and_tweets.tweet_total_likes DESC LIMIT 0, 10").fetchall()
      
        #Fetch images of tweets 
        for i in range(len(tweets)):
            if tweets[i]["tweet_field_images"] > 0:
                tweet_images = db.execute("SELECT * FROM tweet_images WHERE tweet_images.tweet_image_tweet_fk=? ORDER BY tweet_images.tweet_image_order ASC", (tweets[i]["tweet_id"],)).fetchall()
                #Declare new key and add image list
                tweets[i]['tweet_images'] = tweet_images
        
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

        return template("explore", logged_user=logged_user, trends=trends, fsugg=fsugg, tweets=tweets)
    except Exception as ex:
        print(ex)
        return "error"

    finally:
        if "db" in locals(): db.close()