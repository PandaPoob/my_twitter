from bottle import post, response
import x
import bcrypt
import jwt

@post("/api-login")
def _():
    try:
        #why is this here?
        #user = request.get_cookie("user", secret=x.COOKIE_SECRET)
        #if user: return {"info":"success login", "user_name":user["user_name"]}

        #Validate
        user_name = x.validate_username()
        user_password = x.validate_password()
        
        #Connect to database
        db = x.db()
        user = db.execute("SELECT * FROM users WHERE user_name = ?", (user_name,)).fetchone()

        #Check if user exists
        if not user: raise Exception(400, "Invalid credentials")

        if user["user_account_status"] == x.ACC_STATUS_DELETED: raise Exception(400, "Invalid credentials")

        #Check if password is correct
        if not bcrypt.checkpw(user_password.encode("utf-8"), user["user_password"]):
            raise Exception(400, "Invalid credentials")
        
        #User needs to verify
        if user["user_account_status"] == x.ACC_STATUS_INACTIVE: raise Exception(401, "Account has not been verified")

        #Removing pw from cookie
        user.pop("user_password")

        #Using jwt to encode user cookie
        the_jwt = jwt.encode(user, x.COOKIE_SECRET, algorithm="HS256")
        
        result = x.getDomain()

        response.set_cookie("user", the_jwt, httponly=True, secure=result[0], path='/', domain=result[1])
        return {"info":"success login", "user_name":user["user_name"]}
    except Exception as e:
        print(e)
        try:
            response.status = e.args[0]
            return {"info":e.args[1]}
        except:
            response.status = 500
            return {"info":str(e)}
    finally:
        if "db" in locals(): db.close()