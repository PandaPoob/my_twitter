from bottle import post, request, response
import x

@post("/api-unfollow")
def _():
    try:
        #Get cookie user
        logged_user = x.request_cookie()

        if not logged_user:
            raise Exception(400, "Log in to unfollow")
        
        #Decode cookie
        if logged_user:        
            logged_user = x.decode_cookie(logged_user)

        #Open database       
        db = x.db()

        #Confirm cookie user exists
        user_unfollower_id = db.execute("SELECT user_id FROM active_users WHERE user_id=?", (logged_user["user_id"],)).fetchone()
        if not user_unfollower_id:
            raise Exception(400, "User does not exist")

        #Get the user_unfollowe_id
        user_unfollowe_id = request.forms.get("user_unfollowe_id", "")
        if not user_unfollowe_id:
            raise Exception(400, "User not found")
        
        #remove following from table
      
        deleted_rows = db.execute("DELETE FROM following WHERE follower_fk=? AND followee_fk=?", (user_unfollower_id["user_id"], user_unfollowe_id)).rowcount 
        
        if not deleted_rows: raise Exception(400, "Unfollow successful, users not found")

        db.commit()
       
        return {"info": f"Succesfully unfollowed"}
    except Exception as ex:
        print(ex)
        response.status = ex.args[0]
        return {"info":ex.args[1]}
    finally:
        if "db" in locals(): db.close()