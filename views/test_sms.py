from bottle import get, template

@get("/test_sms")
def _():
    return template("test_sms")