from google.appengine.ext import db
from datetime import datetime

class Program(db.Model):
    name = db.StringProperty(indexed=False)
    description = db.StringProperty(indexed=False)
    image = db.StringProperty(indexed=False)
    slots = db.IntegerProperty(indexed=False)
    start_date = db.DateTimeProperty(indexed=True)
    expert = db.ReferenceProperty()

    @db.transactional
    def block_slot(self):
        if self.slots > 0:
            self.slots = self.slots - 1
            self.put()

    @property
    def id(self):
        return self.key().name()

    @property
    def url(self):
        return '/tracks/program_listing?program_id=%s&track_id=%s'%(self.id, self.parent().id)

    @property
    def formatted_start_date(self):
        return self.start_date.strftime('%b %d %Y')
