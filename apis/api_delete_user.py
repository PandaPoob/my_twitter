from bottle import post, request, response
import x
import bcrypt
import time
import os
import utils.sendEmail as s

@post("/api-delete-user")
def _():
    try:
        logged_user = x.request_cookie()

        if not logged_user:
           raise Exception(400, "Log in to delete account")
        
        #Decode cookie
        logged_user = x.decode_cookie(logged_user)
        
        #Validate password
        user_password = x.validate_password()

        #Open database
        db = x.db()

        #Get user
        user_id = logged_user["user_id"]
        user = db.execute("SELECT * FROM users WHERE user_id=? COLLATE NOCASE", (user_id,)).fetchone()

        #Validate password is correct
        if not bcrypt.checkpw(user_password.encode("utf-8"), user["user_password"]):
            raise Exception(400, "Incorrect password")
        
        updated_at = int(time.time())
        #Update user to deleted
        db.execute(f"UPDATE users SET user_account_status=?, user_updated_at=? WHERE user_id=?", (x.ACC_STATUS_DELETED, updated_at, user["user_id"]))

        #@todo Delete on cascade

        #Get all img urls
        tweet_images_url = db.execute("SELECT tweet_images.tweet_image_url FROM tweet_images INNER JOIN tweets ON tweet_images.tweet_image_tweet_fk = tweets.tweet_id WHERE tweets.tweet_user_fk=?", (user["user_id"],)).fetchall()

        #Deleting tweet images with subquery
        db.execute('''
        DELETE FROM tweet_images
        WHERE tweet_image_tweet_fk IN (
        SELECT tweets.tweet_id
        FROM tweets
        JOIN tweet_images ON tweets.tweet_id = tweet_images.tweet_image_tweet_fk
        WHERE tweets.tweet_user_fk = ?
        )
        ''', (user["user_id"],))
        
        #Delete user's tweets
        db.execute("DELETE FROM tweets WHERE tweet_user_fk = ?", (user["user_id"],))
       
        #Delete from following
        db.execute("DELETE FROM following WHERE follower_fk = ? OR followee_fk = ?", (user["user_id"], user["user_id"]))
  
        db.commit()

        #Delete cookie
        result = x.getDomain()
        response.delete_cookie("user", path='/', domain=result[1])

        #If commit is successful then remove all tweet images
        for i in tweet_images_url: 
            name = i["tweet_image_url"]
            url = x.ROOT+f"/images/tweet_imgs/{name}"
            os.remove(url, dir_fd = None)
 
        #Remove avatar image
        avatar_url = x.ROOT+f"/images/avatar_imgs/{user['user_img_avatar']}"
        os.remove(avatar_url, dir_fd = None)
        #Remove cover image
        cover_url = x.ROOT+f"/images/cover_imgs/{user['user_img_cover']}"
        os.remove(cover_url, dir_fd = None)
       
        #Send email
        #Creating the plain-text and HTML version of email
        try:
            import production
            root = "https://pandapoob.eu.pythonanywhere.com/"
        except:
            root = "http://127.0.0.1:3000/"
            
        text = """\
    See you later :(,
    Sorry to see you leave my exam project! Hopefully this isn't goodbye!"""
        html = f"""\
    <html>
    <head>
    <style>
        .body {{
        display: flex;
        justify-content: center;
        font-family: sans-serif;
      }}
      .container {{
        display: grid;
        background-color: black;
        color: white;
        border-radius: 2%;
        max-width: 400px;
        padding: 2rem;
      }}
      h2 {{
        text-align: center;
        margin-top: 0.5rem;
        margin-bottom: 0;
        font-size: 3rem;
        font-weight: 400;
      }}
      .welcome {{
        text-align: center;
        margin-top: 0.5rem;
        margin-bottom: 1.5rem;
        font-size: 14px;
      }}

    </style>
  </head>
        <body">
        <div class="container">
      <h2>See you later :(</h2>
      <p class="welcome">
        Sorry to see you leave my exam project! Hopefully this isn't goodbye! You are always welcome to sign up again!
      </p>
    </div>
  </body>
</html>
    """
        subject = "Freja's exam's deleted account"

        s.send_email(logged_user["user_email"], text, html, subject)
        

        return {"info": "Ok"}
    except Exception as ex:
        try:
            response.status = ex.args[0]
            return {"info":ex.args[1]}
        except:
            response.status = 500
            return {"info":str(ex)}
    finally:
        if "db" in locals(): db.close()