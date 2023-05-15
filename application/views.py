from application import create_app
from flask import Blueprint
from flask_login import login_required, current_user

from flask import render_template,request,redirect
views = Blueprint('views',__name__)


@login_required
@views.route("/")
def index():
    title="index"
    return render_template("index.html",title=title)

@login_required
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

