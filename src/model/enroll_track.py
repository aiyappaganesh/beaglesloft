from google.appengine.ext import db

class EnrollTrack(db.model):
    engagement = db.FloatProperty(indexed=False)
    completed_courses = db.IntegerProperty(indexed=False)

    @classmethod
    def create(cls, member, track):
        cls(key_name=member.email, parent=track).put()