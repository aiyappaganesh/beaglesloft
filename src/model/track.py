from google.appengine.ext import db

class Track(db.Model):

    @property
    def id(self):
        return self.key().name()
    
    @classmethod
    def create(cls, track_id):
        cls(key_name=track_id).put()