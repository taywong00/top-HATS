# Team top_HATS
# Holden, Adam, Taylor, Samantha - pd7
# Methods used in transactions

import sqlite3   # database functions 

f = "../data/traders.db"
# os.remove(f) --> Used during testing to remove file at the beginning

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

# Helper Functions ----------------------------------------------------------
# GIVEN the stock name RETURN the current price of stock
# Via: calling the api and retrieving the data
# Use: to get most recent price of a stock
def getStockPrice(stock):
    price = -1
    # ---------
    # API retrieval code here
    # price = <retrieval code> (stock)
    # ---------
    return price

def buy(balance, stock, amount):
    statement = "Bought ", amount, " shares of ", stock, " 
