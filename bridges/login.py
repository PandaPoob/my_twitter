from bottle import post, request, response
import x
import time

@post("/login")
def _():
    try:
        x.validate_login()
        db = x.db()

        username = request.forms.get("login_user_name")
        user = db.execute("SELECT * FROM users WHERE user_name=? COLLATE NOCASE", (username,)).fetchall()[0]
        
        if not user:
            print("User does not exist")
            response.status = 303
            response.set_header("Location", "/login")
            return
        
        password = request.forms.get("login_password")

        if password != user["user_password"]:
            print("wrong password")
            response.status = 303
            response.set_header("Location", "/login")
            return
    
        
        response.set_cookie("user", user, secret="my-secret", httponly=True)
        response.status = 303
        response.set_header("Location", "/")
        
        return
    except Exception as ex:
        print(ex)
        return

    finally:
        if "db" in locals(): db.close()