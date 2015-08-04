from google.appengine.ext import db

class Program(db.Model):
    name = db.StringProperty(indexed=False)
    description = db.StringProperty(indexed=False)
    image = db.StringProperty(indexed=False)
    slots = db.IntegerProperty(indexed=False)
    start_date = db.DateTimeProperty(indexed=False)
