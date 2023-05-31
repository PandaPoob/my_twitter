from bottle import post, request, response
import x
import uuid
import time
import bcrypt

@post('/api-reset-password')
def _():
    try:
        
        #Validate password
        user_password = x.validate_password()
        x.validate_user_confirm_password()
        
        #Get api key from form
        user_api_key = request.forms.get("user_api_key")
        if not user_api_key: raise Exception(400, "Missing request body")
        
        #Open database
        db = x.db()
        
        #Get user that matches api key
        user = db.execute("SELECT user_id FROM users WHERE user_api_key=? COLLATE NOCASE", (user_api_key,)).fetchone()
        
        #The api key does not exists, it is either wrong or has been changed/updated
        if not user: raise Exception(400, "An error occurred")

        #Hash password
        salt = bcrypt.gensalt()
        new_pw = bcrypt.hashpw(user_password.encode('utf-8'), salt)

        #Update account password
        db.execute(f"UPDATE users SET user_password=? WHERE user_api_key=?", (new_pw, user_api_key,))
        
        #New api key
        new_api_key = str(uuid.uuid4().hex)
    
        #Updated at
        updated_at = int(time.time())

        #Assign new api key
        db.execute(f"UPDATE users SET user_api_key=? WHERE user_id=?", (new_api_key, user["user_id"],))
        db.execute(f"UPDATE users SET user_updated_at=? WHERE user_id=?", (updated_at, user["user_id"],))
      

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

