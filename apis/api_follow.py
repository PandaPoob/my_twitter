from bottle import post, request, response
import x
import time

@post("/api-follow")
def _():
    try:
        #Get cookie user
        logged_user = x.request_cookie()

        if not logged_user:
            raise Exception(400, "Log in to follow")
        
        #Decode cookie
        if logged_user:        
            logged_user = x.decode_cookie(logged_user)

        #Open database   
        db = x.db()

        #Confirm cookie user exists
        user_follower_id = db.execute("SELECT user_id FROM active_users WHERE user_id=?", (logged_user["user_id"],)).fetchone()
        if not user_follower_id:
            raise Exception(400, "User does not exist")

        #Get user_followe_id
        user_followe_id = request.forms.get("user_followe_id", "")

        #Confirm this user exists
        user_followe_id = db.execute("SELECT user_id FROM active_users WHERE user_id=?", (user_followe_id,)).fetchone()

        if not user_followe_id:
            raise Exception(400, "Cannot follow")
        
        if user_follower_id == user_followe_id["user_id"]: raise Exception(400, "User cannot follow themselves")
        
        

        follow = {
            "follower_fk": user_follower_id['user_id'],
            "followee_fk": user_followe_id['user_id'],
            "following_created_at": int(time.time()),
        }
    
        values = x.prepare_values(follow)

        db.execute(f"INSERT INTO following VALUES({values})", follow)
        
        db.commit()                  
        return {"info": f"Succesfully followed"}
    except Exception as ex:
        try:
            response.status = ex.args[0]
            return {"info":ex.args[1]}
        except:
            response.status = 500
            return {"info":str(ex)}
    finally:
        if "db" in locals(): db.close()