from google.appengine.ext import db
from model.manager import Manager

class ManagedUser(db.Model):
    user = db.ReferenceProperty(indexed=False)

    @classmethod
    def create(cls, user, manager):
        cls(key_name=user.email, parent=manager, user=user).put()

    @classmethod
    def get_managed_users(cls, manager_email):
        return ManagedUser.all().ancestor(Manager._for(manager_email)).fetch(limit=50)