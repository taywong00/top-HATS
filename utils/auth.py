import sqlite3, Math

def createUser(name, hashed_pword):
    f = "../data/traders.db"
    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()    #facilitate db ops
    command= "INSERT INTO users VALUES("+Math.randint(1000000)+","+hashed_pword+","+name+"100000"+", [],[],[]"

def add_friend(user_id, friend_id):
    f = "../data/traders.db"
    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()    #facilitate db ops
    #pull friend list
    #append list and replace

def change_pass(user_id, old_pass, new_pass_1, new_pass_2):
    f = "../data/traders.db"
    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()    #facilitate db ops
    #get password from user
    if old_pass==pword and new_pass_1==new_pass_2:
        #set new pass as pword in db
        return "success"
    else:
        return "failure"


    #"CREATE TABLE users(id TEXT, password TEXT, name TEXT, money FLOAT, friends BLOB, holdings BLOB, transactions BLOB)"
