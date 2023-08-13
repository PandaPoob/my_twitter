import time
import calendar
import utils.formatNumber as fn

def get_pretty_tweet(tweets):
    
    #Format images
    for tweet in tweets:
        if tweet["tweet_field_images"] != 0:
            tweet_images = tweet['tweet_images'].split(',')
            image_orders = tweet['image_orders'].split(',')

            #Create array
            image_objects = [{'url': url, 'order': order} for url, order in zip(tweet_images, image_orders)]

            #Update property with formatted array of objects
            tweet['tweet_images'] = image_objects
            del tweet['image_orders']
    
    #Format numbers
    for i in range(len(tweets)):
        if tweets[i]['tweet_total_replies']:
            tweets[i]['tweet_total_replies'] = fn.human_format(tweets[i]['tweet_total_replies'])
        
        if tweets[i]['tweet_total_likes']:
            tweets[i]['tweet_total_likes'] = fn.human_format(tweets[i]['tweet_total_likes'])
            
        if tweets[i]['tweet_total_retweets']:
            tweets[i]['tweet_total_retweets'] = fn.human_format(tweets[i]['tweet_total_retweets'])
        
        #Format created at
        if tweets[i]['tweet_created_at']:
            month = time.strftime('%#m', time.localtime(tweets[i]['tweet_created_at']))
            day = time.strftime('%#d', time.localtime(tweets[i]['tweet_created_at']))
            tweets[i]['tweet_created_at'] = f"{calendar.month_abbr[int(month)]} {day}"
    
    return tweets