from google.appengine.ext import db

class Manager(db.Model):
	user = db.ReferenceProperty(indexed=False)

	@classmethod
	def create(cls, user):
		cls(key_name=user.email, user=user).put()