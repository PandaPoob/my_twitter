from bottle import put, request, response
import x
import uuid

@put('/api-verify-email')
def _():
    try:
        #Get api key from form
        user_api_key = request.forms.get("welcome_user_api_key")
        if not user_api_key: raise Exception("Something went wrong")
        
        #Open database
        db = x.db()

        #Get user that matches api key
        user = db.execute("SELECT * FROM users WHERE user_api_key=? COLLATE NOCASE", (user_api_key,)).fetchone()

        #The api key does not exists, it is either wrong or has been changed/updated
        if not user: raise Exception("An error occurred")

        #Update account status to active
        db.execute(f"UPDATE users SET user_account_status=? WHERE user_api_key=?", (x.ACC_STATUS_ACTIVE, user_api_key,))

        #throw exception to test rollback

        #create new api key
        new_api_key = str(uuid.uuid4().hex)



        #commit
        db.commit()

        return {"info":"ok"}
    except Exception as ex:
        print(ex)
        #rollback
        try:
            response.status = ex.args[0]
            return {"info":ex.args[1]}
        except:
            response.status = 500
            return {"info":str(ex)}
    finally:
        if 'db' in locals(): db.close()