from bottle import request, response
import pathlib
import sqlite3
import re
import datetime
import calendar
import jwt
import os

#COOKIE VARIABLE#
COOKIE_SECRET = "872437049d2a426f9d86f1ea58b4c901"

#USER ACCOUNT STATUS VARIABLES#
ACC_STATUS_ACTIVE = "active"
ACC_STATUS_INACTIVE = "inactive"

#TWEET TYPE VARIABLES#
TWEET_TYPE_DEFAULT = "default"
TWEET_TYPE_COMMENT = "comment"
TWEET_TYPE_RETWEET = "retweet"
TWEET_TYPE_QUOTE = "quote"


#GENERAL FUNCTIONS#
def disable_cache():
    response.add_header("Cache-Control", "no-cache, no-store, must-revalidate, max-age=0")
    response.add_header("Pragma", "no-cache")
    response.add_header("Expires", 0)

def request_cookie():
    logged_user = request.get_cookie("user")
    return logged_user

def decode_cookie(logged_user):
    logged_user = jwt.decode(logged_user, COOKIE_SECRET, algorithms=["HS256"])
    return logged_user

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

def prepare_values(vals):
    values = ""
    for key in vals:
        values += f":{key},"
    values = values.rstrip(",")
    return values

#2mb for profile image and cover
#VALIDATION FUNCTIONS#

#Tweet field text#
#@todo change max len to 280
TWEET_MAX_LEN = 6
TWEET_MAX_IMG_SIZE = 5000000 #5MB
TWEET_MAX_IMG_NO = 4

def validate_tweet_field_text():
    error = f"tweet_field_text max {TWEET_MAX_LEN} characters"
    if len(request.forms.tweet_field_text) > TWEET_MAX_LEN: raise Exception(400, error)
    return request.forms.get("tweet_field_text")

def validate_image_size(filesize):
    error = f"Max size per image is 5mb"
    if filesize > TWEET_MAX_IMG_SIZE: raise Exception(400, error)
    return

def validate_image_type(tweet_image):
    error = f"tweet_field_image only accepts file ext JPG, JPEG, PNG"
    name, ext = os.path.splitext(tweet_image.filename)
    if ext not in ('.png','.jpg','.jpeg'): raise Exception(400, error)
    return

def validate_image_datatype(filetype):
    error = f"tweet_field_image only accepts datatype JPG, JPEG, PNG"
    if "PNG image data" not in filetype and "JPEG image data" not in filetype:
            raise Exception(400, error)
    return



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
 
  if date_birthday > USER_BIRTHDAY_MAX : raise Exception(400, userbirthdayerror)
  if age < 13 : raise Exception(400,  userbirthdayminerror)
  user_birthday = f"{calendar.month_name[int(user_birthday[1])]} {user_birthday[2]}, {user_birthday[0]}"
  
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

  return user_name

########################################################################

PASSWORD_MIN_LEN = 8
PASSWORD_MAX_LEN = 50

passerror = f"Password must be between {PASSWORD_MIN_LEN} and {PASSWORD_MAX_LEN} characters"

def validate_password():
    user_password = request.forms.get("user_password", "")
    user_password = user_password.strip()
    if len(user_password) < PASSWORD_MIN_LEN: raise Exception(400, passerror)
    if len(user_password) > PASSWORD_MAX_LEN: raise Exception(400, passerror)

    return user_password


def validate_user_confirm_password():
	error = f"user_password and user_confirm_password do not match"
	user_password = request.forms.get("user_password", "")
	confirm_password = request.forms.get("confirm_password", "")
	user_password = user_password.strip()
	confirm_password = confirm_password.strip()
	if confirm_password != user_password: raise Exception(400, error)
	return confirm_password