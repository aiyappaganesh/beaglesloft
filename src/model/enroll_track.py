from google.appengine.ext import db
from model.track import Track

class EnrollTrack(db.Model):
    engagement = db.FloatProperty(indexed=False)
    completed_courses = db.IntegerProperty(indexed=False)

    @classmethod
    def create(cls, member, track):
        cls(key_name=member.email, parent=track).put()

    @classmethod
    def is_enrolled(cls, email, track_id):
        return EnrollTrack.get_by_key_name(email, parent=Track.get_by_key_name(track_id))