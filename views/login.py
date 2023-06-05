from bottle import get, template, request, response
import x

@get("/login")
def _():
    x.disable_cache()
    #If a user is logged in and goes to login page redirect to home
    #logged_user = request.get_cookie("user", secret=x.COOKIE_SECRET)
    logged_user = x.request_cookie()
    if logged_user:
        response.status = 303
        response.set_header("Location", "/")
        return
    
    #Validation variables
    validation_vars = {
        "username": {
            "min": x.USERNAME_MIN_LEN,
            "max": x.USERNAME_MAX_LEN,
        },
        "password": {
            "min": x.PASSWORD_MIN_LEN,
            "max": x.PASSWORD_MAX_LEN,
        }
    }
    
    return template("login", validation_vars=validation_vars)
