from bottle import default_app, get, post, template, route, run, static_file, view
import os
import sqlite3
import git

@post('/f1f83b1afe324291a552bf43b219b420')
def git_update():
  repo = git.Repo('./web_dev_mandatory_01')
  origin = repo.remotes.origin
  repo.create_head('main', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
  origin.pull()
  return ""
 

@get("/app.css")
def _():
    return static_file("app.css", root=".")

@get("/images/<filename:re:.*\.jpg>")
def _(filename):
    return static_file(filename, root=os.getcwd()+"./images")

#####

def dict_factory(cursor, row):
  col_names = [col[0] for col in cursor.description]
  return {key: value for key, value in zip(col_names, row)}

#####
@get("/")
def _():
    return "Home page Github"
        

@get("/<username>")
#@view("profile")
def _(username):
    try:
        db = sqlite3.connect(os.getcwd()+"/twitter.db")
        #db = sqlite3.connect("/home/pandapoob/mysite/twitter.db")
        db.row_factory = dict_factory
        user = db.execute("SELECT * FROM users WHERE user_name=? COLLATE NOCASE", (username,)).fetchall()[0]
        #print(user)
        #get users id
        user_id = user["user_id"]
        #print(f"user id: {user_id}")
        tweets = db.execute("SELECT * FROM tweets WHERE tweet_user_fk=? ORDER BY tweets.tweet_created_at DESC LIMIT 0, 10", (user_id,)).fetchall()
    
        #get trends
        trends = db.execute("SELECT * FROM trends").fetchall()

        #get follower suggestions
        fsugg = db.execute("SELECT * FROM follower_suggestions WHERE NOT user_name=?",(username,)).fetchall()
        print("#"*30)
        print(fsugg)
        
        return template("profile", user=user, tweets=tweets, trends=trends, fsugg=fsugg)
    #except Exception as ex:
        #print(ex)
    except:
        return "error"

    finally:
        if "db" in locals(): db.close()

#####


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
