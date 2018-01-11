import sqlite3, random

def create_user(name, hashed_pword):
    f = "../data/traders.db"
    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()    #facilitate db ops
    command= "INSERT INTO users VALUES("+str(random.randint(0,1000000000))+",'"+hashed_pword+"','"+name+"',100000,'','','')"
    c.execute(command)
    db.commit()
    db.close

def add_friend(user_id, friend_id):
    f = "../data/traders.db"
    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()    #facilitate db ops
    command="""UPDATE users
    SET friends= friends || '"""+friend_id+""",'
    WHERE id='"""+user_id+"'"
    c.execute(command)
    #append list and replace
    db.commit()
    db.close

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
#add_friend('996401703','000')
#create_user("abc","123")
