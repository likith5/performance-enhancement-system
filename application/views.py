from application import create_app
from flask import Blueprint,url_for,session,flash
from flask_session import Session
from application import db
from pymongo.errors import PyMongoError
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

@views.route("/marksenter",methods=['GET','POST'])
def marksenter():
    
    studentname = session.get('studentname')
    title="marks enter"
    if  'teacheremail' in session:

        if request.method == 'POST':

                communication= request.form.get('communication')
                technical= request.form.get('technical')
                creativity= request.form.get('creativity')
                projectmmt= request.form.get('projectmmt')
                timemanagement= request.form.get('timemanagement')
                generalknowledge= request.form.get('generalknowledge')
                interpersonal= request.form.get('interpersonal')
                resultoriented= request.form.get('resultoriented')
                leardership= request.form.get('leardership')
                presentation= request.form.get('presentation')
                # print(leardership)
                # print(presentation)
                # print(studentname)
                # print(communication)

                # user = db.users.find_one({'username':username })
                # email = user['email']
                # db.marks.insert_one({"communication": communication})
                try:

                    db.users.update_one(
                    {"username": studentname},
                    {
                        "$set": {
                            "marks": {
                                "communication": communication,
                                "technical": technical,
                                "creativity": creativity,
                                "projectmmt": projectmmt,
                                "timemanagement": timemanagement,
                                "generalknowledge": generalknowledge,
                                "interpersonal": interpersonal,
                                "resultoriented": resultoriented,
                                "leardership": leardership,
                                "presentation": presentation
                            }
                        }
                    }
                )
                    flash('Marks entered successfully', category='success')
                    return redirect(url_for('views.dashboard'))
                except PyMongoError as e:
                    flash(f'Error: {str(e)}', category='error')
                # Handle the error accordingly, such as logging it or displaying an error message to the user
                    return redirect(url_for('views.marksenter'))
                
        
        # print(studentname)
        # return render_template("marksenter.html",title=title,studentname=studentname)
        return render_template("marksenter.html")
    return redirect(url_for('auth.login'))


@views.route("/dashboard")
def dashboard():
    if 'studentemail' in session :
        # def converttorange(grade):
        #     if grade == 1:
        #         percentage = 20
        #     elif grade == 2:
        #         percentage = 40
        #     elif grade == 3:
        #         percentage = 60
        #     elif grade == 4:
        #         percentage = 80
        #     elif grade == 5:
        #         percentage = 100
        #     else:
        #         percentage = 29
            
           
        #     return percentage
        
        name = session.get("studentemail")
        print(name)
        user = db.users.find_one({'email':name })
        studname = user['username']
        communication = int(user['marks'].get('communication'))
        technical = int(user["marks"].get('technical'))
        creativity = int(user['marks'].get('creativity'))
        projectmm = int(user['marks'].get('projectmmt'))
        timemanagement = int(user['marks'].get('timemanagement'))
        generalknowledge = int(user['marks'].get('generalknowledge'))
        interpersonal = int(user['marks'].get('interpersonal'))
        resultoriented = int(user['marks'].get('resultoriented'))
        leardership = int(user['marks'].get('leardership'))
        presentation = int(user['marks'].get('presentation'))
        print(communication)

        # communication = converttorange(communication)
        # creativity = converttorange(creativity)
        # technical = converttorange(technical)
        # projectmm = converttorange(projectmm)
        # timemanagement = converttorange(timemanagement)
        # generalknowledge = converttorange(generalknowledge)
        # interpersonal = converttorange(interpersonal)
        # resultoriented = converttorange(resultoriented)
        # leardership = converttorange(leardership)
        # presentation = converttorange(presentation)
        


        
      


        title="dashboard"
        return render_template('dashboard.html',title=title,studname=studname,creativity=creativity,communication=communication,technical=technical,projectmm=projectmm,timemanagement=timemanagement,generalknowledge=generalknowledge,interpersonal=interpersonal,resultoriented=resultoriented,leardership=leardership,presentation=presentation)
    # return redirect(url_for('auth.login'))
    elif  'teacheremail' in session :
        # def converttorange(grade):
        #     if grade == 1:
        #         percentage = 20
        #     elif grade == 2:
        #         percentage = 40
        #     elif grade == 3:
        #         percentage = 60
        #     elif grade == 4:
        #         percentage = 80
        #     elif grade == 5:
        #         percentage = 100
        #     else:
        #         percentage = None
            
           
        #     return percentage
        
        studentname = session.get("studentname")
        studname=studentname
        print(studentname)
        user = db.users.find_one({'username':studentname })
        # communicat = user['marks'].get('communication')
        communication = int(user['marks'].get('communication'))
        technical = int(user["marks"].get('technical'))
        creativity = int(user['marks'].get('creativity'))
        projectmm = int(user['marks'].get('projectmmt'))
        timemanagement = int(user['marks'].get('timemanagement'))
        generalknowledge = int(user['marks'].get('generalknowledge'))
        interpersonal = int(user['marks'].get('interpersonal'))
        resultoriented = int(user['marks'].get('resultoriented'))
        leardership = int(user['marks'].get('leardership'))
        presentation = int(user['marks'].get('presentation'))

        # communications = converttorange(communication)
        # creativity = converttorange(creativity)
        # technical = converttorange(technical)
        # projectmm = converttorange(projectmm)
        # timemanagement = converttorange(timemanagement)
        # generalknowledge = converttorange(generalknowledge)
        # interpersonal = converttorange(interpersonal)
        # resultoriented = converttorange(resultoriented)
        # leardership = converttorange(leardership)
        # presentation = converttorange(presentation)
        # print(communications)
        


        
      


        title="dashboard"
        return render_template('dashboard.html',studname=studname,title=title,creativity=creativity,communication=communication,technical=technical,projectmm=projectmm,timemanagement=timemanagement,generalknowledge=generalknowledge,interpersonal=interpersonal,resultoriented=resultoriented,leardership=leardership,presentation=presentation)
    return redirect(url_for('auth.login'))

@views.route("/search",methods=['GET','POST'])
def search():
    if 'teacheremail' in session:
        username = request.form.get('username')
        usn = request.form.get('usn')

        if request.method == 'POST':
            college = request.form.get('college')
            username = request.form.get('username')
            usn = request.form.get('usn')
        
            accademicyear = request.form.get('accademicyear')
            user = db.users.find_one({'username':username })
            # user = db.users.find_one({'email':name })
            # studname = user['username']

            # print(email)
            if user:
                session["studentname"] = username
                # bro = session.get['studentname']
                flash('User found Kindly enter the marks ', category='success')
                return redirect(url_for('views.marksenter'))
                # return render_template('marksenter.html',usn=usn,usernames=username)
            else:
                flash('User not found', category='error')
                return redirect(url_for('views.search'))
                # return render_template('dashboard.html',title=title,name=name)   
        return render_template('search.html',usn=usn,username=username)
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

