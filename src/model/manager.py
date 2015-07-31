from google.appengine.ext import db

class Manager(db.Model):
    user = db.ReferenceProperty(indexed=False)

    @classmethod
    def create(cls, user):
        cls(key_name=user.email, user=user).put()

    @classmethod
    def get_managers(cls):
        managers = Manager.all().fetch(limit=50)
        return [(manager.user.email,manager.user.name) for manager in managers]

    @classmethod
    def _for(cls, email):
        return Manager.get_by_key_name(email)