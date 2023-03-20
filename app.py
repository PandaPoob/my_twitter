from bottle import default_app, get, post, response, run, static_file
import os
import git
import x

################################################
#https://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@github.com/PandaPoob/web_dev_mandatory_01.git
#Git webhook to pythonanywhere
@post('/f1f83b1afe324291a552bf43b219b420')
def git_update():
  repo = git.Repo('./web_dev_mandatory_01')
  origin = repo.remotes.origin
  repo.create_head('main', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
  origin.pull()
  return ""
 
#STATIC FILES
@get("/app.css")
def _():
    return static_file("app.css", root=".")

@get("/js/<filename>")
def _(filename):
    return static_file(filename, "js")

@get("/images/avatar_imgs/<filename>")
def _(filename):
    return static_file(filename, root=os.getcwd()+"./images/avatar_imgs/")

@get("/images/cover_imgs/<filename>")
def _(filename):
    return static_file(filename, root=os.getcwd()+"./images/cover_imgs/")

@get("/images/tweet_imgs/<filename>")
def _(filename):
    return static_file(filename, root=os.getcwd()+"./images/tweet_imgs/")

################################################
#APIS
import apis.api_tweet
import apis.api_login
import apis.api_signup
import apis.api_follow
#import apis.api_send_sms

################################################
#BRIDGES
#import bridges.login
@get("/logout")
def _():
  x.disable_cache()

  response.delete_cookie("user")
  response.status = 303
  response.set_header("Location", "/login")
  return

#PAGES
import views.index
import views.profile
import views.login
import views.signup
import views.test_follow
#import views.test_sms

################################################

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
