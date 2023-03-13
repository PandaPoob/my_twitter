from bottle import default_app, get, post, template, response, request, run, static_file
import os
import git
import x

################################################
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

@get("/images/<filename>")
def _(filename):
    return static_file(filename, root=os.getcwd()+"./images")


################################################
#Import functions
import formatNumber

################################################
#APIS
import apis.api_tweet
import apis.api_signup

################################################
#BRIDGES
import bridges.login
import bridges.logout

#PAGES
import views.index
import views.profile

#LOGIN PAGE
@get("/login")
def _():
    logged_user = request.get_cookie("user", secret="my-secret")
    if logged_user:
        response.status = 303
        response.set_header("Location", "/")

    error = request.query.error.replace("_", " ")
    print(error)
    return template("login", username_min_length=x.USERNAME_MIN_LEN, username_max_length=x.USERNAME_MAX_LEN, password_min_length=x.PASSWORD_MIN_LEN, password_max_length=x.PASSWORD_MAX_LEN, username_error=x.usernameerror, password_error=x.passerror, error=error)



################################################
# FORM PAGE
#import views.tweet




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
