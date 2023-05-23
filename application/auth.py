from flask import Blueprint,session
from flask import render_template,request,redirect,flash,url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from flask_session import Session

from application import db,User

auth = Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = db.users.find_one({'email': email})
        if user and check_password_hash(user['password'], password):
            flash('Logged in successfully.', category='success')
            # login_user(User(username), remember=True)
            session["email"] = email
            login_user(User(user["_id"]), remember=True)


            return render_template('index.html')
        else:
            flash('Invalid username or password.',category='error')
            return redirect(url_for('auth.login'))
    else:
        return render_template('login.html', User=current_user)
    



@auth.route('/signup',methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        # hashed_password = bcrypt.hashpw(password1.encode('utf-8'), bcrypt.gensalt())
    

        
        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(username) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        elif db.users.find_one({'email': email}) :
            flash('Username already exists.',  category='error')
        else:
            hashed_password = generate_password_hash(password1)




            

            db.users.insert_one({'email':email,'username': username, 'password':  hashed_password})
            flash('Account created!',category='success')
            # login_user(User(username), remember=True)


            return redirect(url_for('auth.login'))
       
    return render_template("signup.html", User=current_user)
    
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    session.pop("email", None) 
    return redirect(url_for('auth.login'))   

   
