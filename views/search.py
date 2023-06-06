from bottle import get, template, request, response
import x
import time
import utils.formatNumber
import calendar

@get("/search")
def _():
    try:
        x.disable_cache()
        query = request.query.query
        print(query)

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
        fsugg = db.execute("SELECT * FROM follower_suggestions WHERE NOT user_name=?",(username,)).fetchall()

        #Fetch people
        people_result = db.execute("SELECT user_name, user_twitter_status, user_full_name, user_img_avatar, user_bio_text FROM active_users WHERE user_name LIKE '%' || ? || '%' OR user_full_name LIKE '%' || ? || '%' ORDER BY user_name LIKE ? DESC, user_full_name LIKE ? DESC LIMIT 3", (query, query, query, query)).fetchall()

        #Fetch tweets
        tweets = db.execute("SELECT * FROM users_and_tweets WHERE tweet_field_text LIKE '%' || ? || '%' ORDER BY tweet_field_text LIKE ? DESC LIMIT 10", (query, query)).fetchall()
      
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

        return template("search", query=query, logged_user=logged_user, trends=trends, fsugg=fsugg, people_result=people_result, tweets=tweets)
    except Exception as ex:
        print(ex)
        return "error"

    finally:
        if "db" in locals(): db.close()