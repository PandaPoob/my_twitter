import bcrypt
import x
db = x.db()

user = db.execute("SELECT * FROM users WHERE user_name= 'elonmusk' ").fetchall()[0]

salt = bcrypt.gensalt()
pw = bcrypt.hashpw(user['user_password'].encode('utf-8'), salt)
db.execute(f"UPDATE users SET user_password=? WHERE user_name = 'elonmusk'", (pw,))
db.commit()
db.close()

#users = db.execute("SELECT * FROM users").fetchall()
#sql = f"UPDATE users SET user_password = {hash('elonmuskpass')} WHERE user_password = 'elonmuskpass'"
#sql = f"UPDATE users SET user_password = ''"
""" for u in range(len(users)):
    salt = bcrypt.gensalt()
    pw = bcrypt.hashpw(users[u]['user_password'].encode('utf-8'), salt)
    print(pw)
    db.execute(f"UPDATE users SET user_password=? WHERE user_name = user_name=?", (pw,)) """
    #print(users[u]['user_password'])

    #print(users[u]['user_password'])
#db.execute(sql)
