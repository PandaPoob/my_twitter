from bottle import get, template, response
import x

@get("/verified")
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
    phone_val = {
            "max": x.USER_MAX_PHONE,
            "min": x.USER_MIN_PHONE,
    }

    return template("verified", logged_user=logged_user, phone_val=phone_val)