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

        #Backend validation
        #Validate tweet text
        tweet_text = x.validate_tweet_field_text()
        
        #Make sure it is string
        if not tweet_text:
            tweet_text = str("")
    
        #Get tweet images
        tweet_images = request.files.getall("tweet_field_image")

        #Max 4 images
        if len(tweet_images) > x.TWEET_MAX_IMG_NO: raise Exception(400, "tweet_field_image max images is 4")

        if len(tweet_images) >= 1 and tweet_images[0].filename != "empty":
            #Validate images
            for tweet_image in tweet_images:

            #Validate file type on ext
                x.validate_image_type(tweet_image)

                #Upload to temp folder
                name, ext = os.path.splitext(tweet_image.filename)
                tweet_image_name = str(uuid.uuid4().hex)
                tweet_image.save(f"images/temp_imgs/{tweet_image_name+ext}")

                #Validate image size
                filesize = os.stat(f"images/temp_imgs/{tweet_image_name+ext}").st_size
                x.validate_image_size(filesize)

                #Validate image data filetype
                filetype = magic.from_file(f"images/temp_imgs/{tweet_image_name+ext}")
                x.validate_image_datatype(filetype)

        #Validate tweet content
        elif tweet_images[0].filename == "empty" and not tweet_text: raise Exception(400, "Tweet must have atleast 1 image or text")
        
        #REMEMBER DELETE IMAGES IN TEMP AFTER SUCCESFULL PUSH
        #Decode cookie
        if logged_user:        
            logged_user = x.decode_cookie(logged_user)
            x.disable_cache()
        
            #Prepare tweet data
            tweet_id = str(uuid.uuid4().hex)
            tweet_created_at = int(time.time())
            tweet = {
                "tweet_id": tweet_id,
                "tweet_slug": str(uuid.uuid4().hex),
                "tweet_user_fk": logged_user["user_id"],
                "tweet_created_at": tweet_created_at,
                "tweet_updated_at": 0,
                "tweet_field_text": tweet_text,
                "tweet_field_images": 0,
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
  
            #Format date to frontend and immediate display      
            #if tweet['tweet_created_at']:
             #   month = time.strftime('%#m', time.localtime(tweet['tweet_created_at']))
              #  day = time.strftime('%#d', time.localtime(tweet['tweet_created_at']))
               # tweet['tweet_created_at'] = f"{calendar.month_abbr[int(month)]} {day}"

            #
            image_amount = 0
            #Check if there are images
            if len(tweet_images) >= 1 and tweet_images[0].filename != "empty":
                #Loop, save and post
                for i in range(len(tweet_images)): 
                    index = int(i)
                    #Upload to image folder
                    name, ext = os.path.splitext(tweet_images[i].filename)
                    tweet_image_url = str(uuid.uuid4().hex+ext)
                    tweet_images[i].save(f"images/tweet_imgs/{tweet_image_url}")
                    
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
                    total_rows_inserted = db.execute(f"INSERT INTO tweet_images VALUES({img_values})", tweet_image_data).rowcount
                    
                    #for every count +1 into variable
                    image_amount = total_rows_inserted + image_amount
                    
            print(image_amount)
            #Commit
            db.commit()
            #Return necessary info 
        return {"info":"ok", "tweet":tweet, "images": tweet_image_data}
    except Exception as ex:
        try:
            response.status = ex.args[0]
            return {"info":ex.args[1]}
        except:
            response.status = 500
            return {"info":str(ex)}
        finally:
            #clear temp images
            dir = 'images/temp_imgs'
            x.clear_img_folder(dir)
    finally:
        #clear temp images
        dir = 'images/temp_imgs'
        x.clear_img_folder(dir)
        if "db" in locals(): db.close()