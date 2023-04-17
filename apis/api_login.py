from bottle import post, request, response
import x
import bcrypt
import jwt

@post("/api-login")
def _():
    try:
        user = request.get_cookie("user", secret=x.COOKIE_SECRET)
        if user: return {"info":"success login", "user_name":user["user_name"]}

        # Validate
        user_name = x.validate_username()
        user_password = x.validate_password()
        
        # Connect to database
        db = x.db()
        user = db.execute("SELECT * FROM users WHERE user_name = ?", (user_name,)).fetchone()
       
        if not user: raise Exception(400, "Cannot login")
        if not bcrypt.checkpw(user_password.encode("utf-8"), user["user_password"]):
            raise Exception(400, "Invalid credentials")
        if user["user_account_status"] == "inactive": raise Exception(400, "Account has not been verified")
        try:
            import production
            is_cookie_https = True
        except:
            is_cookie_https = False

        user.pop("user_password")
        #print("pop", user)

        #TODO create jwt on cookies
        the_jwt = jwt.encode(user, x.COOKIE_SECRET, algorithm="HS256")
        #print(the_jwt)
        #jwt.decode(the_jwt, "the_secret", algorithms=["HS256"])

        
        response.set_cookie("user", the_jwt, httponly=True, secure=is_cookie_https)
        return {"info":"success login", "user_name":user["user_name"]}
    except Exception as e:
        print(e)
        try: # Controlled exception, usually comming from the x file
            response.status = e.args[0]
            return {"info":e.args[1]}
        except: # Something unknown went wrong
            response.status = 500
            return {"info":str(e)}
    finally:
        if "db" in locals(): db.close()