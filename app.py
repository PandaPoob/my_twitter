from bottle import default_app, get, post, template, response, request, route, run, static_file, view
import os
import sqlite3
import git
import pathlib
import x
import time
import calendar

################################################
#Git webhook to pythonanywhere
@post('/f1f83b1afe324291a552bf43b219b420')
def git_update():
  repo = git.Repo('./web_dev_mandatory_01')
  origin = repo.remotes.origin
  repo.create_head('main', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
  origin.pull()
  return ""
 
################################################
#STATIC FILES
@get("/app.css")
def _():
    return static_file("app.css", root=".")

@get("/js/<filename>")
def _(filename):
    return static_file(filename, "js")

@get("/images/<filename:re:.*\.jpg>")
def _(filename):
    return static_file(filename, root=os.getcwd()+"./images")

################################################

def dict_factory(cursor, row):
  col_names = [col[0] for col in cursor.description]
  return {key: value for key, value in zip(col_names, row)}

################################################
#Import functions
import formatNumber

################################################
# APIS
import apis.api_tweet

################################################
# BRIDGES

import bridges.login

################################################
# LOGIN PAGE
@get("/login")
def _():
    error = request.query.error.replace("_", " ")

    print(error)
    return template("login", username_min_length=x.USERNAME_MIN_LEN, username_max_length=x.USERNAME_MAX_LEN, password_min_length=x.PASSWORD_MIN_LEN, password_max_length=x.PASSWORD_MAX_LEN, username_error=x.usernameerror, password_error=x.passerror, error=error)

# HOME PAGE
@get("/")
def _():
    logged_user = request.get_cookie("user", secret="my-secret")
    response.add_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
    response.add_header("Pragma", "no-cache")
    response.add_header("Expires", 0)
    print(logged_user)
    try:
        db = sqlite3.connect(str(pathlib.Path(__file__).parent.resolve())+"/twitter.db")
        db.row_factory = dict_factory


        tweets = db.execute("SELECT * FROM users_and_tweets ORDER BY users_and_tweets.tweet_created_at DESC LIMIT 0, 10").fetchall()
        trends = trends = db.execute("SELECT * FROM trends").fetchall()
        if logged_user:
            username = logged_user["user_name"]
            fsugg = db.execute("SELECT * FROM follower_suggestions WHERE NOT user_name=?",(username,)).fetchall()
            
        else:
            fsugg = db.execute("SELECT * FROM follower_suggestions").fetchall()

           #format the tweet numbers
        for i in range(len(tweets)):
            if tweets[i]['tweet_total_replies']:
                tweets[i]['tweet_total_replies'] = formatNumber.human_format(tweets[i]['tweet_total_replies'])
        
            if tweets[i]['tweet_total_likes']:
                tweets[i]['tweet_total_likes'] = formatNumber.human_format(tweets[i]['tweet_total_likes'])
            
            if tweets[i]['tweet_total_retweets']:
                tweets[i]['tweet_total_retweets'] = formatNumber.human_format(tweets[i]['tweet_total_retweets'])
            
            if tweets[i]['tweet_total_views']:
                tweets[i]['tweet_total_views'] = formatNumber.human_format(tweets[i]['tweet_total_views'])
           
            if tweets[i]['tweet_created_at']:
                month = time.strftime('%#m', time.localtime(tweets[i]['tweet_created_at']))
                day = time.strftime('%#d', time.localtime(tweets[i]['tweet_created_at']))
                tweets[i]['tweet_created_at'] = f"{calendar.month_abbr[int(month)]} {day}"
                
           #format trends numbers
        for i in range(len(trends)):
            if trends[i]['trend_total_tweets']:
                #print(type(trends[i]['trend_total_tweets']))
                trends[i]['trend_total_tweets'] = formatNumber.human_format(trends[i]['trend_total_tweets'])
           
        return template("index", min_length=x.TWEET_MIN_LEN, max_length=x.TWEET_MAX_LEN, tweets=tweets, trends=trends, fsugg=fsugg, logged_user=logged_user)
    except:
        return "error"

    finally:
        if "db" in locals(): db.close()
################################################
# FORM PAGE
#import views.tweet

@get("/<username>")
def _(username):
    try:
        logged_user = request.get_cookie("user", secret="my-secret")
        response.add_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        response.add_header("Pragma", "no-cache")
        response.add_header("Expires", 0)
        print(logged_user)
        db = sqlite3.connect(str(pathlib.Path(__file__).parent.resolve())+"/twitter.db")
        #db = sqlite3.connect(os.getcwd()+"/twitter.db")
        #db = sqlite3.connect("/home/pandapoob/mysite/twitter.db")
        db.row_factory = dict_factory
        user = db.execute("SELECT * FROM users WHERE user_name=? COLLATE NOCASE", (username,)).fetchall()[0]
        
        user_id = user["user_id"]
        #print(f"user id: {user_id}")
        tweets = db.execute("SELECT * FROM users_and_tweets WHERE tweet_user_fk=? ORDER BY users_and_tweets.tweet_created_at DESC LIMIT 0, 10", (user_id,)).fetchall()
        
        #get trends
        trends = db.execute("SELECT * FROM trends").fetchall()

        #get follower suggestions
        if logged_user:
            username = logged_user["user_name"]
            fsugg = db.execute("SELECT * FROM follower_suggestions WHERE NOT user_name=?",(username,)).fetchall()
        else:
            fsugg = db.execute("SELECT * FROM follower_suggestions WHERE NOT user_name=?",(username,)).fetchall()
        

        #get img tweets
        imgtweets = db.execute("SELECT * FROM tweets WHERE tweet_field_img <> '' AND tweet_user_fk=? ORDER BY tweets.tweet_created_at DESC LIMIT 0, 6", (user_id,)).fetchall()
     

       #format user numbers
        if user['user_total_followers']:
            user["user_total_followers"] = formatNumber.human_format(user['user_total_followers'])
        
        if user['user_total_following']:
            user["user_total_following"] = formatNumber.human_format(user['user_total_following'])
       
        if user['user_total_tweets']:
            user["user_total_tweets"] = formatNumber.human_format(user['user_total_tweets'])
        

        #format the tweet numbers
        if len(tweets) != 0:
            for i in range(len(tweets)):
                if tweets[i]['tweet_total_replies']:
                    tweets[i]['tweet_total_replies'] = formatNumber.human_format(tweets[i]['tweet_total_replies'])
                
                if tweets[i]['tweet_total_likes']:
                    tweets[i]['tweet_total_likes'] = formatNumber.human_format(tweets[i]['tweet_total_likes'])
                
                if tweets[i]['tweet_total_retweets']:
                    tweets[i]['tweet_total_retweets'] = formatNumber.human_format(tweets[i]['tweet_total_retweets'])
                
                if tweets[i]['tweet_total_views']:
                    tweets[i]['tweet_total_views'] = formatNumber.human_format(tweets[i]['tweet_total_views'])

                if tweets[i]['tweet_created_at']:
                    month = time.strftime('%#m', time.localtime(tweets[i]['tweet_created_at']))
                    day = time.strftime('%#d', time.localtime(tweets[i]['tweet_created_at']))
                    tweets[i]['tweet_created_at'] = f"{calendar.month_abbr[int(month)]} {day}"
                
        
        #format trends numbers
        for i in range(len(trends)):
            if trends[i]['trend_total_tweets']:
                #print(type(trends[i]['trend_total_tweets']))
                trends[i]['trend_total_tweets'] = formatNumber.human_format(trends[i]['trend_total_tweets'])

        #format date on user
        if user['user_bio_created_at']:
            year = time.strftime('%Y', time.localtime(user["user_bio_created_at"]))
            month = time.strftime('%#m', time.localtime(user["user_bio_created_at"]))
            user["user_bio_created_at"] = f"Joined {calendar.month_name[int(month)]} {year}"

        #format date on tweet
        

        return template("profile", user=user, tweets=tweets, trends=trends, fsugg=fsugg, imgtweets=imgtweets, logged_user=logged_user)
    except Exception as ex:
        print(ex)
        return "error"

    finally:
        if "db" in locals(): db.close()


#try will run on amazon
try:
    import production
    #x.DB_PATH = "/home/pandapoob/mysite/"
    application = default_app()

#except will run local
except Exception as ex:
    print("Server running locally")
    run(host="127.0.0.1", port=3000, reloader=True, debug=True)
#run(host="127.0.0.1", port=3000, reloader=True, debug=True)
