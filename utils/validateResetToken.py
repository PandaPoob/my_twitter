import jwt
import datetime
import x

def validate_reset_token(token):
    try:
        #Decode token
        payload = jwt.decode(token, x.TOKEN_SECRET, algorithms=["HS256"])

        #Get api key
        user_api_key = payload['user_api_key']

        #Get expiration date
        expiration = datetime.datetime.fromtimestamp(payload['exp'])

        #Check if token is expired, 401 Unauthorized
        if datetime.datetime.utcnow() > expiration: raise Exception(401, "This session has expired")

        return user_api_key
    #If token is expired or not valid throw ex
    except jwt.ExpiredSignatureError:
        raise Exception(401, "This session has expired")

    except (jwt.DecodeError, jwt.InvalidTokenError) as ex:
        print(ex)
        raise Exception(400, "Token not valid")
    

