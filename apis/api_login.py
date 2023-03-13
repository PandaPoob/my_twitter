from bottle import post, request, response
import x
import bcrypt

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

        try:
            import production
            is_cookie_https = True
        except:
            is_cookie_https = False

        hashed_password = bcrypt.hashpw(user["user_password"].encode('utf8'), bcrypt.gensalt())
        input_hashed_password = bcrypt.hashpw(user_password.encode('utf8'), bcrypt.gensalt())
        print(user["user_password"], hashed_password)
        print(user_password, input_hashed_password)
        if bcrypt.checkpw(input_hashed_password, hashed_password):
            print("match")
        else:
            print("does not match")

        if user_password != user["user_password"]:
            
            #print("wrong password")
            error = "Wrong_password"
            raise Exception(error)
            return
        
        user.pop("user_password")
        #print("pop", user)
        response.set_cookie("user", user, secret=x.COOKIE_SECRET, httponly=True, secure=is_cookie_https)
        return {"info":"success login", "user_name":user["user_name"]}
    except Exception as e:
        print("here", e)
        try: # Controlled exception, usually comming from the x file
            response.status = e.args[0]
            return {"info":e.args[1]}
        except: # Something unknown went wrong
            response.status = 500
            return {"info":str(e)}
    finally:
        if "db" in locals(): db.close()