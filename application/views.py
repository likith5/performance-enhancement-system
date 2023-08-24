from application import create_app
from flask import Blueprint,url_for,session,flash,make_response
from flask_session import Session
from application import db
from pymongo.errors import PyMongoError
from flask import render_template,request,redirect,Response
from bson.binary import Binary
from io import StringIO
import openpyxl
from openpyxl.styles import PatternFill
import json



# this is for xls writer 
import xlsxwriter

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
        userusn=user["usn"]
        email = user["personal"].get('email')
        college = user["personal"].get('college')
        phone = user["personal"].get('phone')
        linkdin = user["personal"].get('linkdin')
        github = user["personal"].get('github')
        
        title="dashboard"

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
        
        strongi = int(((technical+creativity+resultoriented)/15)*5)
        leaderi = int(((projectmm+leardership+timemanagement+resultoriented+communication)/25)*5)
        customeri = int(((presentation+generalknowledge+timemanagement+interpersonal+communication)/25)*5)
        projecti = int(((projectmm+resultoriented+timemanagement+technical+communication)/25)*5)
        designi = int(((leardership+resultoriented+creativity+technical)/20)*5)
        marketi = int((( presentation+resultoriented+communication+interpersonal+generalknowledge)/25)*5)
        def st(strongi):
            if strongi >= 4:
                return "Strong in Tech"
            else:
                return "Generic"
        strong = st(strongi)
        def lr(leaderi):
            if leaderi >= 4:
                return "Leadership Roles"
            else:
                return "Generic"
        leader = lr(leaderi)
        def cfr(customei):
            if  customeri <=4:
                return "Customer Facing Roles"
            else:
                return "None"
        customer = cfr(customeri)
        def pm(customer):
            if  projecti <= 4 :
                return "Project Management "
            else:
                return "None"
        project = pm(projecti)
        def df(designi):
            if designi <= 3  :
                return "Design Profile "
            else:
                return "None"
        design = df(designi)
        def mr(marketi):
            if marketi <= 3 :
                return "Marketing Role "
            else:
                return "None"
        market = mr(projecti)
        
        

        return render_template('profile.html',title=title,usn=usn,user=user,design=design,market=market,strong=strong,leader=leader,customer=customer,project=project,username=username,email=email,college=college,phone=phone,linkdin=linkdin,github=github,userusn=userusn)
 


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
                print(test)
                print(leardership)
                print(presentation)
                print(studentname)
                print(communication)

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
        test11 ="Test1"
        title="dashboard"
        test1_skills = user["test1"]
        
        # for item in test:
        #     print(item.)
        def summary(userr):
            p=[]
            for key, value in userr.items():
                p.append(int(value))
            return p
        test_function_summary=summary(test1_skills) 
        
       
        particular_testsummary=int((sum(test_function_summary)/50)*5)
        
        
     
        
        if request.method=="POST":
            man= request.form.get('test')
            test1 = man.capitalize()
            test =man.lower()
            title="dashboard"
            usn = session.get("studentemail")
            user = db.users.find_one({'usn':usn })
            username = user["personal"].get('username')
            show_graph1=False
            show_graph2=False
            show_graph3=False
            

            # print(test)

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
                show_graph1=True
                def summary(userr):
                    p=[]
                    for key, value in userr.items():
                        p.append(int(value))
                    return p
                p=summary(test1_skills) 
                
                
                particular_test1summary=int((sum(p)/50)*5)
              
                

                return render_template('dashboard.html',show_graph1=show_graph1,particular_testsummary=particular_test1summary,test1=test1,username=username,title=title,creativity=creativity,communication=communication,technical=technical,projectmm=projectmm,timemanagement=timemanagement,generalknowledge=generalknowledge,interpersonal=interpersonal,resultoriented=resultoriented,leardership=leardership,presentation=presentation)

                # redirect(url_for('views.dashboard'))
            
            if test=="test2":
                # test2 =user.get('test2')

                # if test2 is None:
                #     return   flash(" second test marks has not been given yet")

                # else:

               
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
                show_graph2=True
                test1_skills = user["test1"]
                test2_skills = user["test2"]
                def summary(userr):
                    p=[]
                    for key, value in userr.items():
                            p.append(int(value))
                    return p                
                list_of_second_test_results=summary(test2_skills)            
                list_of_first_test_results=summary(test1_skills)            
                particular_test2summary=int((sum(list_of_second_test_results)/50)*5)
                particular_test1summary=int((sum(list_of_first_test_results)/50)*5)
                
                
                return render_template('dashboard.html',show_graph2=show_graph2,particular_testsummary=particular_test2summary,p=json.dumps(list_of_first_test_results),q=json.dumps(list_of_second_test_results),test1=test1,username=username,title=title,creativity=creativity,communication=communication,technical=technical,projectmm=projectmm,timemanagement=timemanagement,generalknowledge=generalknowledge,interpersonal=interpersonal,resultoriented=resultoriented,leardership=leardership,presentation=presentation)
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
                show_graph3=True
                test1_skills = user["test1"]
                test2_skills = user["test2"]
                test3_skills = user["test3"]
                def summary(userr):
                    p=[]
                    for key, value in userr.items():
                        p.append(int(value))
                    return p
                
                list_of_third_test_results=summary(test3_skills)
                list_of_second_test_results=summary(test2_skills)
                list_of_first_test_results=summary(test1_skills)
                particular_test3summary=int((sum(list_of_third_test_results)/50)*5)
                particular_test2summary=int((sum(list_of_second_test_results)/50)*5)
                particular_test1summary=int((sum(list_of_first_test_results)/50)*5)
                def sumskills(user1,user2,user3):
                    p=[]
                    q=[]
                    r=[]
                    t1=[]
                    t2=[]
                    t3=[]            
                    for key, value in user1.items():
                        p.append(int(value))

                    t1.append(int((sum(p)/50)*5))
                    # print(t1)

                    for key, value in user2.items():
                        q.append(int(value))

                    t2.append(int((sum(q)/50)*5))

                    for key, value in user3.items():
                        r.append(int(value))
                    t3.append(int((sum(r)/50)*5) )
                    score1=t1+t2+t3           
                    return score1
                score1= sumskills(test1_skills,test2_skills,test3_skills)
                return render_template('dashboard.html',show_graph3=show_graph3,score1=json.dumps(score1),p=json.dumps(list_of_first_test_results),particular_testsummary=particular_test3summary,q=json.dumps(list_of_second_test_results),r=json.dumps(list_of_third_test_results),test1=test1,username=username,title=title,creativity=creativity,communication=communication,technical=technical,projectmm=projectmm,timemanagement=timemanagement,generalknowledge=generalknowledge,interpersonal=interpersonal,resultoriented=resultoriented,leardership=leardership,presentation=presentation)

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
        print(type(presentation))
        
        

        
        # return redirect(url_for('auth.login'))
        return render_template('dashboard.html',particular_testsummary=particular_testsummary,test1=test11,username=username,title=title,creativity=creativity,communication=communication,technical=technical,projectmm=projectmm,timemanagement=timemanagement,generalknowledge=generalknowledge,interpersonal=interpersonal,resultoriented=resultoriented,leardership=leardership,presentation=presentation)


        


        
      


        title="dashboard"

      
    elif  'teacheremail' in session :
        title="dashboard"
        usn = session.get("studentname")
        user = db.users.find_one({'usn':usn })
        username = user["personal"].get('username')
        test1_skills = user["test1"]
        def summary(userr):
            p=[]
            for key, value in userr.items():
                p.append(int(value))
            return p
        test_function_summary=summary(test1_skills)       
        particular_testsummary=int((sum(test_function_summary)/50)*5)      
        if request.method=="POST":
            man= request.form.get('test')
            test =man.lower()
            title="dashboard"
            usn = session.get("studentname")
            user = db.users.find_one({'usn':usn })
            username = user["personal"].get('username')
            show_graph1=False
            show_graph2=False
            show_graph3=False
            

            # print(test)
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
                show_graph1=True
                def summary(userr):
                    p=[]
                    for key, value in userr.items():
                        p.append(int(value))
                    return p
                p=summary(test1_skills) 
                
                
                particular_test1summary=int((sum(p)/50)*5)
                return render_template('dashboard.html',show_graph1=show_graph1,particular_testsummary=particular_test1summary,test1=test,username=username,title=title,creativity=creativity,communication=communication,technical=technical,projectmm=projectmm,timemanagement=timemanagement,generalknowledge=generalknowledge,interpersonal=interpersonal,resultoriented=resultoriented,leardership=leardership,presentation=presentation)

            if test=="test2":
                test2 =user.get('test2')

               
               
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
                show_graph2=True
                test1_skills = user["test1"]
                test2_skills = user["test2"]
                def summary(userr):
                    p=[]
                    for key, value in userr.items():
                        p.append(int(value))
                    return p                
                list_of_second_test_results=summary(test2_skills)            
                list_of_first_test_results=summary(test1_skills)            
                particular_test2summary=int((sum(list_of_second_test_results)/50)*5)
                particular_test1summary=int((sum(list_of_first_test_results)/50)*5)
                
                return render_template('dashboard.html',show_graph2=show_graph2,particular_testsummary=particular_test2summary,p=json.dumps(list_of_first_test_results),q=json.dumps(list_of_second_test_results),test1=test,username=username,title=title,creativity=creativity,communication=communication,technical=technical,projectmm=projectmm,timemanagement=timemanagement,generalknowledge=generalknowledge,interpersonal=interpersonal,resultoriented=resultoriented,leardership=leardership,presentation=presentation)
            if test=="test3":
                test3 =user.get('test3')
                
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
                show_graph3=True
                test1_skills = user["test1"]
                test2_skills = user["test2"]
                test3_skills = user["test3"]
                def summary(userr):
                    p=[]
                    for key, value in userr.items():
                        p.append(int(value))
                    return p
                
                list_of_third_test_results=summary(test3_skills)
                list_of_second_test_results=summary(test2_skills)
                list_of_first_test_results=summary(test1_skills)
                particular_test3summary=int((sum(list_of_third_test_results)/50)*5)
                particular_test2summary=int((sum(list_of_second_test_results)/50)*5)
                particular_test1summary=int((sum(list_of_first_test_results)/50)*5)
                def sumskills(user1,user2,user3):
                    p=[]
                    q=[]
                    r=[]
                    t1=[]
                    t2=[]
                    t3=[]            
                    for key, value in user1.items():
                        p.append(int(value))
                    t1.append(int((sum(p)/50)*5))
                    # print(t1)
                    for key, value in user2.items():
                        q.append(int(value))
                    t2.append(int((sum(q)/50)*5))
                    for key, value in user3.items():
                        r.append(int(value))
                    t3.append(int((sum(r)/50)*5) )
                    score1=t1+t2+t3           
                    return score1
                score1= sumskills(test1_skills,test2_skills,test3_skills)
            
                return render_template('dashboard.html',show_graph3=show_graph3,score1=json.dumps(score1),p=json.dumps(list_of_first_test_results),particular_testsummary=particular_test3summary,q=json.dumps(list_of_second_test_results),r=json.dumps(list_of_third_test_results),test1=test,username=username,title=title,creativity=creativity,communication=communication,technical=technical,projectmm=projectmm,timemanagement=timemanagement,generalknowledge=generalknowledge,interpersonal=interpersonal,resultoriented=resultoriented,leardership=leardership,presentation=presentation)

       
        
        

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

         
                       
        test11="Test1"
      


        return render_template('dashboard.html',particular_testsummary=particular_testsummary,test1=test11,username=username,title=title,creativity=creativity,communication=communication,technical=technical,projectmm=projectmm,timemanagement=timemanagement,generalknowledge=generalknowledge,interpersonal=interpersonal,resultoriented=resultoriented,leardership=leardership,presentation=presentation)

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
                return redirect(url_for('views.score'))
                # return render_template('score.html')
            else:
                flash('User not found', category='error')
                return redirect(url_for('views.search'))
                # return render_template('dashboard.html',title=title,name=name)   
        return render_template('search.html',usn=usn,username=username)
    return redirect(url_for('auth.login'))


     
@views.route('/userdata',methods=['GET','POST'])    
def userdata():
    if  "studentemail" in session:
        if request.method == "POST":
            usn = session.get("studentemail")

            username= request.form.get('username')
            email = request.form.get('email')
            phone = request.form.get('phone')
            course = request.form.get('course')
            college = request.form.get('college')
            city = request.form.get('city')
            numberofcertifications= request.form.get('numberofcertifications')       
            technicalskills= request.form.get('technicalskills')
            softskills= request.form.get('softskills')
            tenthboard= request.form.get('tenthboard')
            tenthmarks= request.form.get('tenthmarks')
            twelvethboard= request.form.get('twelvethboard')
            twelvethmarks= request.form.get('twelvethmarks')
            ugaverage= request.form.get('ugaverage')
            linkdin= request.form.get('linkdin')
            github= request.form.get('github')
            skill1= request.form.get('skill1')
            skill2= request.form.get('skill2')
            skill3= request.form.get('skill3')
            skill4= request.form.get('skill4')
            skill5= request.form.get('skill5')
            certification1= request.form.get('certification1')
            certification2= request.form.get('certification2')
            certification3= request.form.get('certification3')
            certification4= request.form.get('certification4')
            certification5= request.form.get('certification5')
            internshipexperience= request.form.get('internshipexperience')

            hiredcontent= request.form.get('hiredcontent')
           

            try:
                db.users.update_one(
                        {"usn": usn},
                        {
                            "$set": {
                                "personal": {
                                    "username": username,
                                    "email": email,
                                    "phone": phone,
                                    "course": course,
                                    "city": city,
                                    "college":college,
                                    "numberofcertifications":numberofcertifications,
                                    "technicalskills":technicalskills,
                                    "softskills":softskills,
                                    "tenthboard":tenthboard,
                                    "tenthmarks":tenthmarks,
                                    "twelvethboard":twelvethboard,
                                    "twelvethmarks":twelvethmarks,
                                    "ugaverage":ugaverage,
                                    "linkdin": linkdin,
                                    "github": github,
                                    "skill1":skill1,
                                    "skill2":skill2,
                                    "skill3":skill3,
                                    "skill4":skill4,
                                    "skill5":skill5,
                                    "certification1":certification1,
                                    "certification2":certification2,
                                    "certification3":certification3,
                                    "certification4":certification4,
                                    "certification5":certification5,
                                    "internshipexperience":internshipexperience,
                                    "hiredcontent":hiredcontent,
                                }
                            }
                        }
                    )
                db.users.update_one(
                        {"usn": usn},
                        {
                            "$set": {
                                "certificate": {
                                    
                                    
                                    "certification1":certification1,
                                    "certification2":certification2,
                                    "certification3":certification3,
                                    "certification4":certification4,
                                    "certification5":certification5,
                                    
                                }
                            }
                        }
                    )
                db.users.update_one(
                        {"usn": usn},
                        {
                            "$set": {
                                "skills": {
                                    
                                    
                                     "skill1":skill1,
                                    "skill2":skill2,
                                    "skill3":skill3,
                                    "skill4":skill4,
                                    "skill5":skill5,
                                    
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

     

# @views.route('profileskills')
# def profileskills():
#     if request.method == "POST":
#         num_inputs = int(request.form.get("num_inputs", 0))
#     else:
#         num_inputs = 0
    
#     return render_template("index.html", num_inputs=num_inputs)



@views.route('/downloadi_csv')
def downloadi_csv():
    # Connect to MongoDB

    data = db.users.find()

    # Create a new workbook
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # Write headers with formatting
    sheet.append(['Serial Number', 'usn', 'Username', 'tests', 'Communication', 'Technical', 'creativity', 'projectmanagement', 'timemanagement', 'genearl knowledge', 'interpersonal', 'resultoriented', 'leadership', 'Presentation'])
    header_row = sheet[1]
    
    color_mapping = {
        None: "FF0000",  # Red
        1: "00FF00",  # Green
        2: "FFA500",  # Orange
        3: "FFFF00"  # Yellow
    }
    # Write data from MongoDB
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
        # print(creativitys)
        # print(type(creativitys))

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

        sheet.append([serial_number, usn, username, 'test1', communication, technical, creativity, projectmanagement, timemangement, generalknowledge, interpersonal, resultoriented, leadership, presentation])
        sheet.append(['', '', '', 'test2', communications, technicals, creativitys, projectmanagements, timemangements, generalknowledges, interpersonals, resultorienteds, leaderships, presentations])
        sheet.append(['', '', '', 'test3', communicationss, technicalss, creativityss, projectmanagementss, timemangementss, generalknowledgess, interpersonalss, resultorientedss, leadershipss, presentationss])
        sheet.append([''])
        
        serial_number += 1
        # Apply background color to cells with values 1, 2, 3, 4, 5 in columns E to N
        for row in sheet.iter_rows(min_row=2, min_col=5, max_col=14):
            for cell in row:
                if isinstance(cell.value, int) and cell.value in colors:
                    fill = PatternFill(start_color=colors[cell.value], end_color=colors[cell.value], fill_type="solid")
                    cell.fill = fill
                elif cell.value == 'null':
                    fill = PatternFill(start_color='CCCCCC', end_color='CCCCCC', fill_type="solid")
                    cell.fill = fill
                elif cell.value == '1':
                    fill = PatternFill(start_color='FF0000', end_color='FF0000', fill_type="solid")
                    cell.fill = fill
                elif cell.value == '2':
                    fill = PatternFill(start_color='FFC000', end_color='FFC000', fill_type="solid")
                    cell.fill = fill
                elif cell.value == '3':
                    fill = PatternFill(start_color='FFFF00', end_color='FFFF00', fill_type="solid")
                    cell.fill = fill
                elif cell.value == '4':
                    fill = PatternFill(start_color='00B050', end_color='00B050', fill_type="solid")
                    cell.fill = fill
                elif cell.value == '5':
                    fill = PatternFill(start_color='0070C0', end_color='0070C0', fill_type="solid")
                    cell.fill = fill
                else:
                    fill = PatternFill(start_color='FFFFFF', end_color='FFFFFF', fill_type="solid")
                    cell.fill = fill

    # Save the workbook
    response = Response()
    response.headers['Content-Disposition'] = 'attachment; filename=data.xlsx'
    response.mimetype = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    workbook.save(response.stream)

    return response


# @views.route('/downloadi_csv')
# def downloadi_csv():
@views.route('/report')
def report():
    if 'studentemail' in session :
        usn = session.get('studentemail')
        user = db.users.find_one({'usn':usn })
        test1_skills = user["test1"]
        test2_skills = user["test2"]
        test3_skills = user["test3"]
        communication1 = int(user['test1'].get('communication'))
        technical1 = int(user["test1"].get('technical'))
        creativity1 = int(user['test1'].get('creativity'))
        projectmm1 = int(user['test1'].get('projectmmt'))
        timemanagement1 = int(user['test1'].get('timemanagement'))
        generalknowledge1 = int(user['test1'].get('generalknowledge'))
        interpersonal1 = int(user['test1'].get('interpersonal'))
        resultoriented1 = int(user['test1'].get('resultoriented'))
        leardership1 = int(user['test1'].get('leardership'))
        presentation1 = int(user['test1'].get('presentation'))
        
        strongi = int(((technical1+creativity1+resultoriented1)/15)*5)
        leaderi = int(((projectmm1+leardership1+timemanagement1+resultoriented1+communication1)/25)*5)
        customeri = int(((presentation1+generalknowledge1+timemanagement1+interpersonal1+communication1)/25)*5)
        projecti = int(((projectmm1+resultoriented1+timemanagement1+technical1+communication1)/25)*5)
        designi = int(((leardership1+resultoriented1+creativity1+technical1)/20)*5)
        marketi = int((( presentation1+resultoriented1+communication1+interpersonal1+generalknowledge1)/25)*5)
        def st(strongi):
            if strongi >= 4:
                return "Strong in Tech"
            else:
                return "Generic"
        strong = st(strongi)
        def lr(leaderi):
            if leaderi >= 4:
                return "Leadership Roles"
            else:
                return "Generic"
        leader = lr(leaderi)
        def cfr(customei):
            if  customeri <=4:
                return "Customer Facing Roles"
            else:
                return "None"
        customer = cfr(customeri)
        def pm(customer):
            if  projecti <= 4 :
                return "Project Management "
            else:
                return "None"
        project = pm(projecti)
        def df(designi):
            if designi <= 3  :
                return "Design Profile "
            else:
                return "None"
        design = df(designi)
        def mr(marketi):
            if marketi <= 3 :
                return "Marketing Role "
            else:
                return "None"
        market = mr(projecti)

        def summary(userr):
                    p=[]
                    for key, value in userr.items():
                            p.append(int(value))
                    return p  
        list_of_second_test_results=summary(test2_skills)            
        list_of_first_test_results=summary(test1_skills)
        list_of_third_test_results=summary(test3_skills)
        communication=[list_of_first_test_results[0],list_of_second_test_results[0],list_of_third_test_results[0]]
        technical=[list_of_first_test_results[1],list_of_second_test_results[1],list_of_third_test_results[1]]
        creativity=[list_of_first_test_results[2],list_of_second_test_results[2],list_of_third_test_results[2]]
        projectmmt=[list_of_first_test_results[3],list_of_second_test_results[3],list_of_third_test_results[3]]
        timemmt=[list_of_first_test_results[4],list_of_second_test_results[4],list_of_third_test_results[4]]
        gk=[list_of_first_test_results[5],list_of_second_test_results[5],list_of_third_test_results[5]]
        interpersonal=[list_of_first_test_results[6],list_of_second_test_results[6],list_of_third_test_results[6]]
        resultoriented=[list_of_first_test_results[7],list_of_second_test_results[7],list_of_third_test_results[7]]
        leadership=[list_of_first_test_results[8],list_of_second_test_results[8],list_of_third_test_results[8]]
        presentation=[list_of_first_test_results[9],list_of_second_test_results[9],list_of_third_test_results[9]]

    return render_template('report.html',user=user,design=design,market=market,strong=strong,leader=leader,customer=customer,project=project,presentation=json.dumps(presentation),resultoriented=json.dumps(resultoriented),leadership=json.dumps(leadership),interpersonal=json.dumps(interpersonal),communication=json.dumps(communication),technical=json.dumps(technical),creativity=json.dumps(creativity),projectmmt=json.dumps(projectmmt),timemmt=json.dumps(timemmt),gk=json.dumps(gk))
@views.route('/resume')
def resume():
    if 'studentemail' in session :
        usn = session.get('studentemail')
        user = db.users.find_one({'usn':usn })
        username = user["personal"].get('username')
        email = user["personal"].get('email')
        college = user["personal"].get('college')
        phone = user["personal"].get('phone')
        numberofcertifications = user["personal"].get('numberofcertifications')
        technicalskills = user["personal"].get('technicalskills')
        softskills = user["personal"].get('softskills')
        tenthboard = user["personal"].get('tenthboard')
        tenthmarks = user["personal"].get('tenthmarks')
        twelvethboard = user["personal"].get('twelvethboard')
        twelvethmarks = user["personal"].get('twelvethmarks')
        ugaverage = user["personal"].get('ugaverage')
        linkdin = user["personal"].get('linkdin')
        github = user["personal"].get('github')
        skill1 = user["personal"].get('skill1')
        skill2 = user["personal"].get('skill2')
        skill3 = user["personal"].get('skill3')
        skill4 = user["personal"].get('skill4')
        skill5 = user["personal"].get('skill5')
        certification1 = user["personal"].get('certification1')
        certification2 = user["personal"].get('certification2')
        certification3= user["personal"].get('certification3')
        certification4 = user["personal"].get('certification4')
        certification5 = user["personal"].get('certification5')
        
        # for key,value in p.items():
        #     if value=="dsce":
        #         print("heyy well done ") 
        #     else:
        #         print('better luck next time')
        

        
        title="dashboard"

    return render_template('resume.html',user=user)


@views.route('/score',methods=['GET','POST'])
def score():
    usn = session.get('studentname')
    user = db.users.find_one({'usn':usn })
    username = user["personal"].get('username')
    userusn = user["personal"].get('usn')

    title="marks enter"
    if  'teacheremail' in session:

        if request.method == 'POST':

                test= request.form.get('test')
                technical= request.form.get('technical')
                form1= request.form
                c1=form1.get('communication')
                print(c1)
                # t1=form1.get('')
                communication= request.form.get('communication')
               
                creativity= request.form.get('creativity')
                projectmmt= request.form.get('projectmmt')
                timemanagement= request.form.get('timemanagement')
                generalknowledge= request.form.get('generalknowledge')
                interpersonal= request.form.get('interpersonal')
                resultoriented= request.form.get('resultoriented')
                leardership= request.form.get('leardership')
                presentation= request.form.get('presentation')
                
                print(leardership)
                print(presentation)
                print(communication)

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
                        return redirect(url_for('views.score'))
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
                        return redirect(url_for('views.score'))
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
                        return redirect(url_for('views.score'))
                    
        
        # print(studentname)
        # return render_template("marksenter.html",title=title,studentname=studentname)
        return render_template("score.html",username=username,usn=usn)
    return redirect(url_for('auth.login'))

























