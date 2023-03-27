from application import app
from flask import render_template,request,redirect

@app.route("/")
def welcome():
    title="login"
    return render_template("loginpage.html",title=title)