from google.appengine.ext import db

class ProgramModule(db.Model):
    name = db.StringProperty(indexed=False)
    units = db.StringListProperty(indexed=False)


