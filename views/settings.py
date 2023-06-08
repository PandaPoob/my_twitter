from bottle import get, template, response
import x

@get("/settings")
def _():

    x.disable_cache()
    logged_user = x.request_cookie()
    
    if not logged_user:
        response.status = 303
        response.set_header("Location", "/login")
        return

    if logged_user:
        logged_user = x.decode_cookie(logged_user)

    #Validation variables
    pass_val = {
            "max": x.PASSWORD_MAX_LEN,
            "min": x.PASSWORD_MIN_LEN,
    }

    return template("settings", logged_user=logged_user, pass_val=pass_val)