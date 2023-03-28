from bottle import post, request, response
import x
import time

@post("/api-unfollow")
def _():
    try:
        #check if someone is logged in
        user = request.get_cookie("user", secret=x.COOKIE_SECRET)
        if not user:
            raise Exception(400, "Not logged in")

        id = user["user_id"]        
        db = x.db()
        user_follower_id = db.execute("SELECT user_id FROM users WHERE user_id=?", (id,)).fetchone()
        #print(user)
        if not user_follower_id:
            raise Exception(400, "User does not exist")

        user_followe_id = request.forms.get("user_followe_id", "")
        if not user_followe_id:
            raise Exception(400, "Cannot unfollow")
      
        db.execute(f"DELETE FROM following WHERE follower_fk=? AND followee_fk=?", (id, user_followe_id))  
        db.commit()
       
        return {"info": f"Succesful unfollow {user_followe_id, user_follower_id}"}
    except Exception as ex:
        print(ex)
        response.status = ex.args[0]
        return {"info":ex.args[1]}
    finally:
        if "db" in locals(): db.close()