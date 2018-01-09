import sqlite3, Math

def createUser(name, hashed_pword):
    f = "../data/traders.db"
    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()    #facilitate db ops
    command= "INSERT INTO users VALUES("+Math.randint(1000000)+","+hashed_pword+","+name+"100000"+","


    "CREATE TABLE users(id TEXT, password TEXT, name TEXT, money FLOAT, friends BLOB, holdings BLOB, transactions BLOB)"
