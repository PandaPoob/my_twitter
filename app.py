from bottle import default_app, get, post, request, response, run, static_file
import os
import git
import x
import uuid
import mimetypes
import magic
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
import apis.api_unfollow
import apis.api_verify_email
import apis.api_search

#import delete_later.api_send_sms

@post("/upload-picture")
def _():
    try:
        form_picture = request.files.get("picture")
        name, ext = os.path.splitext(form_picture.filename)
        #print("#"*30)
        #print(name, ext)
        if ext not in ('.png','.jpg','.jpeg'):
            raise Exception(400, "File extension not allowed")
    
        picture_name = str(uuid.uuid4()).replace("-","")
        picture_name = picture_name + ext
        form_picture.save(f"pictures/{picture_name}")
        filetype = magic.from_file(f"pictures/{picture_name}")

        print(filetype)
        #JPEG image data
        #PNG image data
        if "PNG image data" not in filetype and "JPEG image data" not in filetype:
            url = os.getcwd()+f"/pictures/{picture_name}"
            os.remove(url, dir_fd = None)
            raise Exception(400, "File extension not allowed")

        return {"info": "picture uploaded"}
    except Exception as ex:
        print(ex)
        response.status = ex.args[0]
        return {"info":ex.args[1]}
    finally:
        pass
 
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
import views.verify_user
import views.tweet
#import delete_later.test_sms

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
