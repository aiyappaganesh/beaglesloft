from google.appengine.ext import db
from datetime import datetime

class Program(db.Model):
    name = db.StringProperty(indexed=False)
    description = db.StringProperty(indexed=False)
    image = db.StringProperty(indexed=False)
    slots = db.IntegerProperty(indexed=False)
    start_date = db.DateTimeProperty(indexed=False)

    @property
    def id(self):
        return self.key().name()

    @property
    def url(self):
        return '/tracks/program_listing?id=' + self.id

    @property
    def formatted_start_date(self):
        return self.start_date.strftime('%b %d %Y')
