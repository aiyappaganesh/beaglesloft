from google.appengine.ext import db

class Expert(db.Model):
    name = db.StringProperty(indexed=False)
    bio = db.TextProperty(indexed=False)
    image = db.StringProperty(indexed=False)

    @classmethod
    def create(cls, email, name=name, bio=bio, image=image):
        cls(key_name=email, name=name, bio=bio, image=image).put()

    @property
    def email(self):
        return self.key().name()
    