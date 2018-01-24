# Team top_HATS
# Holden Higgins, Adam Abbas, Taylor Wong, Samantha Ngo
# SoftDev1 pd7
# P0# --
# 2018-01-02

import os
from flask import Flask, render_template, request, session
from flask import redirect, flash, url_for
from utils import transactions, data_builder, API_funcs
import auth
import json
#from util import

app = Flask (__name__)
app.secret_key = "RpdMo7f9KTwLwkKlP2UrNiSG96Hby7NV"

# HOMEPAGE: brief description and two buttons--"Login" or "Create an account"
@app.route("/")
def home():
    if session.get('username'):
        #print session.get("username")
        return redirect("/feed")
    else:
        return render_template("home.html")

# Status: DONE
# LOGIN: name of product/logo and then "Username:", "Password:", and "Don't have an account? <CREATE hyperlink> one."
@app.route('/login', methods=['GET', 'POST'])
def login():
    #print "REQUEST: ", request.form.get("login")
    # if user already logged in, redirect to homepage(base.html)
    if session.get('username'):
        return redirect('/feed')
    # user entered login form
    elif request.form.get("login") == "Login":
        username = request.form.get("username").strip()
        #print "USERNAME: ", username
        password = request.form.get("password")
        #print "PASSWORD: ", password

        # checks credentials for login
        users = data_builder.getUsers()
        if username in users:
            if auth.check_password(username, password):
                session['username'] = username
                return redirect("/feed")
            else:
                return render_template("home.html", message = "Oops! Wrong password.", good = False)
        else:
            return render_template("home.html", message = "Oops! That username doesn't exist.", good = False)
    else:
        print request.form.get("login")
        return render_template("home.html")

# Status: DONE
@app.route("/signup_page")
def signup_page():
    if session.get("username"):
        return "Please log out before creating a new account."
    else:
        return render_template('signup.html')

# Status: DONE
# LOGIN: name of product/logo and then "Username:", "Password:", and "Don't have an account? <CREATE hyperlink> one."
@app.route("/create_account", methods=['GET', 'POST'])
def create_account():
    #print "REQUEST CREATE: ", request.form.get("create_account")
    # If the user is already logged in:
    if session.get('username'):
        return redirect('/feed')
    # If the user clicks Create Account
    elif request.form.get("create_account") == "Create Account":
        username = request.form.get("username").strip()
        #print "U: ", username
        password1 = request.form.get("password1")
        #print "P1: ", password1
        password2 = request.form.get("password2")
        #print "P2: ", password2
        pfp = request.form.get("pfp")
        if password1 != password2:
            return render_template("signup.html", message = "Your passwords do not match. Please try again.", good = False)
        else:
            return data_builder.create_user(username, password1,pfp)#image is hardcoded
    else:
        return render_template("signup.html")

# Status: DONE
@app.route("/how_to", methods=['GET', 'POST'])
def how_to():
    return render_template("how_to.html")
# -------------

# Status: Complete
@app.route("/account", methods=['GET', 'POST'])
def account():
    if session.get('username'):
        user = session.get("username")
        stocks = data_builder.get_holdings(transactions.get_id(user))
        #print stocks
        for stock in stocks:
            stock.append(transactions.getStockPrice(stock[0]))
        # Get User Balance
        # balance =
        # #moneyz = transactions.get_balance(user)
        balance = transactions.get_balance(transactions.get_id(user))
        pfp = data_builder.get_pic_num(transactions.get_id(user))
        return render_template("account.html", name = user, balance = balance, stocks = stocks, pfp = pfp)
    else:
        return render_template("home.html", message="Please log in to see your account.", warning= True)

@app.route("/sell", methods=['GET', 'POST'])
def sell():
    user = session.get("username")
    #print user
    stock_ind = int(request.form["ind"])
    num_stock = float(request.form["num"])
    #print num_stock
    eyedee = transactions.get_id(user)
    stocks = data_builder.get_holdings(eyedee)
    stock = stocks[stock_ind]
    #print stock
    workd = transactions.sell(eyedee, stock[0], num_stock, transactions.getStockPrice(stock[0]))
    if workd > 0:
        return render_template("account.html", message="Sale successful!", good=True)

    else:
        return render_template("account.html", message="Sale error.", good=False)

# Status: DONE - except better design needed
@app.route("/feed")
def feed():
    if session.get("username"):
        articles = API_funcs.get_headlines("business")
        urls = API_funcs.get_URLS("business")
        #print articles
        return render_template("feed.html", headline=articles[0], headlinet=articles[1], headlineth=articles[2], u1 = urls[0], u2 = urls[1], u3 = urls[2])
    else:
        return render_template("home.html", message="Please log in to access your feed.", warning=True)

# Status: DONE
@app.route("/leaderboard")
def leaderboard():
    leaderboard = transactions.get_leaderboard()
    #print "LEADER: ", leaderboard
    return render_template("leaderboard.html", leaders_list = leaderboard)

# Status: Unknown
@app.route("/transaction")
def transaction():
    return render_template("transaction.html")

# Status: Unknown
@app.route("/transact", methods=['POST'])
def transact():
    name = request.form["searched_stock_name"]
    price = request.form["searched_stock_price"]
    num_stock = request.form["num_stock"]
    name = name.split(" ")
    price = price.split(" ")
    name = name[1]
    price = price[1]
    #print name
    #print price
    #print num_stock
    worked = transactions.buy(session.get("username"), name, num_stock, price)
    if(worked > 0):
        return render_template("account.html", message="Bought stock!", good=True)
    else:
        return render_template("account.html", message="Sorry, looks like you have insufficient funds to complete this transaction.", good=False)

# Status: Unknown
@app.route("/get_stock_price", methods=['POST'])
def get_stock_price():
    stock_name = request.form["stock"]
    stock_price = transactions.getStockPrice(stock_name)
    high = transactions.getHigh(stock_name)
    low = transactions.getLow(stock_name)
    #print "NAME: " + stock_name
    #print "PRICE: " + str(stock_price)
    to_ret = json.dumps({'status':'OK', 'name':stock_name, 'price': stock_price, 'high': high, 'low':low})
    #print to_ret
    return to_ret

# Status: Incomplete
@app.route("/confirmation")
def confirmation():
    return render_template("stats.html", message="Congratulations! Your transaction was successful! You may be one step closer to becoming rich!", good=True)

# Status: Incomplete
@app.route("/logout",methods=['POST','GET'])
def logout():
    if 'username' in session:
        session.pop('username')
        return render_template('home.html', message = 'Logout was successful.', good = True)
    else:
        return redirect("/")

if __name__ == "__main__":
    app.debug = True
    app.run()
