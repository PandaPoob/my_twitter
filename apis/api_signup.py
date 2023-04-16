from bottle import post, response
import x
import bcrypt
import uuid
import time
import sendEmail

@post("/api-signup")
def _():
    try:
        user_fullname = x.validate_fullname()
        user_email = x.validate_user_email()
        user_birthday = x.validate_user_birthday()
        user_name = x.validate_username()
        user_password = x.validate_password()
        x.validate_user_confirm_password()

        salt = bcrypt.gensalt()
        user_id = str(uuid.uuid4()).replace("-","")
        user_api_key = str(uuid.uuid4()).replace("-","")



        user = {
    "user_id" : user_id,
    "user_name" : user_name,
    "user_full_name": user_fullname,  
    "user_password": bcrypt.hashpw(user_password.encode('utf-8'), salt),
    "user_email" : user_email,
    "user_phonenumber": "",
    "user_api_key": user_api_key,
    "user_created_at" : int(time.time()),
    "user_updated_at" : int(time.time()),
    "user_img_avatar": "default.jpg",
    "user_img_cover": "default.jpg",
    "user_bio_text": "",
    "user_bio_location": "",
    "user_bio_link": "",
    "user_bio_birthday": str(user_birthday),
    "user_total_followers": 0,
    "user_total_following": 0,
    "user_total_tweets": 0,
    "user_twitterblue": False,
    "user_account_status": x.ACC_STATUS_INACTIVE
        }

        values = ""
        for key in user:
            values += f":{key},"
        values = values.rstrip(",")
        print(values)	
        db = x.db()

        check_email = db.execute("SELECT user_email FROM users WHERE user_email=?", (user_email,)).fetchone()
        if check_email: raise Exception(400, "Email is already in use")

        check_username = db.execute("SELECT user_name FROM users WHERE user_name=?", (user_name,)).fetchone()
        if check_username: raise Exception(400, "Username already exists")

        total_rows_inserted = db.execute(f"INSERT INTO users VALUES({values})", user).rowcount        
        if total_rows_inserted != 1: raise Exception(400, "Please, try again")
        
        db.commit()
        user.pop("user_password")
        sendEmail.send_email(user_email, user_api_key)
        #print("pop", user)
        try:
            import production
            is_cookie_https = True
        except:
            is_cookie_https = False
        #response.set_cookie("user", user, secret=x.COOKIE_SECRET, httponly=True, secure=is_cookie_https)
        return {
			"info" : "user created", 
			"user_id" : user_id,
            "user_name": user_name
		}                
    except Exception as ex:
        print(ex)
        #
        response.status = ex.args[0]
        return {"info":ex.args[1]}
        
    finally:
        if "db" in locals(): db.close()