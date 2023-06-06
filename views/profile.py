from bottle import get, template, request
import time
import calendar
import x
import utils.formatNumber

@get("/<username>")
def _(username):
    try:
        x.disable_cache()
        
        #Get cookie if exists
        logged_user = x.request_cookie()

        #Open database
        db = x.db()
        
        #Fetch profile
        profile = db.execute("SELECT * FROM users WHERE user_name=? COLLATE NOCASE", (username,)).fetchall()[0]
        
        #Profile id
        profile_id = profile["user_id"]

        #Fetch tweets
        tweets = db.execute("SELECT * FROM users_and_tweets WHERE tweet_user_fk=? ORDER BY users_and_tweets.tweet_created_at DESC LIMIT 0, 10", (profile_id,)).fetchall()
        
        #Fetch images of tweets 
        # @todo perhaps make this general 
        for i in range(len(tweets)):
            tweet_images = db.execute("SELECT * FROM tweet_images WHERE tweet_images.tweet_image_tweet_fk=? ORDER BY tweet_images.tweet_image_order ASC", (tweets[i]["tweet_id"],)).fetchall()
            
            #Declare new key and add image list
            tweets[i]['tweet_images'] = tweet_images

        #Fetch trends
        trends = db.execute("SELECT * FROM trends").fetchall()
        
        #If cookie exists then decode
        if logged_user:
            logged_user = x.decode_cookie(logged_user)
            logged_username = logged_user["user_name"]
            user_id = logged_user["user_id"]

            #Get users that are not the logged in user, the profile and are not already followed
            fsugg = db.execute("""
                SELECT * FROM follower_suggestions
                WHERE user_name NOT IN  (?, ?) 
                AND user_id NOT IN (
                SELECT followee_fk
                FROM following
                WHERE follower_fk = ?
                )""", (logged_username, username, user_id)).fetchall()
        else:
            #if not logged then fetch all where the user is not in
            fsugg = db.execute("SELECT * FROM follower_suggestions WHERE NOT user_name=?",(username,)).fetchall()
        
        #Get 6 latest image tweets
        imgtweets = db.execute("SELECT tweet_image_url, tweet_id FROM tweet_images JOIN tweets ON tweet_image_tweet_fk=tweet_id JOIN users ON user_id=tweet_user_fk WHERE user_id=? ORDER BY tweet_created_at DESC, tweet_image_order ASC LIMIT 0, 6", (profile_id,)).fetchall()
        
        #Format profile numbers
        if profile['user_total_followers']:
            profile["user_total_followers"] = utils.formatNumber.human_format(profile['user_total_followers'])
        
        if profile['user_total_following']:
            profile["user_total_following"] = utils.formatNumber.human_format(profile['user_total_following'])
       
        if profile['user_total_tweets']:
            profile["user_total_tweets"] = utils.formatNumber.human_format(profile['user_total_tweets'])
        
        #Format the tweet numbers
        #@todo maybe make this general func
        if len(tweets) != 0:
            for i in range(len(tweets)):
                if tweets[i]['tweet_total_replies']:
                    tweets[i]['tweet_total_replies'] = utils.formatNumber.human_format(tweets[i]['tweet_total_replies'])
                
                if tweets[i]['tweet_total_likes']:
                    tweets[i]['tweet_total_likes'] = utils.formatNumber.human_format(tweets[i]['tweet_total_likes'])
                
                if tweets[i]['tweet_total_retweets']:
                    tweets[i]['tweet_total_retweets'] = utils.formatNumber.human_format(tweets[i]['tweet_total_retweets'])
                
                if tweets[i]['tweet_total_views']:
                    tweets[i]['tweet_total_views'] = utils.formatNumber.human_format(tweets[i]['tweet_total_views'])

                if tweets[i]['tweet_created_at']:
                    month = time.strftime('%#m', time.localtime(tweets[i]['tweet_created_at']))
                    day = time.strftime('%#d', time.localtime(tweets[i]['tweet_created_at']))
                    tweets[i]['tweet_created_at'] = f"{calendar.month_abbr[int(month)]} {day}"
                
        
        #Format trends numbers
        for i in range(len(trends)):
            if trends[i]['trend_total_tweets']:
                trends[i]['trend_total_tweets'] = utils.formatNumber.human_format(trends[i]['trend_total_tweets'])

        #Format date
        if profile['user_created_at']:
            year = time.strftime('%Y', time.localtime(profile["user_created_at"]))
            month = time.strftime('%#m', time.localtime(profile["user_created_at"]))
            profile["user_created_at"] = f"Joined {calendar.month_name[int(month)]} {year}"

        #Boolean for whether logged_user follows profile
        isFollowing = False
        if logged_user:
            following = db.execute("SELECT * FROM following WHERE follower_fk=?", (logged_user["user_id"],)).fetchall()
          
            for f in range(len(following)):   
                if following[f]['followee_fk'] == profile_id:
                    isFollowing = True

        #Validation variables
        validation_vars = {
            "fullname": {
                "min": x.USER_FULL_NAME_MIN,
                "max": x.USER_FULL_NAME_MAX
            },
            "bio": {
                "max": x.USER_BIO_TEXT_MAX
            },
            "location": {
                "max": x.USER_BIO_LOC_MAX
            },
             "link": {
                "max": x.USER_BIO_LINK_MAX
            },
            "img": {
                "max": x.USER_IMG_MAX_SIZE
            }
        }

        return template("profile", profile=profile, tweets=tweets, trends=trends, fsugg=fsugg, imgtweets=imgtweets, logged_user=logged_user, isFollowing=isFollowing, validation_vars=validation_vars)
    except Exception as ex:
        print(ex)
        return "error"

    finally:
        if "db" in locals(): db.close()

