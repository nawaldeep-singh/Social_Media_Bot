import sqlite3 as sql
import os    

try:
    os.remove("media.db")

except:
    pass

finally:
    obj = sql.connect("media.db")
    cur = obj.cursor()
    cur.execute("create table platforms (workspaces text, platform text not null, login_id text , password text);")
    cur.execute("insert into platforms values ('insta', 'Instagram', null, null);")
    
    obj.commit()
    print("Database Repaired...")
    obj.close()
    exit()