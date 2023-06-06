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

    return template("settings", logged_user=logged_user)