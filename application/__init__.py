from flask import Flask, session
from flask_pymongo import PyMongo
from pymongo.mongo_client import MongoClient
from flask_login import LoginManager,UserMixin, login_user, login_required, logout_user
from flask_session import Session



uri="mongodb+srv://likith:likilikiliki@pme.wntysf4.mongodb.net/"
client = MongoClient(uri,connect=False)
db = client.pme

# flask login-setup
class User(UserMixin):

    def __init__(self, user_id):
        self.id = user_id

    @staticmethod
    def get(user_id):
        user_data = db.users.find_one({'_id': user_id})
        if not user_data:
            return None
        return User(user_data['_id'])




def create_app():
    app =Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)
    # app.config['MONGO_URI'] = 'mongodb+srv://likith:likilikiliki@pme.wntysf4.mongodb.net/'
    # client = MongoClient(MONGO_URI,connect=False)
    
    

    from .views import views
    from .auth import auth
   
    # db.init_app(app)
   
    
    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)

   
    # user_dict = db.users.find_one({'_id': ObjectId(user_id)})
    # return User(user_dict) if user_dict else None
   
    


    
   

    return app



