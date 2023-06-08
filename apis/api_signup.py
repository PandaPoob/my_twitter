from bottle import post, response
import x
import bcrypt
import uuid
import time
import utils.sendEmail
import os

@post("/api-signup")
def _():
    try:
        #Declare imgs
        avatar_img_id = ""
        cover_img_id = ""
        
        #Validate
        user_fullname = x.validate_fullname()
        user_email = x.validate_user_email()
        user_birthday = x.validate_user_birthday()
        user_name = x.validate_username()
        user_password = x.validate_password()
        x.validate_user_confirm_password()
        
        #Salt to hash password
        salt = bcrypt.gensalt()

        #Open database        
        db = x.db()

        #Check that email is not already in use
        check_email = db.execute("SELECT user_email FROM users WHERE user_email=? AND user_account_status != ?", (user_email, x.ACC_STATUS_DELETED)).fetchone()
        if check_email: raise Exception(400, "Email is already in use")
        
        #Check that user name is not taken
        check_username = db.execute("SELECT user_name FROM users WHERE user_name=? AND user_account_status != ?", (user_name, x.ACC_STATUS_DELETED)).fetchone()
        if check_username: raise Exception(400, "Username is already taken")

        #API KEY
        user_api_key = str(uuid.uuid4().hex)

        #Prepare and generate avatar img
        avatar_path = x.ROOT+f"/images/placeholders/avatar_default.jpg"
        avatar_new_path = "/images/avatar_imgs/"
        avatar_img_id = x.generate_image(avatar_path, avatar_new_path)

        #Prepare and generate cover img
        cover_path = x.ROOT+f"/images/placeholders/cover_default.jpg"
        cover_new_path = "/images/cover_imgs/"
        cover_img_id = x.generate_image(cover_path, cover_new_path)
        

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
    "user_img_avatar": avatar_img_id,
    "user_img_cover": cover_img_id,
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

        db.commit()

        
        # Creating the plain-text and HTML version of email
        try:
            import production
            root = "https://pandapoob.eu.pythonanywhere.com/"
        except:
            root = "http://127.0.0.1:3000/"
            
        text = """\
    Welcome!,
    Thank you for signing up to my exam project!"""
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

      #button {{
        background-color: #1d9bf0;
        color: white;
        text-decoration: none;
        line-height: 30px; 
        text-align: center;
        height: 2rem;
        border-radius: 1rem;
        cursor: pointer;
        font-weight: bold;
      
      }}
      .button:hover {{
        opacity: 90%;
        cursor: pointer;
      }}

      .disclaimer {{
        font-size: 12px;
      }} 
    </style>
  </head>
        <body">
        <div class="container">
      <h2>Welcome!</h2>
      <p class="welcome">
        Thank you for signing up to my exam project! You can verify your account
        by clicking on the link below.
      </p>
      <a id="button" href="{root+"verify-user/"+user_api_key}">Verifiy account</a>

      <p class="disclaimer">
        *Please note that this project is in beta and bugs may occur. If you
        find any you are welcome to contact our team, aka. Freja on sender's
        email.
      </p>
    </div>
  </body>
</html>
    """
        subject = "Freja's exam's site signup"
        utils.sendEmail.send_email(user_email, text, html, subject)

        return {
			"info" : "user created", 
            "user_name": user_name
		}                
    except Exception as ex:
        print(ex)
        #Delete new imgs
        if avatar_img_id:
            avatar_img = x.ROOT+f"/images/avatar_imgs/{avatar_img_id}"
            os.remove(avatar_img, dir_fd = None)
        if cover_img_id:
            cover_img = x.ROOT+f"/images/cover_imgs/{cover_img_id}"
            os.remove(cover_img, dir_fd = None)
        
        try:
            response.status = ex.args[0]
            return {"info":ex.args[1]}
        except:
            response.status = 500
            return {"info":str(ex)}
    finally:
        if "db" in locals(): db.close()