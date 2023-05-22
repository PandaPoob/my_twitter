from bottle import post, request, response
import x
import uuid
import time
import calendar
import jwt

@post("/tweet")
def _():
    try:
        #Backend validation 
        x.validate_tweet()
      
        #Get cookie
        logged_user = request.get_cookie("user")
        
        #If user cookie exists
        if logged_user:
        

        #Decode cookie
            logged_user = jwt.decode(logged_user, x.COOKIE_SECRET, algorithms=["HS256"])
            print(logged_user)
        #Add headers
            response.add_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
            response.add_header("Pragma", "no-cache")
            response.add_header("Expires", 0)
        
        #Prepare data
            tweet = {
                "tweet_id": str(uuid.uuid4().hex),
                "tweet_user_fk": logged_user["user_id"],
                "tweet_created_at": int(time.time()),
                "tweet_field_text": request.forms.get("tweet_field_text"),
                "tweet_updated_at": 0,
                "tweet_total_replies": 0,
                "tweet_total_likes": 0,
                "tweet_total_retweets": 0,
                "tweet_total_views": 0,
                "tweet_parent_id": "",
                "tweet_type": x.TWEET_TYPE_DEFAULT,
            }
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

        #Open database
            values = x.prepare_values()
            print(30*"#")
            print("values:", values)

            db = x.db()
            db.execute("INSERT INTO tweets VALUES( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(tweet_id, tweet_user_fk, tweet_created_at, tweet_field_text, tweet_field_img, tweet_updated_at, tweet_total_replies, tweet_total_likes, tweet_total_retweets, tweet_total_views))
            db.commit()
          
            #tweet = db.execute("SELECT user_name, user_full_name, user_img_avatar, user_twitterblue, tweet_id, tweet_created_at, tweet_field_text, tweet_field_img FROM users_and_tweets WHERE tweet_id=?", (tweet_id,)).fetchall()[0]
        
            #if tweet['tweet_created_at']:
             #   month = time.strftime('%#m', time.localtime(tweet['tweet_created_at']))
              #  day = time.strftime('%#d', time.localtime(tweet['tweet_created_at']))
               # tweet['tweet_created_at'] = f"{calendar.month_abbr[int(month)]} {day}"


        return {"info":"ok", "tweet":tweet}
    except Exception as ex:
        #this exception is being called from x file, ex is error in x.py
        
        response.status = 400
        return {"info": str(ex)}

    finally: #Will always happen
        if "db" in locals(): db.close()