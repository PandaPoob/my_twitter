from bottle import put, request, response
import x

@put('/api-verify-email')
def _():
    try:
        db = x.db()
        user_api_key = request.forms.get("welcome_user_api_key")
        user = db.execute("SELECT * FROM users WHERE user_api_key=? COLLATE NOCASE", (user_api_key,)).fetchone()
        if not user: raise Exception("No account found")
        if user["user_account_status"] != "inactive": raise Exception("Account could not be verified")

        db.execute(f"UPDATE users SET user_account_status=? WHERE user_api_key=?", (x.ACC_STATUS_ACTIVE, user_api_key,))
        db.commit()

        return {"info":"ok"}
    except Exception as ex:
        print(ex)
        response.status = 400
        return {"info":str(ex)}
    finally:
        if 'db' in locals(): db.close()