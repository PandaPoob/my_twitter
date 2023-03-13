from bottle import get, template, request, response
import x

@get("/login")
def _():
    x.disable_cache()
    logged_user = request.get_cookie("user", secret=x.COOKIE_SECRET)
    if logged_user:
        response.status = 303
        response.set_header("Location", "/")
        return

    return template("login", username_min_length=x.USERNAME_MIN_LEN, username_max_length=x.USERNAME_MAX_LEN, password_min_length=x.PASSWORD_MIN_LEN, password_max_length=x.PASSWORD_MAX_LEN, username_error=x.usernameerror, password_error=x.passerror)
