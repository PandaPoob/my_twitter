from bottle import get, template
import x

@get("/signup")
def _():
    x.disable_cache()
    validation_vars = {
        "username": {
            "min": x.USERNAME_MIN_LEN,
            "max": x.USERNAME_MAX_LEN,
        },

        "email": {
            "min": x.USER_EMAIL_MIN,
            "max": x.USER_EMAIL_MAX,
        },

         "birthday": {
            "min": x.USER_BIRTHDAY_MIN   
        },

        "fullname": {
            "min": x.USER_FULL_NAME_MIN,
            "max": x.USER_FULL_NAME_MAX
        },
        "password": {
            "min": x.PASSWORD_MIN_LEN,
            "max": x.PASSWORD_MAX_LEN,
        }
       
    }

    return template("signup", validation_vars=validation_vars)