import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O
import os #Used for os.remove()


f = "../data/traders.db"
# os.remove(f) #Used During Testing to remove file at the beginning

def make_tables():
    f = "../data/traders.db"
    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()    #facilitate db ops
    command= "CREATE TABLE users(id INTEGER, password TEXT, name TEXT, money REAL, friends TEXT, holdings TEXT, transactions TEXT)"
    #friends is stored in form of a csv list of IDs
    #holdings is stored as a list as follows: <SYMBL>,<AMNT>\n...
    #transactions is stored in the form <SYMBL>, <amnt>, <price per share>, <price total>, <time>
    c.execute(command)
    db.commit()
    db.close


def display_tables():
    f = "../data/traders.db"
    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()    #facilitate db ops
    c.execute("SELECT * FROM users")
    rows=c.fetchall()
    for row in rows:
        print(row)

display_tables()
#make_tables()
