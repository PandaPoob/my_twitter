from bottle import get, template

@get("/test_follow")
def _():
    return template("test_follow")