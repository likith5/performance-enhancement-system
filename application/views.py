from application import create_app
from flask import Blueprint,url_for,session
from flask_session import Session

from flask import render_template,request,redirect
views = Blueprint('views',__name__)


@views.route("/")

def index():
    if 'email' in session:
        return redirect(url_for('views.dashboard'))
    return redirect(url_for('auth.login'))
    

    
    return render_template('index.html')
@views.route("/profile")
def profile():

    title="profile"
    return render_template("profile.html",title=title)

@views.route("/dashboard")
def dashboard():
    if 'email' in session:
         name = session.get("email")
         title="dashboard"
         return render_template('dashboard.html',title=title,name=name)
    return redirect(url_for('auth.login'))



















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

