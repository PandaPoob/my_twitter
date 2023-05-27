from bottle import post, response
import x
import bcrypt
import uuid
import time
import sendEmail
import os
import shutil

@post("/api-signup")
def _():
    try:
        #Validate
        user_fullname = x.validate_fullname()
        user_email = x.validate_user_email()
        user_birthday = x.validate_user_birthday()
        print(user_birthday)
        user_name = x.validate_username()
        user_password = x.validate_password()
        x.validate_user_confirm_password()
        
        #Salt to hash password
        salt = bcrypt.gensalt()

        #Open database        
        db = x.db()

        #Check that email is not already in use
        check_email = db.execute("SELECT user_email FROM users WHERE user_email=?", (user_email,)).fetchone()
        if check_email: raise Exception(400, "Email is already in use")
        
        #Check that user name is not taken
        check_username = db.execute("SELECT user_name FROM users WHERE user_name=?", (user_name,)).fetchone()
        if check_username: raise Exception(400, "Username already exists")

        #API KEY
        user_api_key = str(uuid.uuid4().hex)
    
        #user_id = generate_user_id()
        #default_image_name = 'default_image.jpg'  
        #new_user_img_avatar = f'{avatar_img_id}.jpg'
        #copy_and_rename_image(default_image_name, new_user_img_avatar)

        avatar_img_id = str(uuid.uuid4().hex)
        #cover_img_id = str(uuid.uuid4().hex)
        

        def copy_image(avatar_img_id):
            source_img = os.getcwd()+f"/images/placeholders/avatar_default.jpg"
            new_img_path = os.getcwd()+f"/images/avatar_imgs/{avatar_img_id}.jpg"
            shutil.copy(source_img, new_img_path)
        copy_image(avatar_img_id)
        
        user = {
    "user_id" : str(uuid.uuid4().hex),
    "user_name" : user_name,
    "user_created_at" : int(time.time()),
    "user_updated_at" : int(time.time()),
    "user_api_key": user_api_key,
    "user_admin": 0,
    "user_twitter_status": x.USER_TWITTER_BASIC,
    "user_account_status": x.ACC_STATUS_INACTIVE,
    "user_email" : user_email,
    "user_phonenumber": "",
    "user_full_name": user_fullname,
    "user_birthday": str(user_birthday),
    "user_password": bcrypt.hashpw(user_password.encode('utf-8'), salt),
    "user_img_avatar": f"{avatar_img_id}.jpg",
    "user_img_cover": "default.jpg",
    "user_bio_text": "",
    "user_bio_location": "",
    "user_bio_link": "",
    "user_bio_birthday": 1,
    "user_total_tweets": 0,
    "user_total_following": 0,
    "user_total_followers": 0,   
        }

        values = x.prepare_values(user)

        total_rows_inserted = db.execute(f"INSERT INTO users VALUES({values})", user).rowcount        
        if total_rows_inserted != 1: raise Exception(400, "Please, try again")

        #db.commit()

        #sendEmail.send_email(user_email, user_api_key)

        return {
			"info" : "user created", 
            "user_name": user_name
		}                
    except Exception as ex:
        print(ex)
        try:
            response.status = ex.args[0]
            return {"info":ex.args[1]}
        except:
            response.status = 500
            return {"info":str(ex)}
    finally:
        if "db" in locals(): db.close()