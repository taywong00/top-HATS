# Team top_HATS
# Holden, Adam, Taylor, Samantha - pd7
# Methods used in transactions

import sqlite3, json, datetime   # database functions
import API_funcs
f = "../data/traders.db"
# os.remove(f) --> Used during testing to remove file at the beginning

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



#getStockPrice("GOOG");

def get_balance(user):
    user="'"+user+"'"
    f = "../data/traders.db"
    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()    #facilitate db ops
    command="""SELECT money
    FROM users
    WHERE name="""+user+";"
    c.execute(command)
    balance=c.fetchone()[0]
    db.commit()
    db.close
    return balance

def get_leaderboard():
    f = "../data/traders.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    command = """SELECT name
    FROM users
    ORDER BY
    money"""
    c.execute(command)
    users = c.fetchone()
    db.commit()
    db.close
    return users

print get_leaderboard()

def buy(stock_name, num_of):
    one_stock = getStockPrice(stock_name)
    price = one_stock * num_of
    price *= -1
    adjust_money(session.get('username'), price)
    return "Bought."

def sell(stock_name, num_of):
    one_stock = getStockPrice(stock_name)
    price = one_stock * num_of
    adjust_money(session.get('username'), price)
    return "Sold."

def adjust_money(user, amt):
    og_mons=get_balance(user) # Original amount of money
    user="'"+user+"'"
    db = sqlite3.connect(f)
    c = db.cursor()
    if((og_mons + amt)<0):
        return -1
    else:
        og_mons+= amt
        cmd = "UPDATE users SET money=" + str(og_mons) + " WHERE name=" + user
        c.execute(cmd)
        db.commit()
        db.close()
        return og_mons

#print adjust_money("abc",-100000000000)
#print get_balance("abc")


def buy(accountName, stock, amount):
    statement = "Bought ", amount, " shares of ", stock, ". Your new balance is "
    currentBalance = getBalance(accountName)
    # Do math
    return statement


def add_transaction(stock, amount, price, user_id):
    time=date.datetime()
    trade=stock+','+str(amount)+','+str(price)+','+str(price*amount)+','+str(time)+"\n"
    f = "../data/traders.db"
    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()    #facilitate db ops
    command="""UPDATE users
    SET transactions= transactions || '"""+trade+"""'
    WHERE id='"""+user_id+"'"
    c.execute(command)
    db.commit()
    db.close()


def check_portfolio(stock, amount):
    f = "../data/traders.db"
    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()    #facilitate db ops
    if not stock:
        return "yeet"
    if stock and not amount:
        return "2 poor"
    else:
        return "litty gvng"

def update_portfolio(stock, amount, price, user_id):
    f = "../data/traders.db"
    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()    #facilitate db ops
    command="SELECT holdings FROM users WHERE id='"+user_id+"'"
    c.execute(command)
    holdings=c.fetchall()[0]
    holdings=holdings.split("\n")
    has_stock=False
    for i in range(holdings.len):
        holdings[i]=holdings[i].split(",")
        if amount>0 and holdings[i][0]==stock:
            has_stock=True
            holdings[i][1]+=amount
            holdings[i][2]=price
            holdings[i][3]=holdings[i][1]*price
            holdings[i][4]=date.datetime()
    if not has_stock:
        new_stock=[stock,amount,price,amount*price,date.datetime()]
        holdings+=new_stock
    new_holdings=""
    for stock in holdings:
        for val in stock:
            new_holdings+=val+","
        new_holdings+="\n"

    #id INTEGER, password TEXT, name TEXT, money REAL, friends TEXT, holdings TEXT, transactions TEXT
    ###the things that matter
    #get last line of trade history
    #adjust portfolio accordingly
    #big csv function that has to adjust and delete anywhere within portfolio
    c.execute(command)
    db.commit()
    db.close()
