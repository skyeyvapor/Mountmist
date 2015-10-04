from flask import Flask, url_for, request, render_template, redirect, flash, make_response, session #import Flask class from flask module in virtualenv
import logging #python logging engine(module)
from logging.handlers import RotatingFileHandler #rotatingfilehander's rotating means creates new file and appends .1 on the other one
#url_for is for making a link's def link to another def #url_for('another_def', parameter='what_you_want_to_send')
#request will have all the data that passed from the client to the server  #can use request.values, request.method, request.form.get('')
#reder_template is for #render_template('the url', parameter=what_you_want_to_send)
#redirect is for #redirect(fuction) or #redirect(url_for())
#request function will have all the data from the client to the server
#flash is for flash messages
#session is more secure
#make_response: modify the http response the app sent, one of this is for cookie
app = Flask(__name__) #instantiate Flask by passing a identifier(here we use MAGICAL __name__ which means name of this file as it was called. it is called from shell )
# (you can have mutiple Flask applications at the same time)
'''
@app.route('/') #@ is called decorator, which modify the following function on the next line
#if someone hits the /, or top level of this app 
def index(): #it does when user hits the / (the top folder) then call this function
	return 'Index Page'
'''

#/blog?post=3 GET method
#/login POST method not visible info
@app.route('/login', methods=['GET', 'POST']) #the first method to render the form will be th GET request
def login():
  error = None
	#if request.values: #if have values
  if request.method == 'POST':
    #can check the method
    #return 'username is %s' % request.values['username']
    if valid_login( #can use request.form['username'] it's a list
      request.form.get('username'),
      request.form.get('password')
    ):
      flash("Successfully logged in")
      session['username'] = request.form.get('username') #session is a list
      #flash("Thanks for coming")
      response = make_response(redirect(url_for('welcome')))#first step is just redirect, store that don't send it yet
      response.set_cookie('username', request.form.get('username'))#response object set cookie on response
      #return "Welcome back, %s" % request.form.get('username')
      #return redirect(url_for('welcome', username=request.form.get('username')))
      #return response #now we return response
      return redirect(url_for('welcome'))
    else:
      error = "Incorrect username and password"
      app.logger.warning("Incorrect username and password for user (%s)", request.form.get("username"))
    #return "User %s logged in" % request.form['username']
  #else:
  #  return '<form method="post" action="/login"><input type="text" name="username" /><p><button type="submit">Submit</button>'
  return render_template('login.html', error=error) #can do error_form=error

#@app.route('/welcome/<username>') #make /welcome/whatever-you-type/ to def(whateveryoutype)
#def welcome(username):
#	return render_template('welcome.html', username=username)

@app.route('/logout')
def logout():
  #response = make_response(redirect(url_for('login')))
  #response.set_cookie('username', '', expires=0) #set username to be bland, and set third parameter which is expiration and set it to 0, which set cookie expired in the past 
  session.pop('username',None)
  return redirect(url_for('login'))
@app.route('/')
def welcome():
  #username = request.cookies.get("username")#read the cookie, and set it to the username value
  if 'username' in session:
    #ir username present
    return render_template('welcome.html', username=session['username'])
  else:
    return redirect(url_for('login'))



def valid_login(username, password):
	# check on the db if the username and password correct
	if username == password:
		return True
	else:
		return False
'''
@app.route('/profile/<username>')
def show_user_profile(username):
	#= return 'User: ' + str(username)
	return 'User: %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
	#return 'Post: ' + str(post_id)
	return 'Post: %d' % post_id

@app.route('/')
def show_url_for():
	return url_for('show_user_profile', username='jorge') #url_for is a function that can return show_user_profile function in above
'''


#underscore
if __name__ == '__main__': #if the name of this file that's running is = __main__, which means that's been run from the terminal
#if application is runned from the shell
  app.secret_key = 'SuperSecretKey'
  handler = RotatingFileHandler('error.log', maxBytes=10000, backupCount=1)
  handler.setLevel(logging.INFO)
  app.logger.addHandler(handler)
  app.debug = True #you can see the change save right after 
  #=app.run(debug=True)
  app.run() #go ahead and run, or start a server
	#otherwise doesn't make any sense to the python shell, cause that you will not see anything