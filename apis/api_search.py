from bottle import post, response, request
import x

@post('/api-search')
def _():
    try:
        
        #Search query 
        search_query = request.forms.get("search_query")

        #Validation
        if search_query == "empty": raise Exception(400, "Must provide a query")

        #Open database
        db = x.db()
        
        #Get top 3 people that matches either with user_name or full name
        search_result = db.execute("SELECT user_name, user_twitter_status, user_full_name, user_img_avatar FROM active_users WHERE user_name LIKE '%' || ? || '%' OR user_full_name LIKE '%' || ? || '%' ORDER BY user_name LIKE ? DESC, user_full_name LIKE ? DESC LIMIT 3", (search_query, search_query, search_query, search_query)).fetchall()
 
        return {"info":"ok", "results": search_result}
    except Exception as ex:
        print(ex)
        try:
            response.status = ex.args[0]
            return {"info":ex.args[1]}
        except:
            response.status = 500
            return {"info":str(ex)}
    finally:
        if 'db' in locals(): db.close()