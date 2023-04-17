from bottle import get, template, request
import time
import calendar
import x
import formatNumber
import jwt

@get("/")
def _():
    try:
        x.disable_cache()
        
        logged_user = request.get_cookie("user")
        db = x.db()
        
        tweets = db.execute("SELECT * FROM users_and_tweets ORDER BY users_and_tweets.tweet_created_at DESC LIMIT 0, 10").fetchall()
        trends = trends = db.execute("SELECT * FROM trends").fetchall()
        if logged_user:
            logged_user = jwt.decode(logged_user, x.COOKIE_SECRET, algorithms=["HS256"])
            username = logged_user["user_name"]
            fsugg = db.execute("SELECT * FROM follower_suggestions WHERE NOT user_name=?",(username,)).fetchall()
            
        else:
            fsugg = db.execute("SELECT * FROM follower_suggestions").fetchall()

           #format the tweet numbers
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
           
        return template("index", min_length=x.TWEET_MIN_LEN, max_length=x.TWEET_MAX_LEN, tweets=tweets, trends=trends, fsugg=fsugg, logged_user=logged_user)
    except:
        return "error"

    finally:
        if "db" in locals(): db.close()