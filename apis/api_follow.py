from bottle import post, request, response

@post("/api-follow")
def _():
    try:
        # TODO: get user form cookie
        # request.get_cookie("user")
        # TODO: get user id from the cookie
        # TODO: validate followee id
        # TODO: connect to database
        # TODO: insert into followers table
        user_followe_id = request.forms.get("user_followe_id", "")
        return {"info": f"Succesful follow {user_followe_id}"}
    except Exception as ex:
        print(ex)
        pass
    finally:
        pass