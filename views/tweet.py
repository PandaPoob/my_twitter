from bottle import get, template, response, request

@get("/<username>/status/<slug>")
def _(username, slug):
    try:
        return template("tweet")

    except Exception as ex:
        print(ex)
        return "error"

    finally:
        pass