from bottle import post, request, response
import x
import uuid
import time
import calendar

@post("/tweet")
def _():
    try: #Success
        x.validate_tweet()
        db = x.db()

        logged_user = request.get_cookie("user", secret=x.COOKIE_SECRET)
        response.add_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        response.add_header("Pragma", "no-cache")
        response.add_header("Expires", 0)

        tweet_id = str(uuid.uuid4().hex)
        tweet_user_fk = logged_user["user_id"]
        tweet_created_at = int(time.time())
        tweet_field_text = request.forms.get("tweet_field_text")
        tweet_field_img = ""
        tweet_updated_at = "0"
        tweet_total_replies = "0"
        tweet_total_likes = "0"
        tweet_total_retweets = "0"
        tweet_total_views = "0"
        #print(tweet_id, tweet_user_fk, tweet_created_at, tweet_field_text, tweet_field_img, tweet_updated_at, tweet_total_replies, tweet_total_likes, tweet_total_retweets, tweet_total_views)

        db.execute("INSERT INTO tweets VALUES( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(tweet_id, tweet_user_fk, tweet_created_at, tweet_field_text, tweet_field_img, tweet_updated_at, tweet_total_replies, tweet_total_likes, tweet_total_retweets, tweet_total_views))
        db.commit()
        #SELECT Orders.OrderID, Orders.OrderDate, Customers.CustomerID, Customers.ContactName, Products.ProductID, Products.ProductName 
        #FROM orders 
        tweet = db.execute("SELECT user_name, user_full_name, user_img_avatar, user_verified, tweet_id, tweet_created_at, tweet_field_text, tweet_field_img FROM users_and_tweets WHERE tweet_id=?", (tweet_id,)).fetchall()[0]
        if tweet['tweet_created_at']:
            month = time.strftime('%#m', time.localtime(tweet['tweet_created_at']))
            day = time.strftime('%#d', time.localtime(tweet['tweet_created_at']))
            tweet['tweet_created_at'] = f"{calendar.month_abbr[int(month)]} {day}"


        return {"info":"ok", "tweet":tweet}
    except Exception as ex: #something is wrong
        #this exception is being called from x file, ex is error in x.py
        
        response.status = 400
        return {"info": str(ex)}

    finally: #Will always happen
        if "db" in locals(): db.close()