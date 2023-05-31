from bottle import post, request, response
import x
import utils.formatNumber

@post("/api-unfollow")
def _():
    try:
        #check if someone is logged in
        user = request.get_cookie("user", secret=x.COOKIE_SECRET)
        if not user:
            raise Exception(400, "Not logged in")

        follower_id = user["user_id"]        
        db = x.db()

        user_followe_id = request.forms.get("user_followe_id", "")
        if not user_followe_id:
            raise Exception(400, "User not found")
      
        deleted_rows = db.execute("DELETE FROM following WHERE follower_fk=? AND followee_fk=?", (follower_id, user_followe_id)).rowcount 
        if not deleted_rows: raise Exception(400, "Unfollow successful, user not found")

        newfollowercount = db.execute("SELECT user_total_followers FROM users WHERE user_id=?", (user_followe_id,)).fetchone()
        if newfollowercount:
            newfollowercount = utils.formatNumber.human_format(newfollowercount["user_total_followers"])
    
        db.commit()
       
        return {"info": f"Succesful unfollow {user_followe_id}", "follower_count": newfollowercount}
    except Exception as ex:
        print(ex)
        response.status = ex.args[0]
        return {"info":ex.args[1]}
    finally:
        if "db" in locals(): db.close()