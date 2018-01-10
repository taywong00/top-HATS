# Team top_HATS
# Holden, Adam, Taylor, Samantha - pd7
# Methods used in transactions

import sqlite3, json, datetime   # database functions
import API_funcs
f = "../data/traders.db"
# os.remove(f) --> Used during testing to remove file at the beginning

def make_tables():
    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()    #facilitate db ops
    command= "CREATE TABLE users(id TEXT, password TEXT, name TEXT, money FLOAT, friends BLOB, holdings BLOB, transactions BLOB)"
    #friends is stored in form of a list of IDs
    #holdings is stored as a list as follows: [[<SYMBL>, <AMNT>]]
    #transactions is stored in the form [<SYMBL>, (amnt price, time)]
    c.execute(command)
    db.commit()
    db.close

# Helper Functions ----------------------------------------------------------
# GIVEN the stock name RETURN the current price of stock
# Via: calling the api and retrieving the data
# Use: to get most recent price of a stock
def getStockPrice(stock):
    price = -1
    key = "I47O8J6SBM5S3302"
    d = API_funcs.get_data(stock, key)
    dt = datetime.datetime.now().date()
    #dt = dt.replace(hour = 0, minute = 0, second=0, microsecond = 0)
    print dt
    #print json.dumps(d["Time Series (Daily)"], indent = 4, sort_keys = False)
    print json.dumps(d["Time Series (Daily)"][str(dt)]["4. close"], indent = 4, sort_keys = True)
    # ---------
    # API retrieval code here
    # price = <retrieval code> (stock)
    # ---------
    return price

getStockPrice("GOOG");

def getbalance(username):
    f = "../data/traders.db"
    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()    #facilitate db ops
    command="""SELECT money
    FROM users
    WHERE name="""+username+";"
    balance= c.execute(command)
    return balance

def adjust_money(user, amt):	
	db = sqlite3.connect(f)
	c = db.cursor()	
	cmd = "SELECT money FROM users WHERE name=" + user 
	c.execute(cmd)
	og_mons = c.fetchone() 
	if(og_mons + amt):
		return -1
	else:
		og_mons += amt
		cmd = "UPDATE users SET money=" + og_mons + " WHERE name=" + user
		c.execute(cmd)
		db.commit()
		db.close()
		return og_mons


def buy(accountName, stock, amount):
    statement = "Bought ", amount, " shares of ", stock, ". Your new balance is "
    currentBalance = getBalance(accountName)
    # Do math
    return statement


