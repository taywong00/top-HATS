# Team top_HATS
# Holden, Adam, Taylor, Samantha - pd7
# Methods used in transactions

import sqlite3, json, datetime, math   # database functions
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

#print get_leaderboard()

def buy(user_id, stock_name, num_of):
    one_stock = getStockPrice(stock_name)
    num_of=math.abs(num_of)
    price = one_stock * num_of
    if(get_balance(user_id) >= price):
        price *= -1
        add_transaction(user_id, stock_name, num_of, price)
        update_portfolio(user_id, stock_name, num_of, price)
        adjust_money(user_id, price)
        return "Bought."
    else:
        return "Purchase error. Insufficient funds."

#testers
buy(123,'GOOG',10)

def sell(user_id, stock_name, num_of):
    one_stock = getStockPrice(stock_name)
    num_of=math.abs(num_of)
    price = one_stock * num_of
    num_of*=-1
    if(check_portfolio(user_id, stock_name, num_of)):
        add_transaction(user_id, stock_name, num_of, price)
        update_portfolio(user_id, stock_name, num_of, price)
        adjust_money(user_id, price)
        return "Sold."
    else:
        return "Sale error. Transaction cancelled"



def get_balance(user_id):
    f = "../data/traders.db"
    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()    #facilitate db ops
    command="""SELECT money
    FROM users
    WHERE id="""+user_id+";"
    c.execute(command)
    balance=c.fetchone()[0]
    db.commit()
    db.close
    return balance


def adjust_money(user_id, amt):
    og_mons=get_balance(user) # Original amount of money
    db = sqlite3.connect(f)
    c = db.cursor()
    if((og_mons + amt)<0):
        return -1
    else:
        og_mons+= amt
        cmd = "UPDATE users SET money=" + str(og_mons) + " WHERE id=" + user_id
        c.execute(cmd)
        db.commit()
        db.close()
        return og_mons

#print adjust_money("abc",-100000000000)
#print get_balance("abc")



def check_portfolio(user_id, stock, amount):
    f = "../data/traders.db"
    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()    #facilitate db ops
    command="SELECT holdings FROM users WHERE id='"+user_id+"'"
    c.execute(command)
    holdings=c.fetchall()[0]
    holdings=holdings.split("\n")
    has_stock=False
    for stk in holdings:
        if stk[0]==stock:
            has_stock=stk
    if not has_stock:
        return False #does not own
    elif not has_stock[1]<(amount*-1):
        return False #does not have enough
    else:
        return True
    db.commit()
    db.close()


#adds transaction to transactions (history)
#for sale price is positive and amount is negative
#for buy price is negative and amount is positive
def add_transaction(user_id, stock, amount, price):
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

#helper function to convert lists to csv string
def stringify(holdings):
    new_holdings=""
    for stock in holdings:
        for val in stock:
            new_holdings+=val+","
        new_holdings+="\n"
    return new_holdings


#updates holdings to reflect purchase or sale
#for sale price and amount are negative
#for buy price and amount are positive
def update_portfolio(user_id, stock, amount, price):
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
    new_holdings=stringify(holdings)
    command="UPDATE users SET holdings='"+new_holdings+"' WHERE is='"+user_id+"'"
    c.execute(command)
    db.commit()
    db.close()
    #id INTEGER, password TEXT, name TEXT, money REAL, friends TEXT, holdings TEXT, transactions TEXT
    ###the things that matter
    #get last line of trade history
    #adjust portfolio accordingly
    #big csv function that has to adjust and delete anywhere within portfolio
