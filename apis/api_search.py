from bottle import post, response
import json
import x
@post('/api-search')
def _():
    try:
        #db = x.db()
        response.set_header("Content-type", "application/json")
        return json.dumps([{"name":"A"}, {"name":"B"}])
        #return {"info":"ok"}
    except Exception as ex:
        print(ex)
        response.status = 400
        return {"info":str(ex)}
    finally:
        pass
        #if 'db' in locals(): db.close()