from bottle import post, request, response
import x
import time

@post("/api-follow")
def _():
    try:
        #check if someone is logged in
        user = request.get_cookie("user", secret=x.COOKIE_SECRET)
        if not user:
            raise Exception(400, "Not logged in")

        id = user["user_id"]        
        db = x.db()
        user_follower_id = db.execute("SELECT user_id FROM users WHERE user_id=?", (id,)).fetchone()
       
        if not user_follower_id:
            raise Exception(400, "User does not exist")

        user_followe_id = request.forms.get("user_followe_id", "")
        if not user_followe_id:
            raise Exception(400, "Cannot follow")
        timestamp = int(time.time())
        db.execute("INSERT INTO following VALUES(?, ?, ?)",(user_follower_id['user_id'], user_followe_id, timestamp))
        db.commit()
       
        return {"info": f"Succesful follow {user_followe_id, user_follower_id, timestamp}"}
    except Exception as ex:
        print("ERROR", ex)
        print("type", type(ex))
        if str(ex).contains("UNIQUE contraint failed"):
            response.status = 400
            return {"info":str(ex)}
        response.status = ex.args[0]
        return {"info":ex.args[1]}
    finally:
        if "db" in locals(): db.close()