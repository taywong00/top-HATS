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
    price = d["Time Series (Daily)"][str(dt)]["4. close"]
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
    num_of=abs(num_of)
    price = one_stock * num_of
    if(get_balance(user_id) >= price):
        price *= -1
        add_transaction(user_id, stock_name, num_of, one_stock)
        update_portfolio(user_id, stock_name, num_of, one_stock)
        adjust_money(user_id, price)
        return "Bought."
    else:
        return "Purchase error. Insufficient funds."

#testers
#buy(123,'GOOG',10)

def sell(user_id, stock_name, num_of):
    one_stock = getStockPrice(stock_name)
    num_of=abs(num_of)
    price = one_stock * num_of
    num_of*=-1
    if(check_portfolio(user_id, stock_name, num_of)):
        add_transaction(user_id, stock_name, num_of, one_stock)
        update_portfolio(user_id, stock_name, num_of, one_stock)
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
    WHERE id="""+str(user_id)+";"
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
        cmd = "UPDATE users SET money=" + str(og_mons) + " WHERE id=" + str(user_id)
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
    command="SELECT holdings FROM users WHERE id='"+str(user_id)+"'"
    c.execute(command)
    holdings=c.fetchall()[0][0]
    if holdings:
        holdings=holdings.split("\n")
        has_stock=False
        for stk in holdings:
            stk=stk.split(',')
            if stk[0]==stock:
                has_stock=stk
        if not has_stock:
            return False #does not own
        elif not int(has_stock[1])>abs(amount):
            return False #does not have enough
        else:
            return True
    else:
        return False
    db.commit()
    db.close()

#print check_portfolio(933041681,'KX',1)

#adds transaction to transactions (history)
#for sale amount is negative
#for buy amount is positive
#PRICE IS ALWAYS POSITIVE
def add_transaction(user_id, stock, amount, price):
    price=abs(price)
    time=datetime.datetime.now()
    trade=stock+','+str(amount)+','+str(price)+','+str(price*amount)+','+str(time)+"\n"
    f = "../data/traders.db"
    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()    #facilitate db ops
    command="""UPDATE users
    SET transactions= transactions || '"""+trade+"""'
    WHERE id='"""+str(user_id)+"'"
    c.execute(command)
    db.commit()
    db.close()

#add_transaction(933041681, 'KX', 10, -100,)
#add_transaction(933041681, 'IB', 10, -57,)

#helper function to convert lists to csv string
def stringify(holdings):
    new_holdings=""
    for stock in holdings:
        for val in stock:
            if str(val):
                new_holdings+=str(val)+","
        new_holdings+="\n"
    return new_holdings


#updates holdings to reflect purchase or sale
#for sale amount is negative
#for buy amount is positive
#PRICE IS ALWAYS POSITIVE
def update_portfolio(user_id, stock, amount, price):
    price=abs(price)
    time=datetime.datetime.now()
    f = "../data/traders.db"
    db = sqlite3.connect(f) #open if f exists, otherwise create
    c = db.cursor()    #facilitate db ops
    command="SELECT holdings FROM users WHERE id='"+str(user_id)+"'"
    c.execute(command)
    holdings=c.fetchall()[0][0]
    holdings=holdings.split("\n")
    has_stock=False
    for i in range(len(holdings)):
        holdings[i]=holdings[i].split(",")
        if holdings[i][0]==stock:
            has_stock=True
            holdings[i][1]=int(holdings[i][1])+amount
            holdings[i][2]=price
            holdings[i][3]=int(holdings[i][1])*price
            holdings[i][4]=time
    if not has_stock:
        new_stock=[[stock,amount,price,amount*price,time]]
        holdings+=new_stock
    new_holdings=stringify(holdings)
    print new_holdings
    command="UPDATE users SET holdings='"+new_holdings+"' WHERE id='"+str(user_id)+"'"
    c.execute(command)
    db.commit()
    db.close()
    #id INTEGER, password TEXT, name TEXT, money REAL, friends TEXT, holdings TEXT, transactions TEXT

#update_portfolio(933041681, 'KX', 10, -100,)
#update_portfolio(933041681, 'IB', 10, -57,)
'''
if check_portfolio(933041681,'IB', 7):
    add_transaction(933041681, 'IB', -7, 10,)
    update_portfolio(933041681, 'IB', -7, 10,)
else:
    print "too few"
'''
