from google.appengine.ext import db

class Track(db.Model):
    name = db.StringProperty(indexed=False)
    image = db.StringProperty(indexed=False)
    order = db.IntegerProperty(indexed=True)

    @property
    def icon(self):
        return '/assets/img/tracks/' + self.image + '.png'
    
    @property
    def highlight_icon(self):
        return '/assets/img/tracks/' + self.image + '_dark.png'

    @property
    def id(self):
        return self.key().name()
    
    @classmethod
    def create(cls, track_id):
        cls(key_name=track_id).put()