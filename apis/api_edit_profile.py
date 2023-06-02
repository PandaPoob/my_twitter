from bottle import post, request, response
import x
import uuid
import time

@post('/api-edit-profile')
def _():
    try:
        #Get cookie user
        logged_user = x.request_cookie()

        
        #Get avatar img
        user_avatar_img = request.files.get("user_avatar_img")
        #IF there is one and it is not the same as before VALIDATE
        
        #Validate image type ext
        x.validate_image_type(user_avatar_img)
        

        #Upload to temp folder

        #Validate image size

        #Validateimage data filetype

        #Validate profile image
        #filetype = magic.from_file(f"images/temp_imgs/{tweet_image_name+ext}")
        #x.validate_image_datatype(filetype)

        #Validate cover image
        #filetype = magic.from_file(f"images/temp_imgs/{tweet_image_name+ext}")
        #x.validate_image_datatype(filetype)

        #Validate Text fields
        user_fullname = x.validate_fullname()
        user_bio_text = x.validate_bio_text()
        user_bio_location = x.validate_bio_loc()
        user_bio_link = x.validate_bio_link()

        #Open database
        db = x.db()

        #Get user that matches api key
        user = db.execute("SELECT * FROM users WHERE user_api_key=? COLLATE NOCASE", (user_api_key,)).fetchone()

        #The api key does not exists, it is either wrong or has been changed/updated
        if not user: raise Exception(400, "An error occurred")
        
        #User id
        user_id = user["user_id"]
        
        #Update account status to active
        db.execute(f"UPDATE users SET user_account_status=? WHERE user_api_key=?", (x.ACC_STATUS_ACTIVE, user_api_key,))

        #New api key
        new_api_key = str(uuid.uuid4().hex)

        updated_at = int(time.time())
        #Assign new api key
        db.execute(f"UPDATE users SET user_api_key=? WHERE user_id=?", (new_api_key, user_id))
        db.execute(f"UPDATE users SET user_updated_at=? WHERE user_id=?", (updated_at, user_id))

        #Commit
        db.commit()

        return {"info":"ok"}
    except Exception as ex:
        print(ex)
        if "db" in locals(): db.rollback()
        try:
            response.status = ex.args[0]
            return {"info":ex.args[1]}
        except:
            response.status = 500
            return {"info":str(ex)}
    finally:
        if 'db' in locals(): db.close()