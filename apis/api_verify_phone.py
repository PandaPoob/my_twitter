from bottle import post, request, response
import x
import uuid
import time
import jwt

@post('/api-verify-phone')
def _():
    try:
        #Get api key from form
        user_api_key = request.forms.get("phone_user_api_key")
        if not user_api_key: raise Exception(400, "Missing request body")
        

        #Get phone number and validate
        user_phonenumber = x.validate_phone_number()

        #Open database
        db = x.db()
        
        #Check if number is already in use
        user = db.execute("SELECT * FROM active_users WHERE user_phonenumber=?", (user_phonenumber,)).fetchone()
        if user:
            raise Exception("Phone number is already in use")

        #Get user that matches api key
        user = db.execute("SELECT * FROM users WHERE user_api_key=? COLLATE NOCASE", (user_api_key,)).fetchone()

        #The api key does not exists, it is either wrong or has been changed/updated
        if not user: raise Exception(400, "An error occurred")
        
        if user["user_twitter_status"] == x.USER_TWITTER_GOLD: raise Exception(400, "User's status is already golden and has their phone number verified")

        #New values
        new_api_key = str(uuid.uuid4().hex)
        updated_at = int(time.time())

        #Update twitter status, phone and key and updated at 
        db.execute(f"UPDATE users SET user_twitter_status=?, user_phonenumber=?, user_api_key=?, user_updated_at=? WHERE user_api_key=?", (x.USER_TWITTER_GOLD, user_phonenumber, new_api_key, updated_at, user_api_key,))

        #Commit
        db.commit()
        
        #Set new cookie
        user = db.execute("SELECT * FROM users WHERE user_name = ?", (user["user_name"],)).fetchone()
        user.pop("user_password")
    
        the_jwt = jwt.encode(user, x.COOKIE_SECRET, algorithm="HS256")

        result = x.getDomain()

        response.set_cookie("user", the_jwt, httponly=True, secure=result[0], path='/', domain=result[1])
        

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