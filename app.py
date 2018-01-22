# Team top_HATS
# Holden Higgins, Adam Abbas, Taylor Wong, Samantha Ngo
# SoftDev1 pd7
# P0# --
# 2018-01-02

import os
from flask import Flask, render_template, request, session
from flask import redirect, flash, url_for
import API_funcs #API calls
import auth
#from util import

app = Flask (__name__)
app.secret_key = os.urandom(32)

# HOMEPAGE: brief description and two buttons--"Login" or "Create an account"
@app.route("/")
def home():
    if session.get('username'):
        print session.get("username")
    return render_template("home.html")

# Status: Incomplete
# LOGIN: name of product/logo and then "Username:", "Password:", and "Don't have an account? <CREATE hyperlink> one."
@app.route('/login', methods=['GET', 'POST'])
def login():
    # if user already logged in, redirect to homepage(base.html)
    if session.get('username'):
        return redirect('base')
    # user entered login form
    else:
        return render_template('login.html')

@app.route("/authorize", methods=['GET', 'POST'])
def authorize():
    all_users = auth.get_users()
    if request.form["username"] in all_users:
        if request.form["password"] == all_users[request.form["username"]]:
            session['username'] = request.form['username'];
            flash("Login successful!")
            return redirect('/');
        else:
            print "PASSWRONG"
            flash("Incorrect password!")
            return redirect(url_for("login"))
    else:
        print "USER DNE"
        flash("User does not exist!")
        return redirect(url_for("login"))

@app.route("/signup_page")
def signup_page():
	if session.get("username"):
		return "Please log out before creating a new account."
	else:
		return render_template('signup.html')

# Status: Incomplete
# LOGIN: name of product/logo and then "Username:", "Password:", and "Don't have an account? <CREATE hyperlink> one."
@app.route("/create_account", methods=['GET', 'POST'])
def create_account():
    # If the user is already logged in:
    if session.get('username'):
        # If the user is logged in, they should not be able to access this page in the first place.
        return redirect('home')
    # If the user clicks Create Account
	print "INFORMATION: ", request.form.get("create_account")
#        print "Username:", request.form.get("username")
#        print "password:", request.form.get("password")
#        print "medium:", request.form.get("medium")
#        print "hard:", request.form.get("hard")

    auth.create_user(request.form.get("username"), request.form.get("password"))
	#if request.form.get("hard") == 'on':
		#level = "hard"
	#elif request.form.get("medium") == 'on':
	#	level = 'medium'
	#else:
		#level = 'easy'
    return redirect('/')
#else:
 #   return render_template("signup.html")

# Status: DONE
@app.route("/how_to", methods=['GET', 'POST'])
def how_to():
    return render_template("how_to.html")
# -------------

# Status: Incomplete
@app.route("/account", methods=['GET', 'POST'])
def account():
    if session.get('username'):
        return render_template("account.html", name = session.get('username'))
    flash("Please log in to see your account")
    return redirect("/")

# Status: Incomplete
@app.route("/feed")
def feed():
    articles = API_funcs.get_headlines("business")
    urls = API_funcs.get_URLS("business")
    print articles
    return render_template("feed.html", headline=articles[0], headlinet=articles[1], headlineth=articles[2], u1 = urls[0], u2 = urls[1], u3 = urls[2])

# Status: Incomplete
@app.route("/stats")
def stats():
    return render_template("stats.html")

# Status: Incomplete
@app.route("/leaderboard")
def leaderboard():
    return render_template("leaderboard.html")

# Status: Incomplete
@app.route("/transaction")
def transaction():
    return render_template("transaction.html")

# Status: Incomplete
@app.route("/confirmation")
def confirmation():
    return render_template("stats.html", message="Congratulations! Your transaction was successful! You're one step closer to becoming rich!", good=True)

# Status: Incomplete
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
