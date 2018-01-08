# Team top_HATS
# Holden Higgins, Adam Abbas, Taylor Wong, Samantha Ngo
# SoftDev1 pd7
# P0# --
# 2018-01-02

from flask import Flask, render_template, request, session
from flask import redirect, flash, url_for
import os
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
        return render_template("register.html")

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
    return render_template("confirmation.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
