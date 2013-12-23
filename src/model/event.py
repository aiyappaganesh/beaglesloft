from google.appengine.ext import db
from datetime import datetime, timedelta

date_format = '%b. %d %Y'
time_format = "%I:%M%p"

class Event(db.Model):
    name = db.StringProperty(indexed=False)
    type = db.StringProperty()
    date_time = db.DateTimeProperty()
    duration = db.IntegerProperty(indexed=False)
    link = db.StringProperty(indexed=False)
    description = db.TextProperty(indexed=False)
    snapshot = db.StringProperty(indexed=False)

    def json(self):
        event_json = dict()
        event_json['name'] = self.name
        event_json['type'] = self.type
        event_json['date'] = (self.date_time + timedelta(hours=5, minutes=30)).strftime(date_format)
        event_json['time'] = "%s - %s"%((self.date_time + timedelta(hours=5, minutes=30)).strftime(time_format),
                                        (self.date_time + timedelta(hours=self.duration) + timedelta(hours=5, minutes=30)).strftime(time_format))
        event_json['description'] = self.description
        event_json['link'] = self.link
        event_json['snapshot'] = self.snapshot
        return event_json

    @staticmethod
    def get_events(type=None):
        events_json = []
        query = Event.all()
        if type:
            query = query.filter('type =', type)
        events = query.order('-date_time').fetch(limit=200)
        if events:
            for event in events:
                events_json.append(Event.get_event_json(event))
        return events_json