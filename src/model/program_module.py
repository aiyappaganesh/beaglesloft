from google.appengine.ext import db

class ProgramModule(db.Model):
    name = db.StringProperty(indexed=True)
    units = db.StringListProperty(indexed=False)
    start_date = db.DateTimeProperty(indexed=False)
