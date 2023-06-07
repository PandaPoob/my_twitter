from bottle import post, response
import x
import utils.generateResetToken as g
import uuid
import bcrypt
import utils.sendEmail as s

@post('/api-forgot-password')
def _():
    try:

        #Validate email
        user_email = x.validate_user_email()

        #Open database        
        db = x.db()

        #Check if email exists
        user = db.execute("SELECT user_email, user_account_status, user_api_key FROM users WHERE user_email=?", (user_email,)).fetchone()
        
        if not user: raise Exception(400, "Email does not exists in our system")

        #Check if account is active
        if not user["user_account_status"] == x.ACC_STATUS_ACTIVE: raise Exception(400, "Activate your account before resetting the password")
        

        #Create temp pw
        temp_pw = str(uuid.uuid4().hex)
        salt = bcrypt.gensalt()
        temp_pw = bcrypt.hashpw(temp_pw.encode('utf-8'), salt)
        
        #Update password
        db.execute(f"UPDATE users SET user_password=? WHERE user_email=?", (temp_pw, user["user_email"],))

        #Create token with api key
        reset_token = g.generate_reset_token(user["user_api_key"])
        
        # Creating the plain-text and HTML version of email
        try:
            import production
            root = "https://pandapoob.eu.pythonanywhere.com/"
        except:
            root = "http://127.0.0.1:3000/"
            
        text = """\
    Reset password,
     Your account's password has been reset, to log in please follow the link below to create a new password"""
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
        font-size: 2rem;
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
      <h2>Reset password</h2>
      <p class="welcome">
        Your account's password has been reset, to log in please follow the link below to create a new password 
      </p>
      <a id="button" href="{root+"reset-password/"+reset_token}">Reset password</a>

      <p class="disclaimer">
        *Please note that the link will expire after {x.RESET_TOKEN_TIME} hour and you will have to reset your password again on {root}/forgot-password.
      </p>
    </div>
  </body>
</html>
    """
        subject = "Reset password on Freja's site"
        s.send_email(user["user_email"], text, html, subject)

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