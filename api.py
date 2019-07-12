from flask import Flask,render_template,request,redirect,url_for,session

app=Flask(__name__)
app.secret_key='hello'

@app.route('/')
def hom():
 
	return render_template('hom.html',title='home')
 
@app.route('/about')
def about():
 
	return render_template('about.html',title='about')
 

@app.route('/contact')
def contact():
 
	return render_template('contact.html',title='contact')
 


@app.route('/login',methods=['GET','POST'])
def login():
	if request.method=='POST':
		users={'user1':'123','user2':'1234','user3':'12345'}
		username=request.form['username']
		password=request.form['password']
 
		if username not in users:
			return "user doesn't exist. go back and enter a valid username"
		if users[username]!=password:
			return "password doesn't match .go back and enter valid password"
		session['username']=username

 	
	return redirect(url_for('hom'))

@app.route('/logout')
def logout():
	session.clear()
	return redirect(url_for('hom'))
 
	

app.run(debug=True)
