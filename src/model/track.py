from google.appengine.ext import db

class Track(db.Model):
    id = db.StringProperty()

    @classmethod
    def create(cls, track_id):
        cls(id=track_id).put()