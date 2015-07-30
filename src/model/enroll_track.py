from google.appengine.ext import db

class EnrollTrack(db.model):
    @classmethod
    def create(cls, member, track):
        cls(key_name=member.email, parent=track).put()