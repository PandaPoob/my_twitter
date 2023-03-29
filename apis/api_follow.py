from bottle import post, request, response
import x
import time
import formatNumber

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
        newfollowercount = db.execute("SELECT user_total_followers FROM users WHERE user_id=?", (user_followe_id,)).fetchone()
        if newfollowercount:
            newfollowercount = formatNumber.human_format(newfollowercount["user_total_followers"])
    
        db.commit()                  
        return {"info": f"Succesful followed {user_followe_id}", "follower_count": newfollowercount}
    except Exception as ex:

        if "UNIQUE constraint failed" in str(ex):
            response.status = 400
            return {"info":str(ex)}
     
        response.status = ex.args[0]
        return {"info":ex.args[1]}
    finally:
        if "db" in locals(): db.close()