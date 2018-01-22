import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O
import os #Used for os.remove()


f = "../data/traders.db"
#os.remove(f) #Used During Testing to remove file at the beginning

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
    db.close()

def display_tables():
	f = "../data/traders.db"
	db = sqlite3.connect(f) #open if f exists, otherwise create
	c = db.cursor()    #facilitate db ops
	c.execute("SELECT * FROM users")
	rows = c.fetchall()
	for row in rows:
		for item in row:
			if item:
				print item
			else:
				print "null"
		print '\n'
	return True

def getUsers():
	users = {}
	db = sqlite3.connect("../data/traders.db") #open if f exists, otherwise create
	c = db.cursor()    #facilitate db ops
	command = "SELECT password, name FROM users"
    #command= "CREATE TABLE users(id INTEGER, password TEXT, name TEXT, money REAL, friends TEXT, holdings TEXT, transactions TEXT)"
    #friends is stored in form of a csv list of IDs
    #holdings is stored as a list as follows: <SYMBL>,<AMNT>\n...
    #transactions is stored in the form <SYMBL>, <amnt>, <price per share>, <price total>, <time>
	x = c.execute(command)
	print "X: ", x
	for line in x:
		# print "Line: ", line
		users[line[1]] = line[0]
	db.close()
	return users
	
def addUser(username, password, level):
	if username in getUsers():
		print "Username already taken."
		return "Username already taken."
	else: 
		balance = -1
		if level == "easy":
			balance = 10000
		elif level == "medium":
			balance = 1000
		elif level == "hard":
			balance = 100
		db = sqlite3.connect("../data/traders.db") #open if f exists, otherwise create
		c = db.cursor()    #facilitate db ops
		command = "INSERT INTO users VALUES(0, '" + password + "', '" + username + "', " + str(balance) + ", 'none','none','none');"
		print command
		c.execute(command)
		db.commit()
		db.close()
		return True

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
display_tables()
print getUsers()
    