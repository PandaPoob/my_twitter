from bottle import post, request, response
import requests
import x
import secrets
import string

@post("/api-sms-gateway")
def _():
    try:
        #logged_user = x.request_cookie()

        #if not logged_user:
         #   raise Exception(400, "Log in to verify")
        
        #Decode cookie
        #logged_user = x.decode_cookie(logged_user)
        
        #user_id = logged_user["user_id"]
        user_id = "b3094c2f1c144817b7cc0b718fc3c644"

        #Open database
        db = x.db()

        #Get the user
        user = db.execute("SELECT * FROM active_users WHERE user_id=?", (user_id,)).fetchone()
        if not user:
           raise Exception(400, "Could not find user")

        #Get phone number and validate
        user_phonenumber = x.validate_phone_number()

        #Check if number is already in use
        user = db.execute("SELECT * FROM active_users WHERE user_phonenumber=?", (user_phonenumber,)).fetchone()
        if user:
            raise Exception("Phone number is already in use")

        #Url to send sms
        url = 'https://fiotext.com/send-sms'

        #Generate a secure random code with the specified length
        characters = string.digits
        code = ''.join(secrets.choice(characters) for _ in range(6))
        
        msg =f"""Your verification code is: {code}.

Thank you,
Freja's Twitter
        """

        #Set the user api key with code
        db.execute(f"UPDATE users SET user_api_key=? WHERE user_id=?", (code, user_id))

        
        #Data it expects
        payload = {"user_api_key": x.KEY, "sms_message": msg, "sms_to_phone": user_phonenumber}
        r = requests.post(url, data=payload)
        if r.status_code != 200:
            raise Exception(400, str(r.text))
     
        db.commit()
       
        return {"info": "Sms sent", "user_phonenumber": user_phonenumber}
    except Exception as ex:
        try:
            response.status = ex.args[0]
            return {"info":ex.args[1]}
        except:
            response.status = 500
            return {"info":str(ex)}
    finally:
        if "db" in locals(): db.close()