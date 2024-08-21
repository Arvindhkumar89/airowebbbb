from flask import Flask,request,jsonify
from flask_login import login_user, UserMixin,LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import re
from datetime import datetime

app =Flask(__name__)
app.secret_key="web1"
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db= SQLAlchemy(app)
login_manager = LoginManager(app)
class user(db.Model,UserMixin):
    id= db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(100))
    email= db.Column(db.String(100),unique = True)
    password = db.Column(db.String(100))
app.app_context().push()
db.create_all()


@app.route('/login',methods=["POST"])
def home():
    data = request.get_json()
    email = data['email']
    pasw = data['password']
    print(data)
    print(email)
    print(pasw)
    checkuser = user.query.filter_by(email=email).first()
    if email=='' or pasw=='':
        return jsonify({'error': 'Fill the required field'}) 
    elif checkuser:
        if  checkuser.password == pasw:
            login_user(checkuser, remember= True)
            return jsonify({'message':'login successfully'})
        else:
            return jsonify({'error': 'Invalid Password'})
    else:
        return jsonify({'error': 'Invalid Email'})


class admin(db.Model,UserMixin):
    id= db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(100))
    email= db.Column(db.String(100),unique = True)
    password = db.Column(db.String(100))
@app.route('/admin',methods=["POST"])
def adminhome(): 
    data = request.get_json()
    email = data['email']
    pasw = data['password']
    print(data)
    print(email)
    print(pasw)
    checkuser = admin.query.filter_by(email=email).first()
    if email=='' or pasw=='':
        return jsonify({'error': 'Fill the required field'}) 
    elif checkuser:
        if  checkuser.password == pasw:
            login_user(checkuser, remember= True)
            return jsonify({'message':'login successfully'})
        else:
            return jsonify({'error': 'Invalid Password'})
    else:
        return jsonify({'error': 'Invalid Email'})


    


@app.route('/', methods=['POST'])
def hello():
    data = request.get_json()
    print( data)
    uname = data['username']
    email = data["email"]
    pasw = data["password"]
    print(uname)
    print(email)
    print(pasw)
    emailc = '^[a-z0-9]+[\._]?[ a-z0-9]+[@]\w+[. ]\w{2,3}$'
    checkuser = user.query.filter_by(email=email).first()
    if email=="" or uname=='' or pasw=='':
        return jsonify({'error':'Fill the required field'})
    elif not re.match(emailc,email):
        return jsonify({'error': 'The email is invalid'})
    elif checkuser:
        return jsonify({'error': 'Account already exists'})
    elif len(pasw)<8:
        return jsonify({'error': 'Atleast 8 characters required'})
    else:
        userdb = user(username= uname, email = email,password=pasw)
        db.session.add(userdb)
        db.session.commit()
        return jsonify({'message': 'signup successfully'})


f1=[['456', 'Indigo', 'Chennai', 'Coimbatore', '15-09-2023', '09:30', '10:30', '1hr', '4500', 'MAA', 'CJB', 56], ['123', 'Air India Express', 'Chennai', 'Madurai', '15-09-2023', '12:00', '13:30', '1hr 30mins', '3800', 'MAA', 'IXM', 39], ['789', 'SpiceJet', 'Chennai', 'Trichy', '15-09-2023', '15:15', '16:15', '1hr', '3200', 'MAA', 'TRZ', 22], ['234', 'Air India', 'Chennai', 'Salem', '15-09-2023', '17:30', '18:15', '45mins', '2900', 'MAA', 'SXV', 24], ['567', 'Vistara', 'Chennai', 'Tirunelveli', '15-09-2023', '20:00', '21:30', '1hr 30mins', '5200', 'MAA', 'TCR', 21], ['890', 'Indigo', 'Chennai', 'Erode', '16-09-2023', '08:45', '09:45', '1hr', '3400', 'MAA', 'EDR', 46], ['345', 'Air India Express', 'Chennai', 'Coimbatore', '16-09-2023', '11:30', '12:30', '1hr', '4500', 'MAA', 'CJB', 3], ['678', 'SpiceJet', 'Chennai', 'Madurai', '16-09-2023', '14:15', '15:45', '1hr 30mins', '3800', 'MAA', 'IXM', 10], ['912', 'Air India', 'Chennai', 'Trichy', '16-09-2023', '17:00', '18:00', '1hr', '3200', 'MAA', 'TRZ', 39], ['234', 'Vistara', 'Chennai', 'Salem', '16-09-2023', '19:30', '20:15', '45mins', '2900', 'MAA', 'SXV', 12], ['456', 'Indigo', 'Chennai', 'Tirunelveli', '17-09-2023', '09:00', '10:30', '1hr 30mins', '5200', 'MAA', 'TCR', 31], ['123', 'Air India Express', 'Chennai', 'Erode', '17-09-2023', '12:45', '13:45', '1hr', '3400', 'MAA', 'EDR', 10], ['789', 'SpiceJet', 'Chennai', 'Coimbatore', '17-09-2023', '15:30', '16:30', '1hr', '4500', 'MAA', 'CJB', 56], ['234', 'Air India', 'Chennai', 'Madurai', '17-09-2023', '18:15', '19:45', '1hr 30mins', '3800', 'MAA', 'IXM', 47], ['890', 'Vistara', 'Chennai', 'Trichy', '17-09-2023', '21:00', '22:00', '1hr', '3200', 'MAA', 'TRZ', 1], ['345', 'Indigo', 'Chennai', 'Salem', '18-09-2023', '08:15', '09:00', '45mins', '2900', 'MAA', 'SXV', 16], ['678', 'Air India Express', 'Chennai', 'Tirunelveli', '18-09-2023', '10:45', '12:15', '1hr 30mins', '5200', 'MAA', 'TCR', 20], ['912', 'SpiceJet', 'Chennai', 'Erode', '18-09-2023', '13:30', '14:30', '1hr', '3400', 'MAA', 'EDR', 37], ['234', 'Air India', 'Chennai', 'Coimbatore', '18-09-2023', '16:15', '17:15', '1hr', '4500', 'MAA', 'CJB', 43], ['456', 'Vistara', 'Chennai', 'Madurai', '18-09-2023', '19:00', '20:30', '1hr 30mins', '3800', 'MAA', 'IXM', 2], ['123', 'Indigo', 'Chennai', 'Trichy', '19-09-2023', '08:30', '09:30', '1hr', '3200', 'MAA', 'TRZ', 15], ['789', 'Air India Express', 'Chennai', 'Salem', '19-09-2023', '11:15', '12:00', '45mins', '2900', 'MAA', 'SXV', 7], ['234', 'SpiceJet', 'Chennai', 'Tirunelveli', '19-09-2023', '13:45', '15:15', '1hr 30mins', '5200', 'MAA', 'TCR', 28], ['567', 'Air India', 'Chennai', 'Erode', '19-09-2023', '16:30', '17:30', '1hr', '3400', 'MAA', 'EDR', 46], ['890', 'Vistara', 'Chennai', 'Coimbatore', '19-09-2023', '19:15', '20:15', '1hr', '4500', 'MAA', 'CJB', 52], ['345', 'Indigo', 'Chennai', 'Madurai', '20-09-2023', '08:00', '09:30', '1hr 30mins', '3800', 'MAA', 'IXM', 32], ['678', 'Air India Express', 'Chennai', 'Trichy', '20-09-2023', '10:45', '11:45', '1hr', '3200', 'MAA', 'TRZ', 5], ['912', 'SpiceJet', 'Chennai', 'Salem', '20-09-2023', '13:30', '14:15', '45mins', '2900', 'MAA', 'SXV', 28], ['456', 'Vistara', 'Chennai', 'Tirunelveli', '20-09-2023', '16:00', '17:30', '1hr 30mins', '5200', 'MAA', 'TCR', 17], ['123', 'Indigo', 'Chennai', 'Erode', '20-09-2023', '19:00', '20:00', '1hr', '3400', 'MAA', 'EDR', 3], ['789', 'Air India Express', 'Chennai', 'Coimbatore', '21-09-2023', '08:45', '09:45', '1hr', '4500', 'MAA', 'CJB', 25], ['234', 'SpiceJet', 'Chennai', 'Madurai', '21-09-2023', '11:30', '13:00', '1hr 30mins', '3800', 'MAA', 'IXM', 38], ['567', 'Air India', 'Chennai', 'Trichy', '21-09-2023', '14:15', '15:15', '1hr', '3200', 'MAA', 'TRZ', 21], ['890', 'Vistara', 'Chennai', 'Salem', '21-09-2023', '17:00', '17:45', '45mins', '2900', 'MAA', 'SXV', 53], ['345', 'Indigo', 'Chennai', 'Tirunelveli', '22-09-2023', '09:30', '11:00', '1hr 30mins', '5200', 'MAA', 'TCR', 32], ['678', 'Air India Express', 'Chennai', 'Erode', '22-09-2023', '12:15', '13:15', '1hr', '3400', 'MAA', 'EDR', 2], ['912', 'SpiceJet', 'Chennai', 'Coimbatore', '22-09-2023', '15:00', '16:00', '1hr', '4500', 'MAA', 'CJB', 30], ['234', 'Air India', 'Chennai', 'Madurai', '22-09-2023', '17:45', '19:15', '1hr 30mins', '3800', 'MAA', 'IXM', 56], ['456', 'Vistara', 'Chennai', 'Trichy', '22-09-2023', '20:30', '21:30', '1hr', '3200', 'MAA', 'TRZ', 7], ['123', 'Indigo', 'Chennai', 'Salem', '30-06-2023', '09:00', '09:45', '45mins', '2900', 'MAA', 'SXV', 28], ['789', 'Air India Express', 'Chennai', 'Tirunelveli', '30-06-2023', '11:30', '13:00', '1hr 30mins', '5200', 'MAA', 'TCR', 7], ['234', 'SpiceJet', 'Chennai', 'Erode', '30-06-2023', '14:15', '15:15', '1hr', '3400', 'MAA', 'EDR', 23], ['567', 'Air India Express', 'Chennai', 'Madurai', '15-09-2023', '02:45', '04:00', '1hr 15mins', '5200', 'MAA', 'IXM', 19], ['890', 'SpiceJet', 'Chennai', 'Coimbatore', '15-09-2023', '03:00', '04:00', '1hr', '3400', 'MAA', 'CJB', 45], ['345', 'Air India', 'Chennai', 'Salem', '15-09-2023', '05:30', '06:15', '45mins', '4500', 'MAA', 'SXV', 6], ['678', 'Vistara', 'Chennai', 'Tirunelveli', '15-09-2023', '04:45', '05:30', '45mins', '3800', 'MAA', 'TRZ', 24], ['912', 'Indigo', 'Chennai', 'Trichy', '16-09-2023', '03:30', '04:15', '45mins', '2900', 'MAA', 'TRZ', 14], ['345', 'Air India Express', 'Chennai', 'Madurai', '16-09-2023', '02:15', '03:30', '1hr 15mins', '5200', 'MAA', 'IXM', 55], ['678', 'SpiceJet', 'Chennai', 'Coimbatore', '16-09-2023', '05:00', '06:00', '1hr', '3400', 'MAA', 'CJB', 31], ['912', 'Air India', 'Chennai', 'Salem', '16-09-2023', '04:30', '05:15', '45mins', '4500', 'MAA', 'SXV', 58], ['234', 'Vistara', 'Chennai', 'Tirunelveli', '16-09-2023', '03:45', '04:30', '45mins', '3800', 'MAA', 'TRZ', 23], ['567', 'Indigo', 'Chennai', 'Trichy', '17-09-2023', '05:30', '06:15', '45mins', '2900', 'MAA', 'TRZ', 33], ['890', 'Air India Express', 'Chennai', 'Madurai', '17-09-2023', '02:45', '04:00', '1hr 15mins', '5200', 'MAA', 'IXM', 10], ['345', 'SpiceJet', 'Chennai', 'Coimbatore', '17-09-2023', '03:00', '04:00', '1hr', '3400', 'MAA', 'CJB', 13], ['678', 'Air India', 'Chennai', 'Salem', '17-09-2023', '05:30', '06:15', '45mins', '4500', 'MAA', 'SXV', 13], ['123', 'Indigo', 'Chennai', 'Coimbatore', '15-09-2023', '05:15', '05:55', '40mins', '2900', 'MAA', 'CJB', 56], ['456', 'Air India Express', 'Chennai', 'Madurai', '15-09-2023', '04:45', '05:45', '1hr', '5200', 'MAA', 'IXM', 17], ['789', 'SpiceJet', 'Chennai', 'Trichy', '15-09-2023', '04:30', '05:15', '45mins', '3400', 'MAA', 'TRZ', 28], ['234', 'Air India', 'Chennai', 'Salem', '15-09-2023', '05:30', '06:00', '30mins', '4500', 'MAA', 'SXV', 10], ['567', 'Vistara', 'Chennai', 'Tirunelveli', '15-09-2023', '04:15', '04:45', '30mins', '3800', 'MAA', 'TRZ', 20], ['890', 'Indigo', 'Chennai', 'Coimbatore', '16-09-2023', '05:00', '05:40', '40mins', '2900', 'MAA', 'CJB', 21], ['321', 'Air India Express', 'Chennai', 'Madurai', '16-09-2023', '04:30', '05:30', '1hr', '5200', 'MAA', 'IXM', 24], ['654', 'SpiceJet', 'Chennai', 'Trichy', '16-09-2023', '05:15', '06:00', '45mins', '3400', 'MAA', 'TRZ', 35], ['987', 'Air India', 'Chennai', 'Salem', '16-09-2023', '05:45', '06:15', '30mins', '4500', 'MAA', 'SXV', 30], ['432', 'Vistara', 'Chennai', 'Tirunelveli', '16-09-2023', '04:30', '05:00', '30mins', '3800', 'MAA', 'TRZ', 17], ['765', 'Indigo', 'Chennai', 'Coimbatore', '17-09-2023', '05:30', '06:10', '40mins', '2900', 'MAA', 'CJB', 44], ['098', 'Air India Express', 'Chennai', 'Madurai', '17-09-2023', '04:45', '05:45', '1hr', '5200', 'MAA', 'IXM', 30], ['321', 'SpiceJet', 'Chennai', 'Trichy', '17-09-2023', '05:00', '05:45', '45mins', '3400', 'MAA', 'TRZ', 35], ['654', 'Air India', 'Chennai', 'Salem', '17-09-2023', '05:30', '06:00', '30mins', '4500', 'MAA', 'SXV', 45]]
l=['0', '0', '0', '0',"0"]
@app.route('/remove',methods=['POST'])
def remove1():
    # print('hi')
    print(dic[int(selectk1[0])])
    f1.remove(dic[int(selectk1[0])])
    del dic[int(selectk1[0])]
    print(dic)
    print("complete")
    return jsonify(dic)

@app.route('/addd',methods=['POST'])
def addelement():
    print("hi")
    data = request.get_json()
    fln = data['fn']
    aln = data['an']
    from1 = data['fro']
    to1 = data['to1']
    date1 = data['datee']
    date1 = "-".join(date1.split("-")[::-1])    
    dpt = data['dtimee']
    atm = data['atimee']
    dura = data['du']
    pri = data['pri']
    fcodee = data['fcode']
    tocodee = data['tocode']
    availa = data['avai']
    l1 =[str(fln),aln,from1,to1,date1,dpt,atm,dura,str(pri),fcodee,tocodee,availa]
    f1.append(l1)
    dic[len(dic)+1] = l1
    print(dic)
    print(l1)
    return jsonify(dic)


@app.route('/search', methods=['POST'])
def searchc():
    data = request.get_json()
    from1 = data["from"]
    to1 = data['to']
    date1 = data['month1']
    class1 = data['selectcheck']
    time11 = data['time1'] 
    date1 = "-".join(date1.split("-")[::-1])
    l[0]=(from1)
    l[1] = (to1)
    l[2]=(date1)
    l[3]=(class1)
    l[4]=(time11)
    print(l)
    return 'hi'

dic={}
@app.route('/flight', methods=['POST'])
def flight():
    searchres =[]
    from1 = l[0]
    to1=l[1]
    date1 =l[2]
    class1= l[3]
    time11 =l[4]
    before6 = datetime.strptime("06:00","%H:%M")
    before12 = datetime.strptime("12:00","%H:%M")
    after6 = datetime.strptime("18:00","%H:%M")
    for i in range(len(f1)):
        if f1[i][2] == from1 and f1[i][3] == to1 and f1[i][4] == date1 and f1[i][11] !=0:
            if class1 == "Business":
                f1[i][8] = str(int(f1[i][8])*3)
            if time11 == "before6":
                c  = datetime.strptime(f1[i][5],"%H:%M")
                if c.hour<before6.hour:
                    searchres.append((f1[i]))
            elif time11 == "6 to 12":
                c  = datetime.strptime(f1[i][5],"%H:%M")
                if c.hour>=before6.hour and c.hour<before12.hour:
                    searchres.append((f1[i]))
            elif time11 == "12 to 6":
                c  = datetime.strptime(f1[i][5],"%H:%M")
                if c.hour>=before12.hour and c.hour<after6.hour:
                    searchres.append((f1[i]))
            elif time11 =='after6':
                c  = datetime.strptime(f1[i][5],"%H:%M")
                if c.hour>=after6.hour:
                    searchres.append((f1[i]))
            else:
                searchres.append((f1[i]))
    
    for i in range(1,len(searchres)+1):
        dic[i] = searchres[i-1]
    print(dic)
    # print(selectk[0])
    if mybookings:
        print(dic[int(selectk[0])])
        ab = dic[int(selectk[0])][11]-1
        dic[int(selectk[0])][11] = ab
        print(dic)
    print('helloooooooo0000000')
    return jsonify(dic)

selectk=[0]
@app.route('/selectedkey', methods=['POST'])
def selectedkey():
    data = request.get_json()
    selectkey = data.get('selectkey')
    selectk[0] = selectkey
    print(selectk[0])
    return 'hi'


@app.route('/book', methods=['POST'])
def book():
    selectedflight = dic[int(selectk[0])]
    return jsonify(selectedflight)

mybookings=[]


@app.route('/confirm', methods=["POST"])
def confirm():
    data = request.get_json()
    data1 = data['confirm1']
    name = data['name1']
    mobile1 = data['mobile']
    email1 = data['email']
    if data1 =='c':
        d = dic[int(selectk[0])] 
        d.append(name)
        d.append(mobile1)
        d.append(email1)
        mybookings.append(d)
    print(mybookings)
    return 'hi'

@app.route('/mybook', methods=['POST'])
def mybook():
    print(mybookings)
    return jsonify(mybookings)



@app.route('/search1', methods=['POST'])
def searchc1():
    data = request.get_json()
    from1 = data["from"]
    to1 = data['to']
    date1 = data['month1']
    class1 = data['selectcheck']
    time11 = data['time1'] 
    date1 = "-".join(date1.split("-")[::-1])
    l[0]=(from1)
    l[1] = (to1)
    l[2]=(date1)
    l[3]=(class1)
    l[4]=(time11)
    print(l)
    return 'hi'

dic={}
@app.route('/flight1', methods=['POST'])
def flight1():
    searchres =[]
    from1 = l[0]
    to1=l[1]
    date1 =l[2]
    class1= l[3]
    time11 =l[4]
    before6 = datetime.strptime("06:00","%H:%M")
    before12 = datetime.strptime("12:00","%H:%M")
    after6 = datetime.strptime("18:00","%H:%M")
    for i in range(len(f1)):
        if f1[i][2] == from1 and f1[i][3] == to1 and f1[i][4] == date1 and f1[i][11] !=0:
            if class1 == "Business":
                f1[i][8] = str(int(f1[i][8])*3)
            if time11 == "before6":
                c  = datetime.strptime(f1[i][5],"%H:%M")
                if c.hour<before6.hour:
                    searchres.append((f1[i]))
            elif time11 == "6 to 12":
                c  = datetime.strptime(f1[i][5],"%H:%M")
                if c.hour>=before6.hour and c.hour<before12.hour:
                    searchres.append((f1[i]))
            elif time11 == "12 to 6":
                c  = datetime.strptime(f1[i][5],"%H:%M")
                if c.hour>=before12.hour and c.hour<after6.hour:
                    searchres.append((f1[i]))
            elif time11 =='after6':
                c  = datetime.strptime(f1[i][5],"%H:%M")
                if c.hour>=after6.hour:
                    searchres.append((f1[i]))
            else:
                searchres.append((f1[i]))
    
    for i in range(1,len(searchres)+1):
        dic[i] = searchres[i-1]
    print(dic)
    return jsonify(dic)

selectk1=[0]
@app.route('/selectedkey1', methods=['POST'])
def selectedkey1():
    data = request.get_json()
    selectkey = data.get('selectkey')
    selectk1[0] = selectkey
    print(selectk1[0])
    return 'hi'

searchres1=[]
@app.route('/adminbook', methods =['POST'])
def adminbook():
    data = request.get_json()
    fnum = str(data['num'])
    time11 = data['time1']
    print(data)
    print(mybookings)
    f2 =mybookings
    before6 = datetime.strptime("06:00","%H:%M")
    before12 = datetime.strptime("12:00","%H:%M")
    after6 = datetime.strptime("18:00","%H:%M")
    for i in range(len(f2)):
        if f2[i][0] == fnum:
            if time11 == "before6":
                c  = datetime.strptime(f2[i][5],"%H:%M")
                if c.hour<before6.hour:
                    searchres1.append((f2[i]))
            elif time11 == "6 to 12":
                c  = datetime.strptime(f2[i][5],"%H:%M")
                if c.hour>=before6.hour and c.hour<before12.hour:
                    searchres1.append((f2[i]))
            elif time11 == "12 to 6":
                c  = datetime.strptime(f2[i][5],"%H:%M")
                if c.hour>=before12.hour and c.hour<after6.hour:
                    searchres1.append((f2[i]))
            elif time11 =='after6':
                c  = datetime.strptime(f2[i][5],"%H:%M")
                if c.hour>=after6.hour:
                    searchres1.append((f2[i]))
            else:
                searchres1.append((f2[i]))
    print(searchres1)
    return jsonify(searchres1)
class student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name1 = db.Column(db.String(100))
    class1 = db.Column(db.String(100))
db.create_all()

@app.route('/stud', methods=['POST'])
def stude():
    data = request.get_json()
    print(data)
    a1 = data['name1'] 
    a2 = data['class1']
    userd = student(name1= a1,class1 = a2)
    db.session.add(userd)
    db.session.commit()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)