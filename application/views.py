from application import create_app
from flask import Blueprint,url_for,session
from flask_login import login_required, current_user
from flask_session import Session

from flask import render_template,request,redirect
views = Blueprint('views',__name__)


@views.route("/")
@login_required
def index():
    name = session.get("email")

    
    return render_template('index.html',User=current_user,name=name)
@views.route("/profile")
def profile():

    title="profile"
    return render_template("profile.html",title=title)


















# @app.route("/search")
# def search():

#     title="search"
#     return render_template("search.html",title=title)
# @app.route("/searchfeature")
# def searchfeature():

#     title="search feature"
#     return render_template("searchfeature.html",title=title)

# @app.route("/extractedfeature")
# def extractedfeature():

#     title="extracted feature"
#     return render_template("extractedfeature.html",title=title)

