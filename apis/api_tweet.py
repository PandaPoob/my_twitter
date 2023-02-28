from bottle import post, request, response
import x
import uuid
import time

@post("/tweet")
def _():
    try: #Success
        x.validate_tweet()
        db = x.db()
        
        tweet_id = str(uuid.uuid4().hex)
        tweet_user_fk = "b3094c2f1c144817b7cc0b718fc3c644"
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
        return {"info":"ok", "tweet_id":tweet_id}
    except Exception as ex: #something is wrong
        #this exception is being called from x file, ex is error in x.py
        response.status = 400
        return {"info": str(ex)}

    finally: #Will always happen
        if "db" in locals(): db.close()