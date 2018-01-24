# Team top_HATS
# Holden Higgins, Adam Abbas, Taylor Wong, Samantha Ngo
# SoftDev1 pd7
# P#02 -- This Is the End

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
        if check_password(username,old_pass):
            db = sqlite3.connect(f) #open if f exists, otherwise create
            c = db.cursor()    #facilitate db ops
            command = "SELECT id FROM users WHERE name='"+username+"'"
            c.execute(command)
            _id=c.fetchall()[0][0]
            command ="UPDATE users SET password='"+hash_password(new_pass1,_id )+"'"
            c.execute(command)
            db.commit()
            db.close()
            return "success"
        else:
            return "incorrect username or password"
    else:
        return "please enter the same password in both fields for new password"

def change_name(old_name, new_name1, new_name2, password):
    if new_name1==new_name2:
        if check_password(old_name, password):
            db = sqlite3.connect(f) #open if f exists, otherwise create
            c = db.cursor()    #facilitate db ops
            command ="UPDATE users SET name='"+new_name1+"'"
            c.execute(command)
            db.commit()
            db.close()
            return "success"
        else:
            return "incorrect username or password"
    else:
        return "please enter the same name in both fields for new username"


    #"CREATE TABLE users(id TEXT, password TEXT, name TEXT, money FLOAT, friends BLOB, holdings BLOB, transactions BLOB)"
#add_friend('996401703','000')
#create_user("def","456")
#create_user("hij","789")
