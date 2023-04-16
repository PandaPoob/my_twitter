from bottle import get, template
import x
import os

@get("/verify-user/<user_api_key>")
def _(user_api_key):
    x.disable_cache()
    return template("verify_user", user_api_key=user_api_key, login_url=os.getcwd()+"login")
