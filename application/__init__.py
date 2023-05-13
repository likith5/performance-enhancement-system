from flask import Flask
from flask_pymongo import PyMongo
from pymongo.mongo_client import MongoClient


# uri="mongodb+srv://likith:likilikiliki@pme.wntysf4.mongodb.net/"
client = MongoClient(uri,connect=False)
db = client.pme
users = db['users']
todos = db['todos']
def create_app():
    app =Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['MONGO_URI'] = 'mongodb+srv://likith:likilikiliki@pme.wntysf4.mongodb.net/'
    db.init_app(app)
    from .views import views
    from .auth import auth

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')
    return app



