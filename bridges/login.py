from bottle import post, request, response
import x
import time

@post("/login")
def _():
    try:
        x.validate_login()
        db = x.db()
        
        username = request.forms.get("login_user_name")
        
        user = db.execute("SELECT * FROM users WHERE user_name = ? COLLATE NOCASE", (username,)).fetchall()[0]
        
        #if not user:
         #   error = "User does not exist"
          #  print(error)
           # raise Exception(error)
            #return
        
        password = request.forms.get("login_password")

        if password != user["user_password"]:
            #print("wrong password")
            error = "Wrong_password"
            raise Exception(error)
            return

        user.pop("user_password")
        print("after", user)
        response.set_cookie("user", user, secret="my-secret", httponly=True)
        response.status = 303
        response.set_header("Location", "/")
        
        return
    except Exception as ex:
        print(ex)
        errormessage = str(ex)
        error = str(ex)
        if error == "list index out of range":
            errormessage = "Username_does_not_exist"
        
        response.status = 303
        response.set_header("Location", f"/login?error={errormessage}")
        return

    finally:
        if "db" in locals(): db.close()