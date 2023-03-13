from bottle import request, response
import pathlib
import sqlite3
import re


def disable_cache():
    response.add_header("Cache-Control", "no-cache, no-store, must-revalidate, max-age=0")
    response.add_header("Pragma", "no-cache")
    response.add_header("Expires", 0)


def dict_factory(cursor, row):
  col_names = [col[0] for col in cursor.description]
  return {key: value for key, value in zip(col_names, row)}


def db():
  try:
    db = sqlite3.connect(str(pathlib.Path(__file__).parent.resolve())+"/twitter.db") 
    db.row_factory = dict_factory
    return db
  except Exception as ex:
    print(ex)
  finally:
    pass

####################################
#tweet validation
TWEET_MIN_LEN = 1
TWEET_MAX_LEN = 8

def validate_tweet():
    error = f"tweet_field_text min {TWEET_MIN_LEN} max {TWEET_MAX_LEN} characters"
    if len(request.forms.tweet_field_text) < TWEET_MIN_LEN: raise Exception(error)
    if len(request.forms.tweet_field_text) > TWEET_MAX_LEN: raise Exception(error)
    return request.forms.get("tweet_field_text")

#user validation
USERNAME_MIN_LEN = 4
USERNAME_MAX_LEN = 20
USERNAME_REGEX = "^[a-zA-Z0-9_]*$"

usernameerror = f"Username must be between {USERNAME_MIN_LEN} and {USERNAME_MAX_LEN} characters"
usernamematcherror = f"Invalid username"

PASSWORD_MIN_LEN = 8
PASSWORD_MAX_LEN = 20

passerror = f"Password must be between {USERNAME_MIN_LEN} and {USERNAME_MAX_LEN} characters"

###TODO isolate validation validate_username, _password

def validate_login():
    if len(request.forms.login_user_name) < USERNAME_MIN_LEN: raise Exception(usernameerror)
    if len(request.forms.login_user_name) > USERNAME_MAX_LEN: raise Exception(usernameerror)

    
    if request.forms.login_user_name == "": raise Exception(usernameerror)
    if len(request.forms.login_password) < PASSWORD_MIN_LEN: raise Exception(passerror)
    if len(request.forms.login_password) > PASSWORD_MAX_LEN: raise Exception(passerror)
    return request.forms.get("login_user_name"), request.forms.get("request.forms.login_password")
    
def validate_signup():
    #remove space before
    print(30*"#")

    request.forms.signup_user_name = request.forms.signup_user_name.strip()
    if len(request.forms.signup_user_name) < USERNAME_MIN_LEN: raise Exception(usernameerror)
    if len(request.forms.signup_user_name) > USERNAME_MAX_LEN: raise Exception(usernameerror)
    if not re.match(USERNAME_REGEX, request.forms.signup_user_name): raise Exception(usernamematcherror)
    #usernamematcherror
    return request.forms.signup_user_name