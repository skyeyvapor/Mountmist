from flask import Flask #import Flask class from flask module in virtualenv
app = Flask(__name__) #instantiate Flask by passing a identifier(here we use MAGICAL __name__ which means name of this file as it was called. it is called from shell )
# (you can have mutiple Flask applications at the same time)
'''
@app.route('/') #@ is called decorator, which modify the following function on the next line
#if someone hits the /, or top level of this app 
def index(): #it does when user hits the / (the top folder) then call this function
	return 'Index Page'
'''
@app.route('/hello')
def hello():
	return 'Hello World'

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