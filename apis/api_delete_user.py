from bottle import post, request, response
import requests
import x
import secrets
import string

@post("/api-delete-user")
def _():
    try:
        logged_user = x.request_cookie()

        if not logged_user:
           raise Exception(400, "Log in to verify")
        
        #Decode cookie
        logged_user = x.decode_cookie(logged_user)
        
        user_id = logged_user["user_id"]

        #Open database
        db = x.db()

        #Set user status to deleted
        #@todo Delete on cascade
        
        #Delete all tweets
        #Delete all tweet images
        #Delete from following


      
        #Set the user api key with code
        #db.execute(f"UPDATE users SET user_api_key=? WHERE user_id=?", (code, user_id))

        
  
        #db.commit()
        #If commit is successful then remove all tweet images
        #Remove avatar and profile image
       
        return {"info": "Ok"}
    except Exception as ex:
        try:
            response.status = ex.args[0]
            return {"info":ex.args[1]}
        except:
            response.status = 500
            return {"info":str(ex)}
    finally:
        if "db" in locals(): db.close()