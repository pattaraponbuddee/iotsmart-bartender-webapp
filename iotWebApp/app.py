from flask import *
import prou
import RPi.GPIO as GPIO
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
GPIO.setmode(GPIO.BCM) #set up GPIO
prou.start()
cred = credentials.Certificate('mos.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
app = Flask(__name__) #set up flask server

@app.route('/')
def main():
	prou.start()
	return render_template('main.html')

@app.route('/<changepin>', methods=['POST'])
def reroute(changepin):

	changePin = int(changepin) #cast changepin to an int

	if changePin == 1:
		prou.drink1()
	elif changePin == 2:
		prou.drink2()
	elif changePin == 3:
		prou.drink3()
	elif changePin == 4:
		prou.drink4()
	elif changePin == 5:
		prou.drink5()
	elif changePin == 6:
		prou.drink6()
	elif changePin == 7:
		prou.drink7()
	elif changePin == 8:
		prou.drink8()
	elif changePin == 9:
		prou.shake()	
	
		


	response = make_response(redirect(url_for('index')))
	return(response)
	
@app.route('/regist' , methods=["GET", "POST"])
def regist():
	if request.method == "POST":
		username = request.form["uname"]
		telephone = request.form["phone"]
		email = request.form["email"]
		password = request.form["psw"]
		db.collection('user').add({'username':username,'password':password ,'email':email 
		,'Phonenumber':telephone , 'p1':0 , 'p2':0 , 'p3':0 , 'p4':0})
		return render_template('prelogin.html')	
	else:
		return render_template('re.html' )
	return render_template('re.html')	

@app.route('/login', methods=["GET", "POST"])
def login():
	if request.method == "POST":
		usernamelogin = request.form["username"]
		passwordlogin = request.form["password"]
		global x
		x = usernamelogin
		global y
		y = passwordlogin
		docs1 = db.collection('user').where("username","==",usernamelogin).get()
		docs2 = db.collection('user').where("password","==",passwordlogin).get()
		if docs1 != '' and docs2 != '' :
			print('loginsc')
			return redirect('/custom')	
	return render_template('login.html')





@app.route('/oldlogin', methods=["GET", "POST"])
def oldlogin():
	if request.method == "POST":
		usernamelogin = request.form["username"]
		passwordlogin = request.form["password"]
		global x
		x = usernamelogin
		global y
		y = passwordlogin
		docs1 = db.collection('user').where("username","==",usernamelogin).get()
		docs2 = db.collection('user').where("password","==",passwordlogin).get()
		if docs1 != '' and docs2 != '' :
			print('loginsc')
			return redirect('/custom')	
		
	return render_template('iot_login.html')


@app.route('/oldregist' , methods=["GET", "POST"])
def oldregist():
	if request.method == "POST":
		username = request.form["username"]
		Phonenumber = request.form["Phonenumber"]
		password = request.form["password"]
		db.collection('user').add({'username':username,'password':password
		,'Phonenumber':Phonenumber , 'p1':0 , 'p2':0 , 'p3':0 , 'p4':0})
		return render_template('prelogin.html')	
	else:
		return render_template('regist.html' )
	return render_template('regist.html' )
	
@app.route('/custom', methods=["GET", "POST"])
def custom():
	
	if request.method == "POST":
		print('sssssssssss')
		g1 = request.form["p1"]
		g2 = request.form["p2"]
		g3 = request.form["p3"]
		g4 = request.form["p4"]
		print(g1,g2,g3,g4)
		print(x,y)
		docs = db.collection('user').get()
		for doc in docs :
			if doc.to_dict()['username'] == str(x):
				global u1
				global u2
				global u3
				global u4
				u1 = float(g1)*(1/25)
				u2 = float(g2)*(1/25)
				u3 = float(g3)*(1/25)
				u4 = float(g4)*(1/25)
				
				key = doc.id
				db.collection('user').document(key).update({'p1':g1 , 'p2':g2 , 'p3':g3 , 'p4':g4})
				
				return redirect('/fill')		
	return render_template('custom.html')	

@app.route('/prelogin')
def prelogin():
	return render_template('prelogin.html')	

@app.route('/lastcustom')
def lastcumtom():
	return render_template('lastcustom.html')	
	

@app.route('/fill')
def fill():
	prou.custom1(u1)
	prou.custom2(u2)
	prou.custom3(u3)
	prou.custom4(u4)
	
	return redirect('/')

@app.route('/test')
def test():
	return render_template('test.html')

		

app.run(debug=True, host='0.0.0.0', port=80) #set up the server
