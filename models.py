from peewee import * #all the functions import
import datetime

db = SqliteDatabase('posts.db')	#connect db

class Post(Model):
	id = PrimaryKeyField()
	date = DateTimeField(default = datetime.datetime.now) #combo of data and time from class,, current
	title = CharField()	#arg. can be unique=True
	text = TextField()	

	class Meta:	#meta class to specify database to be as db object
		database = db

def initialize_db():
	db.connect()
	db.create_tables([Post], safe=True)