# Team CYES
# Samantha Ngo, Carol Pan, Eugene Thomas, Yuyang Zhang
# SoftDev1 pd7
# P01 -- ArRESTed Development
# 2017-11-16

from flask import Flask, render_template, request
from flask import redirect, flash, url_for
from util import api_calls as api

app = Flask (__name__)

#home route, takes zipcode and other inputs
@app.route("/")
def hello_world():
    print "**DIAG: has api key been acquired?**"

    '''will figure out how to display keys at later date'''
    return render_template("base.html")

#reach out to apis and acquire info
@app.route("/info")
def display_info():
    #retrieving the name
    name=request.args["name"]
    #retrieving weather data
    zipcode=request.args["zipcode"]
    #code for api call have been moved to util/api_calls.py
    wform = api.weathercall(zipcode)
    #retrieving book data
    age=request.args["age"]
    #code for api call have been moved to util/api_calls.py
    bform = api.bookcall(age)

    return render_template("info.html", name=name, bookdata=bform, weatherdata=wform)

if __name__ == "__main__":
    app.debug = True
    app.run()
