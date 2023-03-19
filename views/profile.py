from bottle import get, template, response, request
import time
import calendar
import x
import formatNumber

@get("/<username>")
def _(username):
    try:
        x.disable_cache()

        logged_user = request.get_cookie("user", secret=x.COOKIE_SECRET)
      
        db = x.db()
    
        user = db.execute("SELECT * FROM users WHERE user_name=? COLLATE NOCASE", (username,)).fetchall()[0]
        
        user_id = user["user_id"]
        #print(f"user id: {user_id}")
        tweets = db.execute("SELECT * FROM users_and_tweets WHERE tweet_user_fk=? ORDER BY users_and_tweets.tweet_created_at DESC LIMIT 0, 10", (user_id,)).fetchall()
        
        #get trends
        trends = db.execute("SELECT * FROM trends").fetchall()

        #get follower suggestions
        if logged_user:
            username = logged_user["user_name"]
            fsugg = db.execute("SELECT * FROM follower_suggestions WHERE NOT user_name=?",(username,)).fetchall()
        else:
            fsugg = db.execute("SELECT * FROM follower_suggestions WHERE NOT user_name=?",(username,)).fetchall()
        

        #get img tweets
        imgtweets = db.execute("SELECT * FROM tweets WHERE tweet_field_img <> '' AND tweet_user_fk=? ORDER BY tweets.tweet_created_at DESC LIMIT 0, 6", (user_id,)).fetchall()
     

       #format user numbers
        if user['user_total_followers']:
            user["user_total_followers"] = formatNumber.human_format(user['user_total_followers'])
        
        if user['user_total_following']:
            user["user_total_following"] = formatNumber.human_format(user['user_total_following'])
       
        if user['user_total_tweets']:
            user["user_total_tweets"] = formatNumber.human_format(user['user_total_tweets'])
        

        #format the tweet numbers
        if len(tweets) != 0:
            for i in range(len(tweets)):
                if tweets[i]['tweet_total_replies']:
                    tweets[i]['tweet_total_replies'] = formatNumber.human_format(tweets[i]['tweet_total_replies'])
                
                if tweets[i]['tweet_total_likes']:
                    tweets[i]['tweet_total_likes'] = formatNumber.human_format(tweets[i]['tweet_total_likes'])
                
                if tweets[i]['tweet_total_retweets']:
                    tweets[i]['tweet_total_retweets'] = formatNumber.human_format(tweets[i]['tweet_total_retweets'])
                
                if tweets[i]['tweet_total_views']:
                    tweets[i]['tweet_total_views'] = formatNumber.human_format(tweets[i]['tweet_total_views'])

                if tweets[i]['tweet_created_at']:
                    month = time.strftime('%#m', time.localtime(tweets[i]['tweet_created_at']))
                    day = time.strftime('%#d', time.localtime(tweets[i]['tweet_created_at']))
                    tweets[i]['tweet_created_at'] = f"{calendar.month_abbr[int(month)]} {day}"
                
        
        #format trends numbers
        for i in range(len(trends)):
            if trends[i]['trend_total_tweets']:
                #print(type(trends[i]['trend_total_tweets']))
                trends[i]['trend_total_tweets'] = formatNumber.human_format(trends[i]['trend_total_tweets'])

        #format date on user
        if user['user_created_at']:
            year = time.strftime('%Y', time.localtime(user["user_created_at"]))
            month = time.strftime('%#m', time.localtime(user["user_created_at"]))
            user["user_created_at"] = f"Joined {calendar.month_name[int(month)]} {year}"

        #format date on tweet
        

        return template("profile", user=user, tweets=tweets, trends=trends, fsugg=fsugg, imgtweets=imgtweets, logged_user=logged_user)
    except Exception as ex:
        print(ex)
        return "error"

    finally:
        if "db" in locals(): db.close()
