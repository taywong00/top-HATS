import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O
import os #Used for os.remove()


f = "../data/traders.db"
# os.remove(f) #Used During Testing to remove file at the beginning

def make_tables():
    f = "../data/traders.db"
    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()    #facilitate db ops
    command= "CREATE TABLE users(id TEXT, password TEXT, name TEXT, money FLOAT, friends BLOB, holdings BLOB, transactions BLOB)"
    #friends is stored in form of a list of IDs
    #holdings is stored as a list as follows: [[<SYMBL>, <AMNT>]]
    #transactions is stored in the form [<SYMBL>, (amnt price, time)]
    c.execute(command)
    db.commit()
    db.close


make_tables()
