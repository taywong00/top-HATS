# Team top_HATS
# Holden Higgins, Adam Abbas, Taylor Wong, Samantha Ngo
# SoftDev1 pd7
# P0# --
# 2018-01-02

import os
from flask import Flask, render_template, request, session
from flask import redirect, flash, url_for
import API_funcs #API calls
#from util import

app = Flask (__name__)
app.secret_key = os.urandom(32)


# HOMEPAGE: brief description and two buttons--"Login" or "Create an account"
@app.route("/")
def homepage():
    return render_template("home.html")

# LOGIN: name of product/logo and then "Username:", "Password:", and "Don't have an account? <CREATE hyperlink> one."
@app.route('/login', methods=['GET', 'POST'])
def login():
    # if user already logged in, redirect to homepage(base.html)
    if session.get('username'):
        return redirect('base')
    # user entered login form
    elif request.form.get('login'):
        print "login"
        return auth.login()
    # user didn't enter form
    else:
        return render_template('login.html')

# LOGIN: name of product/logo and then "Username:", "Password:", and "Don't have an account? <CREATE hyperlink> one."
@app.route("/create_account", methods=['GET', 'POST'])
def create_account():
    if session.get('username'):
        return redirect('homepage')
    # user entered signup form
    elif request.form.get('signup'):
        return auth.signup()
    else:
        return render_template("signup.html")

@app.route("/how_to", methods=['GET', 'POST'])
def how_to():
    return render_template("how_to.html")

@app.route("/account", methods=['GET', 'POST'])
def account():
    return render_template("account.html")

@app.route("/feed")
def feed():
    return render_template("feed.html")

@app.route("/stats")
def stats():
    return render_template("stats.html")

@app.route("/leaderboard")
def leaderboard():
    return render_template("leaderboard.html")

@app.route("/transaction")
def transaction():
    return render_template("transaction.html")

@app.route("/confirmation")
def confirmation():
    return render_template("stats.html", message="Congratulations! Your transaction was successful! You're one step closer to becoming rich!", good=True)

@app.route("/logout",methods=['POST','GET'])
def logout():
    if 'username' not in session:
        redirect("/")

    #code from my last project LOL - pm
    #accounts = db_functions.accounts_dict()
    #stories = db_functions.stories_dict()

    #remove user info from session
    if 'username' in session:
        session.pop('username')
    return render_template('home.html', message = 'Logout was successful.', good = True)


if __name__ == "__main__":
    app.debug = True
    app.run()
