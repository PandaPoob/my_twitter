from bottle import get, run, template, static_file, response, request
import sqlite3
#this data will come from the database
#for now data is hardcoded
#json object but called dictionary in Python
# 0 = false, 1 = true
# if "message_image" in tweet:
tweets = [
    {
    "image_name": "cleo.jpg",
    "fullname": "Cleo",
    "username": "Cleodoggo",
    "message": "I love my new profile picture",
    "message_image": "cleo.jpg",
    "total_comments": "1",
    "total_retweets": "2",
    "total_likes": "3",
    "total_dislikes": "4",
    "verified": 0,
    },
        {
    "image_name": "1.jpg",
    "fullname": "Elon Musk",
    "username": "elonmusk",
    "message": "My first tweet",
    "message_image": "1.png",
    "total_comments": "1",
    "total_retweets": "2",
    "total_likes": "3",
    "total_dislikes": "4",
     "verified": 1,
    },
        {
  "image_name": "3.jpg",
    "fullname": "Shakira",
    "username": "shakira",
    "message": "My first tweet",
    "message_image": "3.jpg",
    "total_comments": "1",
    "total_retweets": "2",
    "total_likes": "3",
    "total_dislikes": "4",
     "verified": 1,
    },
        {
    "image_name": "2.jpg",
    "fullname": "Joe Biden",
    "username": "joebiden",
    "message": " Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.",
    "message_image": "5.jpg",
    "total_comments": "1",
    "total_retweets": "2",
    "total_likes": "3",
    "total_dislikes": "4",
     "verified": 1,
    },
        {
   "image_name": "3.jpg",
    "fullname": "Shakira",
    "username": "shakira",
    "message": "My first tweet",
    "message_image": "4.jpeg",
    "total_comments": "1",
    "total_retweets": "2",
    "total_likes": "3",
    "total_dislikes": "4",
     "verified": 1,
    },
        {
    "image_name": "1.jpg",
    "fullname": "Freja Smith",
    "username": "frejasmith",
    "message": "My first tweet",
    
    "total_comments": "1",
    "total_retweets": "2",
    "total_likes": "3",
    "total_dislikes": "4",
     "verified": 0,
    },
]

trends = [
    {
    "title": "One",
    "total_hash":1,
    },
      {
    "title": "Two",
    "total_hash":2,
    },
      {
    "title": "Three",
    "total_hash":3,
    },
      {
    "title": "Four",
    "total_hash":4,
    },
   {
    "title": "Five",
    "total_hash":5,
    },
       {
    "title": "Six",
    "total_hash":6,
    },
     {
    "title": "Seven",
    "total_hash":7,
    },
]

suggested_follows = [
     {
        "image_name": "cleo.jpg",
        "fullname": "Cleo",
        "username": "Cleodoggo",
    },
    {
        "image_name": "1.jpg",
        "fullname": "Elon Musk",
        "username": "elonmusk"
    },
    {
        "image_name": "2.jpg",
        "fullname": "Joe Biden",
        "username": "joebiden",
    },
    {
        "image_name": "3.jpg",
        "fullname": "Shakira",
        "username": "shakira",
    },
    {
        "image_name": "2.jpg",
        "fullname": "Joe Biden",
        "username": "joebiden",
    },
]

###########################
#get thumbnails
#if a file ends with jpg then get from thumbnails
@get("/thumbnails/<filename:re:.*\.jpg>")
def _(filename):
    return static_file(filename, root="./thumbnails")
###########################

#get thumbnails
#if a file ends with png then get from thumbnails
@get("/thumbnails/<filename:re:.*\.png>")
def _(filename):
    return static_file(filename, root="./thumbnails")
###########################

#get images
#jpg
@get("/images/<filename:re:.*\.jpg>")
def _(filename):
    return static_file(filename, root="./images")

#png
@get("/images/<filename:re:.*\.png>")
def _(filename):
    return static_file(filename, root="./images")

#jpeg
@get("/images/<filename:re:.*\.jpeg>")
def _(filename):
    return static_file(filename, root="./images")
###########################
#get css file
#if browser is pointing to app.css then get app.css and the position which rn is the root
@get("/app.css")
def _():
    return static_file("app.css", root=".")

###########################

@get("/")
#make function to render page with : 
def render_index():
    return template("index", title="Twitter", tweets=tweets, trends=trends, suggested_follows=suggested_follows)

@get("/about")
def _():
    return template("about-us")

@get("/contact")
def _():
    return template("contact-us")

@get("/explore")
def _():
    return template("explore")

###########################
#APIS do not return HTML, there are exceptions
#APIS return most likely JSON
#Rule 1 - Test API (thunder client or postman)
@get("/api-get-name")
def _():
    try: #best case scenario
        id = request.query.get("id")
        name = request.query.get("name")
        last_name = request.query.get("last_name")

        if id != "1": raise Exception("The id is wrong")
        if name != "a": raise Exception("The name is wrong")
        if last_name != "b": raise Exception("The last name is wrong")
    #connect to the database
        db = sqlite3.connect("twitter.db")
        users = db.execute("SELECT * FROM users").fetchall() #function to get ALL users fetchall returns the list
        print("users", users)
    #get name from database

    #send the name to the client(response)
        return {"id":id, "name": name, "last_name": last_name} 
    except Exception as ex: #something went wrong |ex is variable that contains error
    #send a 400 to the client
        print(ex)
        response.status = 400
        return {"error": str(ex)}
    finally: #it must be done/will always happen
    #close the database (no matter if it fails or not)
        if "db" in locals(): db.close()
        print("The end")


###########################
# syn. localhost # ports are between 0-65535
run(host="127.0.0.1", port=3000, reloader=True, debug=True) 
#install new server: pip list, pip install paste
##run(host="127.0.0.1", port=3000, reloader=True, debug=True, server="paste") 
###python app.py