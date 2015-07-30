from google.appengine.ext import db

class ManagedUser(db.Model):
	user = db.ReferenceProperty(indexed=False)

	@classmethod
	def create(cls, user, manager):
		cls(key_name=user.email, parent=manager, user=user).put()