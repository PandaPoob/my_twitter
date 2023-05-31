from bottle import get, template
import x

@get("/forgot-password")
def _():
    x.disable_cache()
    email_val = {
            "min": x.USER_EMAIL_MIN,
            "max": x.USER_EMAIL_MAX,    
    }
    return template("forgot_password", email_val=email_val)