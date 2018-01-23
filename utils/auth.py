import data_builder # Caution: When this is imported, the test functions in this .py file are run as well.

def login(username, password):
    users = data_builder.getUsers()
    # checks credentials for login
    if username in users:
        if password == users[username]:
            session['username'] = username
            return redirect(url_for('feed'))
        else:
            flash("Bad password")
            return redirect(url_for('signup_page'))
    else:
        flash("Bad username")
        return redirect(url_for('authentication'))
