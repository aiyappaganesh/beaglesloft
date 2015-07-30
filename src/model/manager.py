from google.appengine.ext import db

class Manager(db.Model):
	user = db.ReferenceProperty(indexed=False)

	@classmethod
	def create(cls, email):
		cls(key_name=email).put()