from bottle import get, request, response
import x
import utils.formatNumber
import time
import calendar

@get('/api-pagination-tweets')
def _():
    try:
        page = request.query.page

        user_name = request.query.user
   
        per_page = 10
        offset = (int(page) - 1) * per_page

        #Open database
        db = x.db()
        if user_name:
            #Get user
            user = db.execute("SELECT user_id FROM users WHERE user_name=? COLLATE NOCASE", (user_name,)).fetchone()

            #Profile tweets
            tweets = db.execute("SELECT * FROM users_and_tweets WHERE tweet_user_fk=? ORDER BY users_and_tweets.tweet_created_at DESC LIMIT ?, ?", (user["user_id"], offset, per_page)).fetchall()
        else:    
            #Index tweets
            tweets = db.execute("SELECT * FROM users_and_tweets ORDER BY users_and_tweets.tweet_created_at DESC LIMIT ?, ?", (offset, per_page)).fetchall()
        
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
        

        #return tweets
        return {"info":"ok", "tweets": tweets}
    except Exception as ex:
        print(ex)
        try:
            response.status = ex.args[0]
            return {"info":ex.args[1]}
        except:
            response.status = 500
            return {"info":str(ex)}
    finally:
        if 'db' in locals(): db.close()