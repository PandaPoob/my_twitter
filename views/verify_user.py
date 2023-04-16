from bottle import get, template
import x

@get("/verify-user/<user_api_key>")
def _(user_api_key):
    x.disable_cache()
    return template("verify_user", user_api_key=user_api_key)
