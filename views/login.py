from bottle import get, template, request
import x
import time
import calendar
import formatNumber

@get("/login")
def _():
    x.disable_cache()
    logged_user = request.get_cookie("user", secret="my-secret")
    if logged_user:
        response.status = 303
        response.set_header("Location", "/")

    error = request.query.error.replace("_", " ")
    print(error)
    return template("login", username_min_length=x.USERNAME_MIN_LEN, username_max_length=x.USERNAME_MAX_LEN, password_min_length=x.PASSWORD_MIN_LEN, password_max_length=x.PASSWORD_MAX_LEN, username_error=x.usernameerror, password_error=x.passerror, error=error)
