from google.appengine.ext import db

class Track(db.Model):

    @classmethod
    def create(cls, track_id):
        cls(key_name=track_id).put()