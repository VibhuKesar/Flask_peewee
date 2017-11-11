from peewee import *
import datetime

db = SqliteDatabase('posts.db')

class Post(Model):
	id = PrimaryKeyField()
	date = DateTimeField(default = datetime.datetime.now)
	title = CharField()
	text = TextField()

	class Meta:
		database = db # to be db object

def initialize_db():
	db.connect()
	db.create_tables([Post], safe=True)
