from bottle import get, template, response
import x
import utils.validateResetToken as v

@get("/reset-password/<token>")
def _(token):
    x.disable_cache()
   
    try:
        #Validate token
        user_api_key = v.validate_reset_token(token)
        
        #Open database
        db = x.db()
        
        #Get user api key
        user_id = db.execute("SELECT user_id FROM users WHERE user_api_key=? COLLATE NOCASE", (user_api_key,)).fetchone()

        #If there is no matching api key
        if not user_id: raise Exception(401, "An error occurred")
        
        password_val = {
            "min": x.PASSWORD_MIN_LEN,
            "max": x.PASSWORD_MAX_LEN,   
        }

        return template("reset_password", token=token, password_val=password_val)

    except Exception as ex:
        print(ex)
        try:
            response.status = ex.args[0]
            #error_msg = {"info":ex.args[1]}
            return f'<body style="background-color: black; color: white">{ex.args[1]}</body>'
        except:
            response.status = 500
            return {"info":str(ex)}
        
    finally:
        if "db" in locals(): db.close()
    
    