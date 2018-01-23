import data_builder # Caution: When this is imported, the test functions in this .py file are run as well.
from flask import flash, redirect, url_for, session

def login(username, password):
    users = data_builder.getUsers()
    # checks credentials for login
    if username in users:
        if password == users[username]:
            session['username'] = username
            return redirect(url_for('feed'))
        else:
            return redirect("login.html", msg = "Oops! Wrong password.", good = False)
    else:
        flash("Bad username")
        return redirect('/login')

def create_account(username, password, level):
    users = data_builder.getUsers()
    if username in users:
        flash("Username already taken.")
        return redirect("/create_account")
    else:
        return render_template("signup.html")
