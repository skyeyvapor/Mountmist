from flask import Flask, url_for, request, render_template #import Flask class from flask module in virtualenv
#request function will have all the data from the client to the server
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
      return "Welcome back, %s" % request.form.get('username')
    else:
      error = "Incorrect username and password"
    #return "User %s logged in" % request.form['username']
  #else:
  #  return '<form method="post" action="/login"><input type="text" name="username" /><p><button type="submit">Submit</button>'
  return render_template('login.html', error=error)

def valid_login(username, password):
	# check on the db if the username and password correct
	if username == password:
		return True
	else:
		return False

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



#underscore
if __name__ == '__main__': #if the name of this file that's running is = __main__, which means that's been run from the terminal
#if application is runned from the shell
  app.debug = True #you can see the change save right after 
  #=app.run(debug=True)
  app.run() #go ahead and run, or start a server
	#otherwise doesn't make any sense to the python shell, cause that you will not see anything