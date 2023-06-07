from bottle import default_app, get, post, request, response, run, static_file, template
import os
import git
import x

################################################
#https://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@github.com/PandaPoob/web_dev_mandatory_01.git
#Git webhook to pythonanywhere
#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
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

@get("/images/placeholders/<filename>")
def _(filename):
    return static_file(filename, root=os.getcwd()+"./images/placeholders/")

################################################
#APIS
import apis.api_tweet
import apis.api_login
import apis.api_signup
import apis.api_verify_email
import apis.api_forgot_password
import apis.api_reset_password
import apis.api_edit_profile
import apis.api_search
import apis.api_follow
import apis.api_unfollow
import apis.api_pagination_tweets


#import delete_later.api_send_sms

################################################
#BRIDGES

@get("/logout")
def _():
  x.disable_cache()
  result = x.getDomain()
  response.delete_cookie("user", path='/', domain=result[1])
  response.status = 303
  response.set_header("Location", "/login")
  return

#PAGES
import views.index
import views.profile
import views.login
import views.signup
import views.verify_user
import views.tweet
import views.forgot_password
import views.reset_password
import views.search
import views.explore
import views.settings
#import delete_later.test_sms

################################################

#Runs on PythonAnywhere
try:
    import production
    application = default_app()

#Runs locally
except Exception as ex:
    print("Server running locally")
    run(host="127.0.0.1", port=3000, reloader=True, debug=True)