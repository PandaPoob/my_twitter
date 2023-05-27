from bottle import put, request, response
import x
import uuid
import time

@put('/api-verify-email')
def _():
    try:
        #Get api key from form
        user_api_key = request.forms.get("welcome_user_api_key")
        if not user_api_key: raise Exception(400, "Missing request body")
        
        #Open database
        db = x.db()

        #Get user that matches api key
        user = db.execute("SELECT * FROM users WHERE user_api_key=? COLLATE NOCASE", (user_api_key,)).fetchone()

        #The api key does not exists, it is either wrong or has been changed/updated
        if not user: raise Exception(400, "An error occurred")
        
        #User id
        user_id = user["user_id"]
        
        #Update account status to active
        db.execute(f"UPDATE users SET user_account_status=? WHERE user_api_key=?", (x.ACC_STATUS_ACTIVE, user_api_key,))

        #New api key
        new_api_key = str(uuid.uuid4().hex)

        updated_at = int(time.time())
        #Assign new api key
        db.execute(f"UPDATE users SET user_api_key=? WHERE user_id=?", (new_api_key, user_id))
        db.execute(f"UPDATE users SET user_updated_at=? WHERE user_id=?", (updated_at, user_id))

        #TODO update user's updated at_

        #Commit
        db.commit()

        return {"info":"ok"}
    except Exception as ex:
        print(ex)
        if "db" in locals(): db.rollback()
        try:
            response.status = ex.args[0]
            return {"info":ex.args[1]}
        except:
            response.status = 500
            return {"info":str(ex)}
    finally:
        if 'db' in locals(): db.close()