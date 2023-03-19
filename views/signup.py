from bottle import get, template, request, response
import x

@get("/signup")
def _():
    x.disable_cache()

    return template("signup", fullname_min_length=x.USER_FULL_NAME_MIN, fullname_max_length=x.USER_FULL_NAME_MAX, fullname_error=x.fullnameerror, email_error=x.useremailerror, birthday_max=x.USER_BIRTHDAY_MAX, birthday_error=x.userbirthdayminerror, username_min_length=x.USERNAME_MIN_LEN, username_max_length=x.USERNAME_MAX_LEN, username_error=x.usernameerror, password_min_length=x.PASSWORD_MIN_LEN, password_max_length=x.PASSWORD_MAX_LEN, password_error=x.passerror)