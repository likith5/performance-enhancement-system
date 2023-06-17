from application import create_app
from flask import Blueprint,url_for,session,flash,make_response
from flask_session import Session
from application import db
from pymongo.errors import PyMongoError
from flask import render_template,request,redirect
from bson.binary import Binary
import csv
from io import StringIO

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
    if  'teacheremail' in session:
        usn = session.get('studentname')
        user = db.users.find_one({'usn':usn })
        username = user["personal"].get('username')
        email = user["personal"].get('email')
        college = user["personal"].get('college')
        sem = user["personal"].get('sem')
        linkdin = user["personal"].get('linkdin')
        github = user["personal"].get('github')
        project1 = user["personal"].get('project-1')
        intership1 = user["personal"].get('internship-1')
        interst1 = user["personal"].get('interst-1')
        title="dashboard"
        return render_template('profile.html',title=title,usn=usn,username=username,email=email,college=college,sem=sem,linkdin=linkdin,github=github,intership1=intership1,project1=project1,interst1=interst1)
   
    if 'studentemail' in session :
        usn = session.get('studentemail')
        user = db.users.find_one({'usn':usn })
        username = user["personal"].get('username')
        email = user["personal"].get('email')
        college = user["personal"].get('college')
        sem = user["personal"].get('sem')
        linkdin = user["personal"].get('linkdin')
        github = user["personal"].get('github')
        project1 = user["personal"].get('project-1')
        intership1 = user["personal"].get('internship-1')
        interst1 = user["personal"].get('interst-1')
        title="dashboard"
        return render_template('profile.html',title=title,usn=usn,username=username,email=email,college=college,sem=sem,linkdin=linkdin,github=github,intership1=intership1,project1=project1,interst1=interst1)
 


    flash('Please login in to view profile', category='error')

    return redirect(url_for('auth.login'))

@views.route("/marksenter",methods=['GET','POST'])
def marksenter():
    
    usn = session.get('studentname')
    user = db.users.find_one({'usn':usn })
    username = user["personal"].get('username')

    title="marks enter"
    if  'teacheremail' in session:

        if request.method == 'POST':

                test= request.form.get('test')
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
                if test == "Test1":
                    try:

                        db.users.update_one(
                        {"usn": usn},
                        {
                            "$set": {
                                "test1": {
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
                if test == "Test2":
                    try:

                        db.users.update_one(
                        {"usn": usn},
                        {
                            "$set": {
                                "test2": {
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
                if test == "Test3":
                    try:

                        db.users.update_one(
                        {"usn": usn},
                        {
                            "$set": {
                                "test3": {
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
        return render_template("marksenter.html",usn=usn,username=username)
    return redirect(url_for('auth.login'))


@views.route("/dashboard",methods=['GET','POST'])
def dashboard():
    if 'studentemail' in session :
       
        usn = session.get("studentemail")
        user = db.users.find_one({'usn':usn })
        username = user["personal"].get('username')
        title="dashboard"
        

        
        if request.method=="POST":
            man= request.form.get('test')
            test =man.lower()
            title="dashboard"
            usn = session.get("studentemail")
            user = db.users.find_one({'usn':usn })
            username = user["personal"].get('username')

            print(test)
            if test=="test1":
             
                communication = int(user['test1'].get('communication'))
                technical = int(user["test1"].get('technical'))
                creativity = int(user['test1'].get('creativity'))
                projectmm = int(user['test1'].get('projectmmt'))
                timemanagement = int(user['test1'].get('timemanagement'))
                generalknowledge = int(user['test1'].get('generalknowledge'))
                interpersonal = int(user['test1'].get('interpersonal'))
                resultoriented = int(user['test1'].get('resultoriented'))
                leardership = int(user['test1'].get('leardership'))
                presentation = int(user['test1'].get('presentation'))
                return render_template('dashboard.html',username=username,title=title,creativity=creativity,communication=communication,technical=technical,projectmm=projectmm,timemanagement=timemanagement,generalknowledge=generalknowledge,interpersonal=interpersonal,resultoriented=resultoriented,leardership=leardership,presentation=presentation)

                # redirect(url_for('views.dashboard'))
            if test=="test2":
               
                communication = int(user['test2'].get('communication'))
                technical = int(user["test2"].get('technical'))
                creativity = int(user['test2'].get('creativity'))
                projectmm = int(user['test2'].get('projectmmt'))
                timemanagement = int(user['test2'].get('timemanagement'))
                generalknowledge = int(user['test2'].get('generalknowledge'))
                interpersonal = int(user['test2'].get('interpersonal'))
                resultoriented = int(user['test2'].get('resultoriented'))
                leardership = int(user['test2'].get('leardership'))
                presentation = int(user['test2'].get('presentation'))
                return render_template('dashboard.html',username=username,title=title,creativity=creativity,communication=communication,technical=technical,projectmm=projectmm,timemanagement=timemanagement,generalknowledge=generalknowledge,interpersonal=interpersonal,resultoriented=resultoriented,leardership=leardership,presentation=presentation)
            if test=="test3":
               
                communication = int(user['test3'].get('communication'))
                technical = int(user["test3"].get('technical'))
                creativity = int(user['test3'].get('creativity'))
                projectmm = int(user['test3'].get('projectmmt'))
                timemanagement = int(user['test3'].get('timemanagement'))
                generalknowledge = int(user['test3'].get('generalknowledge'))
                interpersonal = int(user['test3'].get('interpersonal'))
                resultoriented = int(user['test3'].get('resultoriented'))
                leardership = int(user['test3'].get('leardership'))
                presentation = int(user['test3'].get('presentation'))
                return render_template('dashboard.html',username=username,title=title,creativity=creativity,communication=communication,technical=technical,projectmm=projectmm,timemanagement=timemanagement,generalknowledge=generalknowledge,interpersonal=interpersonal,resultoriented=resultoriented,leardership=leardership,presentation=presentation)

        # communication = int(user['marks'].get('communication'))
        # technical = int(user["marks"].get('technical'))
        # creativity = int(user['marks'].get('creativity'))
        # projectmm = int(user['marks'].get('projectmmt'))
        # timemanagement = int(user['marks'].get('timemanagement'))
        # generalknowledge = int(user['marks'].get('generalknowledge'))
        # interpersonal = int(user['marks'].get('interpersonal'))
        # resultoriented = int(user['marks'].get('resultoriented'))
        # leardership = int(user['marks'].get('leardership'))
        # presentation = int(user['marks'].get('presentation'))
        # print(communication)

        


        
      


        title="dashboard"
        return render_template('dashboard.html')
    # return redirect(url_for('auth.login'))
    elif  'teacheremail' in session :
        title="dashboard"
        usn = session.get("studentname")
        user = db.users.find_one({'usn':usn })
        username = user["personal"].get('username')

        
        if request.method=="POST":
            man= request.form.get('test')
            test =man.lower()
            title="dashboard"
            usn = session.get("studentname")
            user = db.users.find_one({'usn':usn })
            username = user["personal"].get('username')

            print(test)
            if test=="test1":
             
                communication = int(user['test1'].get('communication'))
                technical = int(user["test1"].get('technical'))
                creativity = int(user['test1'].get('creativity'))
                projectmm = int(user['test1'].get('projectmmt'))
                timemanagement = int(user['test1'].get('timemanagement'))
                generalknowledge = int(user['test1'].get('generalknowledge'))
                interpersonal = int(user['test1'].get('interpersonal'))
                resultoriented = int(user['test1'].get('resultoriented'))
                leardership = int(user['test1'].get('leardership'))
                presentation = int(user['test1'].get('presentation'))
                return render_template('dashboard.html',username=username,title=title,creativity=creativity,communication=communication,technical=technical,projectmm=projectmm,timemanagement=timemanagement,generalknowledge=generalknowledge,interpersonal=interpersonal,resultoriented=resultoriented,leardership=leardership,presentation=presentation)

                # redirect(url_for('views.dashboard'))
            if test=="test2":
               
                communication = int(user['test2'].get('communication'))
                technical = int(user["test2"].get('technical'))
                creativity = int(user['test2'].get('creativity'))
                projectmm = int(user['test2'].get('projectmmt'))
                timemanagement = int(user['test2'].get('timemanagement'))
                generalknowledge = int(user['test2'].get('generalknowledge'))
                interpersonal = int(user['test2'].get('interpersonal'))
                resultoriented = int(user['test2'].get('resultoriented'))
                leardership = int(user['test2'].get('leardership'))
                presentation = int(user['test2'].get('presentation'))
                return render_template('dashboard.html',username=username,title=title,creativity=creativity,communication=communication,technical=technical,projectmm=projectmm,timemanagement=timemanagement,generalknowledge=generalknowledge,interpersonal=interpersonal,resultoriented=resultoriented,leardership=leardership,presentation=presentation)
            if test=="test3":
               
                communication = int(user['test3'].get('communication'))
                technical = int(user["test3"].get('technical'))
                creativity = int(user['test3'].get('creativity'))
                projectmm = int(user['test3'].get('projectmmt'))
                timemanagement = int(user['test3'].get('timemanagement'))
                generalknowledge = int(user['test3'].get('generalknowledge'))
                interpersonal = int(user['test3'].get('interpersonal'))
                resultoriented = int(user['test3'].get('resultoriented'))
                leardership = int(user['test3'].get('leardership'))
                presentation = int(user['test3'].get('presentation'))
                return render_template('dashboard.html',username=username,title=title,creativity=creativity,communication=communication,technical=technical,projectmm=projectmm,timemanagement=timemanagement,generalknowledge=generalknowledge,interpersonal=interpersonal,resultoriented=resultoriented,leardership=leardership,presentation=presentation)

       
        
        

        communicat = user['marks'].get('communication')
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

       
        
      


        
        return render_template('dashboard.html')
                # return render_template('dashboard.html')
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
            user = db.users.find_one({'usn':usn })
            # user = db.users.find_one({'email':name })
            # studname = user['username']

            # print(email)
            if user:
                session["studentname"] = usn
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

# @views.route('/userdata',methods=['GET','POST'])    
# def userdata():
    
#     return render_template('userdata.html')

     
@views.route('/userdata',methods=['GET','POST'])    
def userdata():
    if  "studentemail" in session:
        if request.method == "POST":
            usn = session.get("studentemail")

            username= request.form.get('username')
            email = request.form.get('email')
            college = request.form.get('college')
            sem= request.form.get('sem')
            linkdin= request.form.get('linkdin')
            github= request.form.get('github')
            internship1= request.form.get('i-1')
            project1= request.form.get('p-1')
            interst1= request.form.get('intrest-1')
            file = request.files['resume']
            file_data = file.read()
            binary_data = Binary(file_data)

            try:
                db.users.update_one(
                        {"usn": usn},
                        {
                            "$set": {
                                "personal": {
                                    "username": username,
                                    "email": email,
                                    "college": college,
                                    " sem":  sem,
                                    "linkdin": linkdin,
                                    "github": github,
                                    "internship-1": internship1,
                                    "project-1": project1,
                                    "interst-1": interst1,
                                    "resume":binary_data,
                                }
                            }
                        }
                    )
                flash('details have been entered please login again', category='success')
                return redirect(url_for('auth.login'))
            except PyMongoError as e:
                flash(f'Error: {str(e)}', category='error')
                    # Handle the error accordingly, such as logging it or displaying an error message to the user
                return redirect(url_for('views.marksenter'))
        # usn = session.get('studentemail')
        # user = db.users.find_one({'usn':usn })
        # username = user["personal"].get('username')
        # email = user["personal"].get('email')
        # college = user["personal"].get('college')
        # sem = user["personal"].get('sem')
        # linkdin = user["personal"].get('linkdin')
        # github = user["personal"].get('github')
        # project1 = user["personal"].get('project-1')
        # intership1 = user["personal"].get('internship-1')
        # interst1 = user["personal"].get('interst-1')
        # title="Account"

                        
                    

        return render_template('userdata.html')
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

# @views.route('/download_csv')
# def download_csv():
#     # Connect to MongoDB
 

#     # Fetch data from MongoDB
#     data = db.users.find()

#     # Create a CSV file
#     csv_data = [['slno', 'username', 'skill1']]  # Replace with your field names
    
#     for item in data:
#         print(item['password'])
#         csv_data.append([item['password'], item['usn'], item['role']])  # Replace with your field names
        
        

#     # Create a response with CSV data
#     response = make_response()
#     response.headers['Content-Disposition'] = 'attachment; filename=data.csv'
#     # csv_data = StringIO()
#     writer = csv.writer(csv_data)
#     writer.writerows(csv_data)

#     return response

@views.route('/download_csv')
def download_csv():
    # Connect to MongoDB
 
    data = db.users.find()

    # Create CSV headers
    # Get all unique test skills
    unique_skills = set()
    for item in data:
        test1 = item.get('test1', {})
        print(test1.values())
        unique_skills.update(test1.keys())

    # Sort the unique skills alphabetically
    sorted_skills = sorted(unique_skills - {'communication', 'presentation', 'technical'})

    # Create CSV headers
    csv_headers = ['Serial Number', 'Username','', 'Communication', 'Presentation', 'Technical'] + sorted_skills

    # Create CSV rows
    csv_rows = []
    serial_number = 1
    for item in data:
        usn = item['usn']
        test11 = item.get('test1', {})
        test1 =test11.values()

        username = item.get('personal', {}).get('username', '')
        communication = item.get('test1', {}).get(('communication', ''),('technical', ''))
        presentation = item.get('test1', {}).get('presentation', '')
        technical = item.get('test1', {}).get('technical', '')
        test_marks = [item.get('test1', {}).get(skill, '') for skill in sorted_skills]
        csv_row = ['','', 'test1', test2_marks, test3_marks]

        csv_row = [serial_number, username, communication, presentation, technical] + test_marks
        csv_rows.append(test1)
        serial_number += 1

    # Create a response with CSV data
    response = make_response()
    response.headers['Content-Disposition'] = 'attachment; filename=data.csv'
    response.mimetype = 'text/csv'

    csv_data = StringIO()
    writer = csv.writer(csv_data)
    writer.writerow(csv_headers)
    writer.writerows(csv_rows)

    # Set the CSV data as the response content
    response.data = csv_data.getvalue().encode('utf-8')

    return response
@views.route('/downloaid_csv')
def downloaid_csv():
    # Connect to MongoDB
 
    data = db.users.find()

    # Create CSV headers
    # Get all unique test skills
    # csv_headers = ['Serial Number', 'usn','Username', 'Test1', 'Test2', 'Test3']
    csv_headers = ['Serial Number', 'usn', 'Username','', 'Communication', 'Presentation', 'Technical'] + sorted_skills


    # Create CSV rows
    csv_rows = []
    serial_number = 1
    for item in data:
        usn = item['usn']

        username = item.get('personal', {}).get('username', '')
        test1_marks = item.get('test1', {}).get('communication', '')
        test2_marks = item.get('test2', {}).get('communication', '')
        test3_marks = item.get('test3', {}).get('communication', '')
        csv_row = [serial_number,usn ,username, test1_marks, test2_marks, test3_marks]
        csv_rows.append(csv_row)
        serial_number += 1

    # Create a response with CSV data
    response = make_response()
    response.headers['Content-Disposition'] = 'attachment; filename=data.csv'
    response.mimetype = 'text/csv'

    csv_data = StringIO()
    writer = csv.writer(csv_data)
    writer.writerow(csv_headers)
    writer.writerows(csv_rows)

    # Set the CSV data as the response content
    response.data = csv_data.getvalue().encode('utf-8')

    return response
@views.route('/downloadi_csv')
def downloadi_csv():
    # Connect to MongoDB
 
    data = db.users.find()

    # Create CSV headers
    # Get all unique test skills
     # Get all unique test skills
    response = make_response()
    response.headers['Content-Disposition'] = 'attachment; filename=data.csv'

    # Set the mimetype to indicate it's a CSV file
    response.mimetype = 'text/csv'

    # Open the response stream for writing CSV data
    csv_writer = csv.writer(response.stream)

    # Write CSV headers
    csv_writer.writerow(['Serial Number', 'usn','Username','tests', 'Communication', 'Technical','creativity','projectmanagement','timemanagement','genearl knowledge','interpersonal','resultoriented','leadership','Presentation',])

    # Write CSV data from MongoDB
    serial_number = 1
    for item in data:
        usn = item['usn']
        


        username = item.get('personal', {}).get('username', '')
        test1 = item.get('test1', {})
        communication = test1.get('communication', '')
        technical = test1.get('technical', '')
        creativity = test1.get('creativity', '')
        projectmanagement = test1.get('projectmmt', '')
        timemangement = test1.get('timemanagement', '')
        generalknowledge = test1.get('generalknowledge', '')
        interpersonal = test1.get('interpersonal', '')
        resultoriented = test1.get('resultoriented', '')
        leadership = test1.get('leardership', '')
        presentation = test1.get('presentation', '')


        test2 = item.get('test2', {})
        communications = test2.get('communication', '')
        technicals = test2.get('technical', '')
        creativitys = test2.get('creativity', '')
        projectmanagements = test2.get('projectmmt', '')
        timemangements = test2.get('timemanagement', '')
        generalknowledges = test2.get('generalknowledge', '')
        interpersonals = test2.get('interpersonal', '')
        resultorienteds = test2.get('resultoriented', '')
        leaderships = test2.get('leardership', '')
        presentations = test2.get('presentation', '')

        test3 = item.get('test3', {})
        communicationss = test3.get('communication', '')
        technicalss = test3.get('technical', '')
        creativityss = test3.get('creativity', '')
        projectmanagementss = test3.get('projectmmt', '')
        timemangementss = test3.get('timemanagement', '')
        generalknowledgess = test3.get('generalknowledge', '')
        interpersonalss = test3.get('interpersonal', '')
        resultorientedss = test3.get('resultoriented', '')
        leadershipss = test3.get('leardership', '')
        presentationss = test3.get('presentation', '')
        csv_writer.writerow([serial_number, usn,username,'test1' ,communication, technical, creativity,projectmanagement,timemangement,generalknowledge,interpersonal,resultoriented,leadership,presentation])
        csv_writer.writerow(['', '','','test2' ,communications, technicals, creativitys,projectmanagements,timemangements,generalknowledges,interpersonals,resultorienteds,leaderships,presentations])
        csv_writer.writerow(['', '','','test3' ,communicationss, technicalss, creativityss,projectmanagementss,timemangementss,generalknowledgess,interpersonalss,resultorientedss,leadershipss,presentationss])
        csv_writer.writerow([''])
        
        serial_number += 1

    return response


