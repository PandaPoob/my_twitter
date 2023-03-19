from bottle import post, request, response
import x
import bcrypt
import uuid
import time

@post("/api-signup")
def _():
    try:
        user_fullname = x.validate_fullname()
        user_email = x.validate_user_email()
        user_birthday = x.validate_user_birthday()
        user_name = x.validate_username()
        user_password = x.validate_password()

        salt = bcrypt.gensalt()
        user_id = str(uuid.uuid4()).replace("-","")

        user = {
    "user_id" : user_id,
    "user_name" : user_name,
    "user_full_name": "name here",  
    "user_password": bcrypt.hashpw(user_password.encode('utf-8'), salt),
    "user_email" : user_email,
    "user_created_at" : int(time.time()),
    "user_updated_at" : int(time.time()),
    "user_img_avatar": 0,
    "user_img_cover": 0,
    "user_verified": 0,
    "user_bio_text": 0,
    "user_bio_location": 0,
    "user_bio_link": 0,
    "user_bio_birthday": 0,
    "user_total_followers": 0,
    "user_total_following": 0,
    "user_total_tweets": 0
        }

        values = ""
        for key in user:
            values += f":{key},"
        values = values.rstrip(",")
        print(values)	
        db = x.db()
        
        total_rows_inserted = db.execute(f"INSERT INTO users VALUES({values})", user).rowcount        
        
        if total_rows_inserted != 1: raise Exception("Please, try again")
        
        db.commit()
        return {
			"info" : "user created", 
			"user_id" : user_id
		}                
    except Exception as ex:
        print(ex)
        return {"info": str(ex)}
    finally:
        if "db" in locals(): db.close()