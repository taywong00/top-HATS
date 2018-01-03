# Team top_HATS
# Holden Higgins, Adam Abbas, Taylor Wong, Samantha Ngo
# SoftDev1 pd7
# P0# --
# 2018-01-02

from flask import Flask, render_template, request
from flask import redirect, flash, url_for
import API_funcs
#from util import

app = Flask (__name__)


# HOMEPAGE: brief description and two buttons--"Login" or "Create an account"
@app.route("/")
def homepage():
    return render_template("home.html");

# LOGIN: name of product/logo and then "Username:", "Password:", and "Don't have an account? <CREATE hyperlink> one."
@app.route("/login")
def login():
    return render_template("login.html");

if __name__ == "__main__":
    app.debug = True
    app.run()
