from bottle import request, response
import pathlib
import sqlite3
import re
import datetime

COOKIE_SECRET = "872437049d2a426f9d86f1ea58b4c901"

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
    #db = sqlite3.connect(os.getcwd()+"/twitter.db")
    #db = sqlite3.connect("/home/pandapoob/mysite/twitter.db")
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

########################################################################
USER_FULL_NAME_MIN = 2
USER_FULL_NAME_MAX = 40

fullnameerror = f"Name must be between {USER_FULL_NAME_MIN} and {USER_FULL_NAME_MAX} characters"

def validate_fullname():
  user_full_name = request.forms.get("user_full_name", "")
  user_full_name = user_full_name.strip()
  if len(user_full_name) < USER_FULL_NAME_MIN: raise Exception(fullnameerror)
  if len(user_full_name) > USER_FULL_NAME_MAX: raise Exception(fullnameerror)

  return user_full_name

########################################################################

USER_EMAIL_MIN = 6
USER_EMAIL_MAX = 100
USER_EMAIL_REGEX = "^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$"

useremailerror = f"user_email invalid"

def validate_user_email():
	user_email = request.forms.get("user_email", "")        
	user_email = user_email.strip()
	if len(user_email) < USER_EMAIL_MIN : raise Exception(400, useremailerror)
	if len(user_email) > USER_EMAIL_MAX : raise Exception(400, useremailerror)  
	if not re.match(USER_EMAIL_REGEX, user_email): raise Exception(400, useremailerror)
	return user_email

########################################################################
def calculate_age(born):
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

USER_BIRTHDAY_MAX = datetime.date.today()
userbirthdayerror = "userbirthday invalid"
userbirthdayminerror = "User must be 13 years or older to sign up"

def validate_user_birthday():
  user_birthday = request.forms.get("user_birthday", "")        
  user_birthday = user_birthday.strip()
  user_birthday = user_birthday.split("-")
  date_birthday = datetime.date(int(user_birthday[0]), int(user_birthday[1]), int(user_birthday[2]))
  age = calculate_age(datetime.date(int(user_birthday[0]), int(user_birthday[1]), int(user_birthday[2])))
  print(age)
  if date_birthday > USER_BIRTHDAY_MAX : raise Exception(400, userbirthdayerror)
  if age < 13 : raise Exception(400,  userbirthdayminerror)
  return user_birthday
########################################################################

USERNAME_MIN_LEN = 4
USERNAME_MAX_LEN = 20
USERNAME_REGEX = "^[a-zA-Z0-9_]*$"

usernameerror = f"Username must be between {USERNAME_MIN_LEN} and {USERNAME_MAX_LEN} characters"
usernamematcherror = f"Invalid username"
   
def validate_username():
  user_name = request.forms.get("user_name", "")
  user_name = user_name.strip()
  if len(user_name) < USERNAME_MIN_LEN: raise Exception(usernameerror)
  if len(user_name) > USERNAME_MAX_LEN: raise Exception(usernameerror)
  if not re.match(USERNAME_REGEX, user_name): raise Exception(usernamematcherror)

  return request.forms.get("user_name")

########################################################################

PASSWORD_MIN_LEN = 8
PASSWORD_MAX_LEN = 50

passerror = f"Password must be between {PASSWORD_MIN_LEN} and {PASSWORD_MAX_LEN} characters"

def validate_password():
    user_password = request.forms.get("user_password", "")
    user_password = user_password.strip()
    if len(user_password) < PASSWORD_MIN_LEN: raise Exception(passerror)
    if len(user_password) > PASSWORD_MAX_LEN: raise Exception(passerror)

    return request.forms.get("user_password")


def validate_user_confirm_password():
	error = f"user_password and user_confirm_password do not match"
	user_password = request.forms.get("user_password", "")
	user_confirm_password = request.forms.get("user_confirm_password", "")
	user_password = user_password.strip()
	user_confirm_password = user_confirm_password.strip()
	if user_confirm_password != user_password: raise Exception(400, error)
	return user_confirm_password