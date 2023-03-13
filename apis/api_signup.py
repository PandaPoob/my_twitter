from bottle import post, request, response
import x

@post("/api-signup")
def _():
    try:
        #validate before open db
        #To do valiate username
        user_name = x.validate_signup()
        user_id = 1
        user = {
            "user_id": user_id,
            "user_name": user_name
        }
        #db.execute("INSERT INTO users VALUES(:user_id, :user_name)", user)
        values = ""
        for key in user:
            values = values + f":{key},"
        values = values.rstrip(",")
        print(values)
        #db.execute(f"INSERT INTO users VALUES({values})", user)
        return "ok"                        
    except Exception as ex:
        print(ex)
        return {"info": str(ex)}
    finally:
        if "db" in locals(): db.close()