from bottle import post, request, response
import x
import jwt
import uuid
import os
import magic
import utils.prepareImages as p
import time

@post('/api-edit-profile')
def _():
    try:
        x.disable_cache()

        folder_path = ""
        #Get cookie user
        logged_user = x.request_cookie()
        #Decode cookie
        logged_user = x.decode_cookie(logged_user)
        
        if not logged_user:
            raise Exception(400, "Log in to edit profile")

        #Variables for transaction
        query = "UPDATE users SET "
        update_params = []

        #Variables for new img names
        cover_image_url = ""
        avatar_image_url = ""

        #Get avatar
        user_img_avatar = request.files.get("user_img_avatar")
        avatar_filename = None
        if user_img_avatar is not None:
            avatar_filename = user_img_avatar.filename
            if avatar_filename == "empty":
                avatar_filename = None
        
        #Get cover
        user_img_cover = request.files.get("user_img_cover")
        cover_filename = None
        if user_img_cover is not None:
            cover_filename = user_img_cover.filename
            if cover_filename == "empty":
                cover_filename = None
        

        if avatar_filename is not None or cover_filename is not None:
            #Create temp folder
            folder_name = logged_user["user_id"]
            directory_path = x.ROOT+"/images/temp_imgs/"
            folder_path = os.path.join(directory_path, folder_name)
            os.makedirs(folder_path)

        #Avatar image
        if avatar_filename is not None:
            avatar_filename = user_img_avatar.filename
            #Validate type on ext
            
            x.validate_image_type(user_img_avatar)
            
            #Upload to temp folder
            name, ext = os.path.splitext(avatar_filename)
            new_avatar_img_name = str(uuid.uuid4().hex)
            user_img_avatar.save(f"{folder_path}/{new_avatar_img_name+ext}")

            #Validate image size
            filesize = os.stat(f"{folder_path}/{new_avatar_img_name+ext}").st_size
            x.validate_profile_image_size(filesize)

            #Validate image data filetype
            filetype = magic.from_file(f"{folder_path}/{new_avatar_img_name+ext}")
            x.validate_image_datatype(filetype)
            
            #Crop
            path = f"{folder_path}/{new_avatar_img_name+ext}"
            cropped_img = p.resize_crop_avatar_image(path, x.USER_AVATAR_ASPECT)

            #Save new image
            avatar_image_url = str(uuid.uuid4().hex+ext.lower())
            cropped_img.save(x.ROOT+f"/images/avatar_imgs/{avatar_image_url}")

            #Add new image to query
            query += "user_img_avatar = ?, "
            update_params.append(avatar_image_url)

        #Cover image
        if cover_filename is not None:
            cover_filename = user_img_cover.filename
            #Validate type on ext
            x.validate_image_type(user_img_cover)

            #Upload to temp folder
            name, ext = os.path.splitext(cover_filename)
            new_cover_img_name = str(uuid.uuid4().hex)
            user_img_cover.save(f"{folder_path}/{new_cover_img_name+ext}")
            
            #Validate image size
            filesize = os.stat(f"{folder_path}/{new_cover_img_name+ext}").st_size
            x.validate_profile_image_size(filesize)

            #Validate image data filetype
            filetype = magic.from_file(f"{folder_path}/{new_cover_img_name+ext}")
            x.validate_image_datatype(filetype)
            
            #Crop
            path = f"{folder_path}/{new_cover_img_name+ext.lower()}"
            cropped_img = p.resize_crop_cover_image(path, x.USER_COVER_ASPECT)

            #Save new image
            cover_image_url = str(uuid.uuid4().hex+ext)
            cropped_img.save(x.ROOT+f"/images/cover_imgs/{cover_image_url}")

            #Add new image to query
            query += "user_img_cover = ?, "
            update_params.append(cover_image_url)

 
        #Validate Text fields
        user_full_name = x.validate_fullname()
        user_bio_text = x.validate_bio_text()
        user_bio_location = x.validate_bio_loc()
        user_bio_link = x.validate_bio_link()

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

        #Execute update query if anything has been added
        if update_params:

            #Open database
            db = x.db()
            
            updated_at = int(time.time())
            query += "user_updated_at = ?, "
            update_params.append(updated_at)

            #Remove the trailing comma and space from the query
            query = query.rstrip(", ")

            #Add the WHERE and user id
            query += " WHERE user_id = ?"
            update_params.append(logged_user["user_id"])

            db.execute(query, update_params)
            
            #Commit
            db.commit()

            #Delete image if new is added
            if "user_img_avatar" in query:
                url = x.ROOT+f"/images/avatar_imgs/{logged_user['user_img_avatar']}"
                os.remove(url, dir_fd = None)

            if "user_img_cover" in query:
                url = x.ROOT+f"/images/cover_imgs/{logged_user['user_img_cover']}"
                os.remove(url, dir_fd = None)
            
            #Set new cookie
            user = db.execute("SELECT * FROM users WHERE user_name = ?", (logged_user["user_name"],)).fetchone()
            user.pop("user_password")
    
            the_jwt = jwt.encode(user, x.COOKIE_SECRET, algorithm="HS256")

            result = x.getDomain()

            response.set_cookie("user", the_jwt, httponly=True, secure=result[0], path='/', domain=result[1])

        return {"info":"ok"}
    except Exception as ex:
        print(ex)
        if "db" in locals(): db.rollback()

        #Delete images if they were saved but update fails
        if (avatar_image_url):
            url = x.ROOT+f"/images/avatar_imgs/{avatar_image_url}"
            os.remove(url, dir_fd = None)

        if (cover_image_url):
            url = x.ROOT+f"/images/cover_imgs/{cover_image_url}"
            os.remove(url, dir_fd = None)
        try:
            response.status = ex.args[0]
            return {"info":ex.args[1]}
        except:
            response.status = 500
            return {"info":str(ex)}
    finally:
        if folder_path != "":
            x.delete_img_folder(folder_path)
        if 'db' in locals(): db.close()