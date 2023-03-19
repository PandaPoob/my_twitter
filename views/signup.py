from bottle import get, template, request, response
import x

@get("/signup")
def _():
    x.disable_cache()

    return template("signup")