import jwt
import datetime
import x

def generate_reset_token(user_api_key):
    expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=x.RESET_TOKEN_TIME)
    payload = {
        "user_api_key": user_api_key,
        "exp": expiration
    }
    
    token = jwt.encode(payload, x.TOKEN_SECRET, algorithm="HS256")
 
    return token