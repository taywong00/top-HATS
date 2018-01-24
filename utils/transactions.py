# Team top_HATS
# Holden, Adam, Taylor, Samantha - pd7
# Methods used in transactions

import sqlite3, json, datetime # database functions
from datetime import timedelta
import pytz
import API_funcs
f = "data/traders.db"
# os.remove(f) --> Used during testing to remove file at the beginning

tz=pytz.timezone('America/New_York')
key = "I47O8J6SBM5S3302"

# Helper Functions ----------------------------------------------------------
# GIVEN the stock name RETURN the current price of stock
# Via: calling the api and retrieving the data
# Use: to get most recent price of a stock
def getStockPrice(stock):
    price = -1
    d = API_funcs.get_data(stock, key)
    now = datetime.datetime.now(tz)
    #print now
    #print now.hour
    if now.hour < 9:
        now = now - timedelta(days=1)
        #print now
    dt = now.date()
    price = d["Time Series (Daily)"][str(dt)]["4. close"]
    return price

def getHigh(stock):
    d = API_funcs.get_data(stock, key)
    now = datetime.datetime.now(tz)
    #print now
    if now.hour < 9:
        now = now - timedelta(days=1)
        print now
    dt = now.date()
    high = d["Time Series (Daily)"][str(dt)]["2. high"]
    return high

def getLow(stock):
    d = API_funcs.get_data(stock, key)
    now = datetime.datetime.now(tz)
    #print now
    if now.hour < 9:
        now = now - timedelta(days=1)
        #print now
    dt = now.date()
    low = d["Time Series (Daily)"][str(dt)]["3. low"]
    return low


#getStockPrice("GOOG");

def get_leaderboard():
    leaderboard = {}
    f = "data/traders.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    command = """SELECT name, money
    FROM users
    ORDER BY
    money DESC;"""
    x = c.execute(command)
    counter = 1
    '''
    for line in x:
        print "     0: ", line[0]
        print "     1: ", line[1]
    x = c.execute(command)
    '''
    for line in x:
        if counter <= 10:
            info = [0,1]
            # Used to see top ten users and *their balances
            # print "0: ", line[0]
            # print "1: ", line[1]
            info[0] = line[0]
            info[1] = line[1]
            #print info
            leaderboard[counter] = info
            # leaderboard[line[0]] = counter
            counter += 1
        else:
            break
    return leaderboard

#print "LEADERBOARD: "
#print get_leaderboard()

def get_id(username):
    if username:
        db = sqlite3.connect(f) #open if f exists, otherwise create
        c = db.cursor()    #facilitate db ops
        command="""SELECT id
        FROM users
        WHERE name='""" + username + "'"
        c.execute(command)
        _id=c.fetchall()[0][0]
        #print _id
        db.close()
        return int(_id)
    else:
        #print "\n\n\n\n\n-------------------------------------------------------"
        return -1

def buy(username, stock_name, num_of, price):
    stock_name=stock_name.upper()
    #print username
    #print "\n\n\n\n\n-------------------------------------------------------"
    user_id= get_id(username)
    num_of=abs(float(num_of))
    #print "\n\n\n\n\n-------------------------------------------------------"
    price=float(price)
    price_total = price * num_of
    if(get_balance(user_id) >= price_total):
        add_transaction(user_id, stock_name, num_of, price)
        update_portfolio(user_id, stock_name, num_of, price)
        adjust_money(user_id, price_total*-1)
        return price_total
    else:
        return -1

#testers
#buy(123,'GOOG',10)

def sell(username, stock_name, num_of, price):
    stock_name=stock_name.upper()
    user_id= username
    num_of=abs(float(num_of))
    price=float(price)
    price_total = price * num_of
    num_of*=-1
    if(check_portfolio(user_id, stock_name, num_of)):
        add_transaction(user_id, stock_name, num_of, price)
        update_portfolio(user_id, stock_name, num_of, price)
        adjust_money(user_id, price_total)
        print "Sold."
        return price_total
    else:
        print "Sale error. Transaction cancelled"
        return -1


def get_balance(user_id):
    #f = "../data/traders.db"
    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()    #facilitate db ops
    command="""SELECT money
    FROM users
    WHERE id="""+str(user_id)
    #print command
    c.execute(command)
    balance=c.fetchone()[0]
    db.commit()
    db.close
    return balance

def adjust_money(user_id, amt):
    og_mons=get_balance(user_id) # Original amount of money
    db = sqlite3.connect(f)
    c = db.cursor()
    if((og_mons + amt)<0):
        return -1
    else:
        og_mons+= amt
        cmd = "UPDATE users SET money=" + str(og_mons) + " WHERE id=" + str(user_id)
        c.execute(cmd)
        db.commit()
        db.close()
        return og_mons

#print adjust_money("abc",-100000000000)
#print get_balance("abc")

def check_portfolio(user_id, stock, amount):
    #f = "../data/traders.db"
    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()    #facilitate db ops
    command="SELECT holdings FROM users WHERE id='"+str(user_id)+"'"
    c.execute(command)
    holdings=c.fetchall()
    db.commit()
    db.close()
    if len(holdings)>0:
        holdings=holdings[0][0]
        holdings=holdings.split("\n")
        has_stock=False
        for stk in holdings:
            stk=stk.split(',')
            if stk[0]==stock:
                has_stock=stk
        if not has_stock:
            print "missing"
            return False #does not own
        elif not float(has_stock[1])>=abs(amount):
            print has_stock
            print "poor"
            return False #does not have enough
        else:
            return True
    else:
        print "nada"
        return False

#adds transaction to transactions (history)
#for sale amount is negative
#for buy amount is positive
#PRICE IS ALWAYS POSITIVE
def add_transaction(user_id, stock, amount, price):
    price=abs(price)
    time=datetime.datetime.now(tz)
    trade=stock+','+str(amount)+','+str(price)+','+str(price*amount)+','+str(time)+"\n"
    #f = "../data/traders.db"
    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()    #facilitate db ops
    command="""UPDATE users
    SET transactions= transactions || '"""+trade+"""'
    WHERE id='"""+str(user_id)+"'"
    c.execute(command)
    db.commit()
    db.close()

#helper function to convert lists to csv string
def stringify(holdings):
    new_holdings=""
    for stock in holdings:
        if len(stock)>1:
            for val in stock:
                if len(str(val))>0:
                    new_holdings+=str(val)+","
            new_holdings+="\n"
    return new_holdings

#updates holdings to reflect purchase or sale
#for sale amount is negative
#for buy amount is positive
#PRICE IS ALWAYS POSITIVE
def update_portfolio(user_id, stock, amount, price):
    price=abs(price)
    time=datetime.datetime.now(tz)
    #f = "../data/traders.db"
    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()    #facilitate db ops
    command="SELECT holdings FROM users WHERE id='"+str(user_id)+"'"
    c.execute(command)
    holdings=c.fetchall()
    #if holdings is full
    if len(holdings)>0:
        holdings=holdings[0][0]
        holdings=holdings.split("\n")
        has_stock=False
        #search for stock in holdings
        for i in range(len(holdings)):
            holdings[i]=holdings[i].split(",")
            if holdings[i][0]==stock:
                has_stock=True
                holdings[i][1]=float(holdings[i][1])+amount
                holdings[i][2]=price
                holdings[i][3]=float(holdings[i][1])*price
                holdings[i][4]=time
        #if stock is not found in holdings
        if not has_stock:
            new_stock=[[stock,amount,price,amount*price,time]]
            holdings+=new_stock
    #if holdings is empty
    else:
       new_stock=[[stock,amount,price,amount*price,time]]
       holdings+=new_stock
    new_holdings=stringify(holdings)
    #print new_holdings
    command="UPDATE users SET holdings='"+new_holdings+"' WHERE id='"+str(user_id)+"'"
    c.execute(command)
    db.commit()
    db.close()
    #id INTEGER, password TEXT, name TEXT, money REAL, friends TEXT, holdings TEXT, transactions TEXT

def stock_val(user_id):
    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()    #facilitate db ops
    command="SELECT holdings FROM users WHERE id='"+str(user_id)+"'"
    c.execute(command)
    holdings=c.fetchall()
    total_val=0
    #if holdings is full
    if len(holdings)>0:
        holdings=holdings[0][0]
        holdings=holdings.split("\n")
        for i in range(len(holdings)):
            holdings[i]=holdings[i].split(",")
            price=getStockPrice(holdings[i][0])
            value=price*holdings[i][1]
            holdings[i][3]=value
            total_val+=value
        new_holdings=stringify(holdings)
        command="UPDATE users SET holdings='"+new_holdings+"' WHERE id='"+str(user_id)+"'"
        c.execute(command)
    db.commit()
    db.close()
    return total_val

def total_val(user_id):
   return stock_val(user_id)+float(get_balance(user_id))


