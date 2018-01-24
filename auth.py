import sqlite3, random
import uuid, hashlib

f = "data/traders.db"

def hash_password(password,uid):
    return hashlib.sha256(str(uid) + password).hexdigest()

def check_password(username,password):
    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()    #facilitate db ops
    command = "SELECT id,password FROM users WHERE name='"+username+"'"
    c.execute(command)
    info=c.fetchall()[0]
    db.close()
    return info[1]  == hash_password(password,info[0])


    #"CREATE TABLE users(id TEXT, password TEXT, name TEXT, money FLOAT, friends BLOB, holdings BLOB, transactions BLOB)"

def change_pass(username, old_pass, new_pass_1, new_pass_2):
    if new_pass_1==new_pass_2:
        if check_password(old_pass):
            db = sqlite3.connect(f) #open if f exists, otherwise create
            c = db.cursor()    #facilitate db ops
            command = "SELECT id FROM users WHERE name='"+username+"'"
            c.execute()
            _id=c.fetchall()[0][0]
            command ="UPDATE users SET password='"+hash_password(new_pass1,_id )+"'"
            db.commit()
            db.close()
            return "success"
        else:
            return "incorrect password"
    else:
        return "please enter the same password in both fields for new password"


    #"CREATE TABLE users(id TEXT, password TEXT, name TEXT, money FLOAT, friends BLOB, holdings BLOB, transactions BLOB)"
#add_friend('996401703','000')
#create_user("def","456")
#create_user("hij","789")
