from bottle import post, request, response
import x
import jwt
import uuid
import time

@post('/api-edit-profile')
def _():
    try:
        #Get cookie user
        logged_user = x.request_cookie()
        #Decode cookie
        logged_user = x.decode_cookie(logged_user)

        #DELETE AFTER
        #db = x.db()
        #logged_user = db.execute("SELECT * FROM users WHERE user_name = ?", ("my_name_cleo",)).fetchone()
        
        if not logged_user:
            raise Exception(400, "Log in to edit profile")
        print(logged_user)

        #Validate Text fields
        user_full_name = x.validate_fullname()
        user_bio_text = x.validate_bio_text()
        user_bio_location = x.validate_bio_loc()
        user_bio_link = x.validate_bio_link()

        #Variables for transaction
        query = "UPDATE users SET "
        update_params = []

        #Check if fullname has changed
        if user_full_name != logged_user["user_full_name"]:
            query += "user_full_name = ?, "
            update_params.append(user_full_name)

        #Check if bio has changed
        if user_bio_text != logged_user["user_bio_text"]:
            query += "user_bio_text = ?, "
            update_params.append(user_bio_text)

        #Check if location has changed
        if user_bio_location != logged_user["user_bio_location"]:
            query += "user_bio_location = ?, "
            update_params.append(user_bio_location)

        #Check if link has changed
        if user_bio_link != logged_user["user_bio_link"]:
            query += "user_bio_link = ?, "
            update_params.append(user_bio_link)

        
        print(query, update_params)
        # Execute the update query if anything has been added to update params
        if update_params:
            #Open database
            db = x.db()
            #@todo add the updated at
            # Remove the trailing comma and space from the query
            query = query.rstrip(", ")

            #Add the WHERE and user id
            query += " WHERE user_id = ?"
            update_params.append(logged_user["user_id"])

            db.execute(query, update_params)
            db.commit()

            try:
                import production
                is_cookie_https = True
            except:
                is_cookie_https = False

            #Set new cookie
            user = db.execute("SELECT * FROM users WHERE user_name = ?", (logged_user["user_name"],)).fetchone()
            user.pop("user_password")
            the_jwt = jwt.encode(user, x.COOKIE_SECRET, algorithm="HS256")
            response.set_cookie("user", the_jwt, httponly=True, secure=is_cookie_https)

        
        #Get avatar img
        #user_avatar_img = request.files.get("user_avatar_img")
        #IF there is one and it is not the same as before VALIDATE
        
        #Validate image type ext
        #x.validate_image_type(user_avatar_img)
        

        #Upload to temp folder

        #Validate image size

        #Validateimage data filetype

        #Validate profile image
        #filetype = magic.from_file(f"images/temp_imgs/{tweet_image_name+ext}")
        #x.validate_image_datatype(filetype)

        #Validate cover image
        #filetype = magic.from_file(f"images/temp_imgs/{tweet_image_name+ext}")
        #x.validate_image_datatype(filetype)







        #Get user that matches api key
        #user = db.execute("SELECT * FROM users WHERE user_api_key=? COLLATE NOCASE", (user_api_key,)).fetchone()

        #The api key does not exists, it is either wrong or has been changed/updated
        #if not user: raise Exception(400, "An error occurred")
        
        #User id
        #user_id = user["user_id"]
        
        #Update account status to active
        #db.execute(f"UPDATE users SET user_account_status=? WHERE user_api_key=?", (x.ACC_STATUS_ACTIVE, user_api_key,))



        #updated_at = int(time.time())
       
        #db.execute(f"UPDATE users SET user_updated_at=? WHERE user_id=?", (updated_at, user_id))

        #Commit
        #db.commit()

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