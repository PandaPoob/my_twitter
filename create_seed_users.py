import sqlite3
import uuid
from faker import Faker
fake = Faker()

db = sqlite3.connect("twitter.db")

db.executescript(
    """
    BEGIN;
    DROP TABLE IF EXISTS users;
    CREATE TABLE users(
        id          TEXT,
        name        TEXT,
        email       TEXT UNIQUE,
        PRIMARY KEY(id)
    ) WITHOUT ROWID;
    COMMIT;
    """
)


#python  
for u in range(100000):
    id = str(uuid.uuid4()) #type is UUID but we make it text
    name = fake.first_name()
    #email = fake.email()
    email = name.lower() + id.replace("-", "") + "@" + fake.free_email_domain()
    
    db.execute(f"INSERT INTO users(id,name,email) VALUES('{id}','{name}','{email}')")

db.commit()