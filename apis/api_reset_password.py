from bottle import post, request, response
import x
import uuid
import time
import bcrypt
import utils.validateResetToken as v

@post('/api-reset-password')
def _():
    try:
        
        #Validate password
        user_password = x.validate_password()
        x.validate_user_confirm_password()
        
        #Get api key from form
        token = request.forms.get("token")
        if not token: raise Exception(400, "Missing request body")

        #Decode token
        user_api_key = v.validate_reset_token(token)

        #Open database
        db = x.db()
        
        #Get user that matches api key
        user = db.execute("SELECT user_id FROM users WHERE user_api_key=? COLLATE NOCASE", (user_api_key,)).fetchone()
        
        #The api key does not exists, it is either wrong or has been changed/updated
        if not user: raise Exception(400, "An error occurred")

        #Hash password
        salt = bcrypt.gensalt()
        new_pw = bcrypt.hashpw(user_password.encode('utf-8'), salt)

        #New api key
        new_api_key = str(uuid.uuid4().hex)

        #Updated at
        updated_at = int(time.time())

        #Update account password
        db.execute(f"UPDATE users SET user_password=?, user_api_key=?, user_updated_at=? WHERE user_api_key=?", (new_pw, new_api_key, updated_at, user_api_key,))
        
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

