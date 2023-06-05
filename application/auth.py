from flask import Blueprint,session
from flask import render_template,request,redirect,flash,url_for
from werkzeug.security import generate_password_hash, check_password_hash
import bcrypt
from application import db
# ,User  this has been excluded from above statement

auth = Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = db.users.find_one({'email': email})
        teacher = db.teacher.find_one({'email': email})
        if user and check_password_hash(user['password'], password):
            
            
            marks = user.get('marks')
            if marks is not None :
                flash('Logged in successfully.', category='success')
                session["studentemail"] = email

                # return render_template('dashboard.html')
                return redirect(url_for('views.dashboard'))
            else:
                flash('marks has not been given yet',category='error')
                return redirect(url_for('auth.login'))

        if teacher and check_password_hash(teacher['password'], password):
            flash('Logged in successfully.', category='success')
            
            session["teacheremail"] = email


            # return render_template('search.html')
            return redirect(url_for('views.search'))
        else:
            flash('Invalid username or password.',category='error')
            return redirect(url_for('auth.login'))
    else:
        return render_template('login.html')
    



@auth.route('/signup',methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        role = request.form.get('role')

        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        hashed_password = bcrypt.hashpw(password1.encode('utf-8'), bcrypt.gensalt())
    

        
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
        elif role == 'student':
            hashed_password = generate_password_hash(password1)

            db.users.insert_one({'email':email,'role':role,'username': username, 'password':  hashed_password})
            flash('Account created!',category='success')
            return redirect(url_for('auth.login'))
        elif role == 'teacher':
            hashed_password = generate_password_hash(password1)

            db.teacher.insert_one({'email':email,'username': username, 'password':  hashed_password})
            flash('Account created!',category='success')
            return redirect(url_for('auth.login'))
       
    return render_template("signup.html")
    
@auth.route('/logout')
def logout():
    session.pop("studentname",None) 
    session.pop("studentemail",None) 
    session.pop("teacheremail", None) 
    return redirect(url_for('auth.login'))   

   
