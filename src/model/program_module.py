from google.appengine.ext import db
from datetime import datetime

class ProgramModule(db.Model):
    name = db.StringProperty(indexed=True)
    units = db.StringListProperty(indexed=False)
    start_date = db.DateTimeProperty(indexed=False)

    @property
    def completed(self):
        return self.start_date < datetime.now()