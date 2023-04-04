from application import app
from flask import render_template,request,redirect

@app.route("/")
def welcome():
    title="index"
    return render_template("index.html",title=title)

@app.route("/login")
def login():

    title="login"
    return render_template("login.html",title=title)
@app.route("/signup")
def signup():

    title="signup"
    return render_template("signup.html",title=title)

@app.route("/search")
def search():

    title="search"
    return render_template("search.html",title=title)
@app.route("/searchfeature")
def searchfeature():

    title="search"
    return render_template("searchfeature.html",title=title)