import sqlite3
import random   #enable control of a sqlite database
import csv       #facilitates CSV I/O
import os #Used for os.remove()
from flask import url_for, redirect, flash, render_template

f = "data/traders.db"
#####os.remove(f) #Used During Testing to remove file at the beginning

def make_tables():
    #f = "../data/traders.db"
    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()    #facilitate db ops
    command= "CREATE TABLE users(id INTEGER, password TEXT, name TEXT, money REAL, friends TEXT, holdings TEXT, transactions TEXT)"
    #friends is stored in form of a csv list of IDs
    #holdings is stored as a list as follows: <SYMBL>,<AMNT>,<LAST_PRICE>,<TOTAL_VAL>,<LAST_TIME>\n...
    #transactions is stored in the form <SYMBL>, <amnt>, <price per share>, <price total>, <time>
    c.execute(command)
    db.commit()
    db.close()

def display_tables():
    #f = "../data/traders.db"
    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()    #facilitate db ops
    c.execute("SELECT * FROM users")
    rows = c.fetchall()
    db.commit()
    db.close()
    for row in rows:
        for item in row:
            if item:
                print item
            else:
                print "null"
        print ''
    return True

def getUsers():
    users = {}
    #f = "..data/traders.db"
    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()    #facilitate db ops
    command = "SELECT password, name FROM users"
    #command= "CREATE TABLE users(id INTEGER, password TEXT, name TEXT, money REAL, friends TEXT, holdings TEXT, transactions TEXT)"
    #friends is stored in form of a csv list of IDs
    #holdings is stored as a list as follows: <SYMBL>,<AMNT>,<LAST_PRICE>,<TOTAL_VAL>,<LAST_TIME>\n...
    #transactions is stored in the form <SYMBL>, <amnt>, <price per share>, <price total>, <time>
    x = c.execute(command)
    #print "X: ", x
    for line in x:
        # print "Line: ", line
        users[line[1]] = line[0]
    return users

def create_user(username, password):
    if username in getUsers():
        print "Username already taken."
        return render_template('signup.html', message = 'Username already taken. Please choose a different one.', good = False)
    else:
        db = sqlite3.connect(f)#"../data/traders.db") #open if f exists, otherwise create
        c = db.cursor()    #facilitate db ops
        _id=random.randint(0,1000000)
        while check_id(_id):
            _id=random.randint(0,1000000)
        command = "INSERT INTO users VALUES("+str(_id)+", '" + password + "', '" + username + "', 100000, '','','');"
        print command
        c.execute(command)
        db.commit()
        db.close()
        return render_template('home.html', message = 'Account successfully created!', good = True)

def check_id(num):
    db = sqlite3.connect(f)#"../data/traders.db") #open if f exists, otherwise create
    c = db.cursor()    #facilitate db ops
    command="SELECT * FROM users WHERE id="+str(num)
    c.execute(command)
    users=c.fetchall()
    db.commit()
    db.close()
    if len(users)==0:
        return False
    else:
        return True

'''
def create_user(name, hashed_pword):
    f = "../data/traders.db"
    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()    #facilitate db ops
    command= "INSERT INTO users VALUES("+str(random.randint(0,1000000000))+",'"+hashed_pword+"','"+name+"',100000,'','','')"
    c.execute(command)
    db.commit()
    db.close
'''

def add_friend(user_id, friend_id):
    #f = "../data/traders.db"
    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()    #facilitate db ops
    command="""UPDATE users
    SET friends= friends || '"""+friend_id+""",'
    WHERE id='"""+user_id+"'"
    c.execute(command)
    #append list and replace
    db.commit()

def change_pass(user_id, old_pass, new_pass_1, new_pass_2):
    #f = "../data/traders.db"
    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()    #facilitate db ops
    #get password from user
    if old_pass==pword and new_pass_1==new_pass_2:
        #set new pass as pword in db
        return "success"
    else:
        return "failure"

#holdings is stored as a list as follows: <SYMBL>,<AMNT>,<LAST_PRICE>,<TOTAL_VAL>,<LAST_TIME>\n...
#transactions is stored in the form <SYMBL>, <amnt>, <price per share>, <price total>, <time>
def get_holdings(user_id):
    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()    #facilitate db ops
    command="SELECT holdings FROM users WHERE id='"+str(user_id)+"'"
    c.execute(command)
    holdings=c.fetchall()
    db.close()
    #if holdings is not null
    if len(holdings)>0:
        holdings=holdings[0][0]
        holdings=holdings.split("\n")
        for i in range(len(holdings)):
            holdings[i]=holdings[i].split(",")[0:-1]
        holdings=holdings[0:-1]
    else:
        holdings=[['',0,0,0,0]]
    return holdings

#print get_holdings(801266)


#"CREATE TABLE users(id TEXT, password TEXT, name TEXT, money FLOAT, friends BLOB, holdings BLOB, transactions BLOB)"
#add_friend('996401703','000')
#create_user("def","456")
#create_user("hij","789")

"""
try:
    make_tables()
except:
    print "Table already created"
addUser("pumpkin", "pie", "easy")
addUser("pumpkin", "pie", "easy")
addUser("Mickey", "Mouse", "easy")
addUser("Frank", "Sinatra", "medium")
addUser("Orange", "Juice", "medium")
addUser("Scrambled", "Eggs", "hard")
addUser("ice", "cream", "hard")
#"""

#display_tables()
#print getUsers()
