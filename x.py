from bottle import request
import pathlib
import sqlite3


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
TWEET_MIN_LEN = 2
TWEET_MAX_LEN = 8

def validate_tweet():
    error = f"tweet_field_text min {TWEET_MIN_LEN} max {TWEET_MAX_LEN} characters"
    if len(request.forms.tweet_field_text) < TWEET_MIN_LEN: raise Exception(error)
    if len(request.forms.tweet_field_text) > TWEET_MAX_LEN: raise Exception(error)
    return request.forms.get("tweet_field_text")
