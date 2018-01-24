import sqlite3, random
import uuid, hashlib

# Credit: Python Central
def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

# Credit: Python Central    
def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

''' Testing Functions
new_pass = "Popcorn"
hashed_password = hash_password(new_pass)
print('The string to store in the db is: ' + hashed_password)
old_pass = "Popcor"
if check_password(hashed_password, old_pass):
    print('You entered the right password')
else:
    print('I am sorry but the password does not match')
'''
    
def get_users():
    f = "data/traders.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    command = "SELECT name, password FROM users"
    sq_result = c.execute(command)
    users = {}
    for entry in sq_result:
        users[entry[0]] = entry[1]
    db.close
    return users

def create_user(name, hashed_pword):
    f = "data/traders.db"
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
#create_user("def","456")
#create_user("hij","789")
