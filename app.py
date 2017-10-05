from flask import Flask, render_template, request, redirect, url_for
from models import *

app = Flask(__name__)

@app.before_request
def before_request():
	#create db and connect
	initialize_db()

@app.teardown_request
def teardown_request(exception): #check if there was exception with args.
	db.close()

@app.route('/')
def index():
	#render homepage with saved posts
	return render_template('home.html', posts=Post.select().order_by(Post.date.desc))

@app.route('/new_post/')
def new_post():
	return render_template('new_post.html')

@app.route('/create/', methods=['POST']) #this method helps not to go directly to this by typing this link add. to URL, safe.
def create_post():
	#create new form
	Post.create(
	 #happen to be in dict. like
		title=request.form['title'],
		text=request.form['body']
	)

	#return the user to the homepage
	return redirect(url_for('index')) #or ('/')


if __name__ == '__main__':
	app.run(debug=True)


