from bottle import post, request, response
import x
import uuid
import time
import os
import magic

@post("/tweet")
def _():
    try:
        x.disable_cache()
        #Check if user is logged in
        logged_user = x.request_cookie()
        if not logged_user:
            raise Exception(400, "Log in to tweet")

        #Validate tweet text
        tweet_text = x.validate_tweet_field_text()
        
        #Make sure it is string
        if not tweet_text:
            tweet_text = str("")
    
        #Get tweet images
        tweet_images = request.files.getall("tweet_field_image")

        #Get image amount
        image_amount = 0
        if len(tweet_images) >= 1 and tweet_images[0].filename == "empty":
            image_amount = 0
        elif len(tweet_images) > x.TWEET_MAX_IMG_NO:
            #Max 4 images
            raise Exception(400, "tweet_field_image max images is 4")
        else:
            image_amount = len(tweet_images)

        #Tweet id
        tweet_id = str(uuid.uuid4().hex)
        
        folder_path = ""
        #Validate images
        if image_amount >=1:
            
            #Create temp tolder
            folder_name = tweet_id
            directory_path = x.ROOT+"/images/temp_imgs/"
            folder_path = os.path.join(directory_path, folder_name)
            os.makedirs(folder_path)

            #Loop images
            for tweet_image in tweet_images:

            #Validate file type on ext
                x.validate_image_type(tweet_image)

                #Upload to temp folder
                name, ext = os.path.splitext(tweet_image.filename)
                tweet_image_name = str(uuid.uuid4().hex)
                tweet_image.save(f"{folder_path}/{tweet_image_name+ext}")

                #Validate image size
                filesize = os.stat(f"{folder_path}/{tweet_image_name+ext}").st_size
                x.validate_image_size(filesize)

                #Validate image data filetype
                filetype = magic.from_file(f"{folder_path}/{tweet_image_name+ext}")
                x.validate_image_datatype(filetype)

        #Validate tweet content
        if image_amount == 0 and not tweet_text: raise Exception(400, "Tweet must have atleast 1 image or text")
        
        #Decode cookie
        if logged_user:        
            logged_user = x.decode_cookie(logged_user)
            x.disable_cache()
        
            #Prepare tweet data
            tweet_created_at = int(time.time())
            tweet = {
                "tweet_id": tweet_id,
                "tweet_slug": str(uuid.uuid4().hex),
                "tweet_user_fk": logged_user["user_id"],
                "tweet_created_at": tweet_created_at,
                "tweet_updated_at": 0,
                "tweet_field_text": tweet_text,
                "tweet_field_images": image_amount,
                "tweet_total_replies": 0,
                "tweet_total_likes": 0,
                "tweet_total_retweets": 0,
                "tweet_total_views": 0,
                "tweet_parent_id": "",
                "tweet_type": x.TWEET_TYPE_DEFAULT,
            }
            values = x.prepare_values(tweet)

            #Open database
            db = x.db()

            #Insert tweets into database
            db.execute(f"INSERT INTO tweets VALUES({values})", tweet)
  
            saved_images = []
            #Check if there are images
            if image_amount >= 1:
                
                #Loop, save and post
                for i in range(len(tweet_images)): 
                    try:
                        index = int(i)
                        #Upload to image folder
                        name, ext = os.path.splitext(tweet_images[i].filename)
                        tweet_image_url = str(uuid.uuid4().hex+ext)
                        tweet_images[i].save(x.ROOT+f"/images/tweet_imgs/{tweet_image_url}")

                        #Store url of saved imgs
                        saved_images.append(tweet_image_url)

                        #Prepare image data
                        tweet_image_data = {
                            "tweet_image_id": str(uuid.uuid4().hex),
                            "tweet_image_tweet_fk": tweet_id,
                            "tweet_image_url": tweet_image_url,
                            "tweet_image_order": index,
                            "tweet_image_created_at": tweet_created_at,
                        }
                        img_values = x.prepare_values(tweet_image_data)

                        #Insert tweet images in database
                        db.execute(f"INSERT INTO tweet_images VALUES({img_values})", tweet_image_data)
                    except Exception as ex:
                        #If insert fails then remove all images from folder
                    
                        for saved_image in saved_images:
                            #url = os.getcwd()+f"/images/tweet_imgs/{saved_image}"
                            url = x.ROOT+f"/images/tweet_imgs/{saved_image}"
                            os.remove(url, dir_fd = None)
                        
                        raise Exception(500, str(ex))

            #Commit
            db.commit()
            author = { 
                "user_name": logged_user["user_name"], 
                "full_name": logged_user["user_full_name"], 
                "img_avatar": logged_user["user_img_avatar"], 
                "twitter_status": logged_user["user_twitter_status"]
                }
            
        return {"info":"ok", "content": {"tweet":tweet, "image_amount":image_amount, "images": saved_images, "author": author}}
    
    except Exception as ex:
        try:
            response.status = ex.args[0]
            return {"info":ex.args[1]}
        except:
            response.status = 500
            return {"info":str(ex)}
        finally:
            #Clear temp images
            x.delete_img_folder(folder_path)
            if "db" in locals(): db.rollback()
    finally:
        #Clear temp images
        x.delete_img_folder(folder_path)
        if "db" in locals(): db.close()