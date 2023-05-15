from flask import Flask
from flask_pymongo import PyMongo
from pymongo.mongo_client import MongoClient
from flask_login import LoginManager

uri="mongodb+srv://likith:likilikiliki@pme.wntysf4.mongodb.net/"
client = MongoClient(uri,connect=False)
db = client.pme
users = db['users']
todos = db['todos']
def create_app():
    app =Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    # app.config['MONGO_URI'] = 'mongodb+srv://likith:likilikiliki@pme.wntysf4.mongodb.net/'
    # client = MongoClient(MONGO_URI,connect=False)
    
    # db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        user_dict = db.users.find_one({'_id': ObjectId(user_id)})
        return User(user_dict) if user_dict else None
   

    return app



