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
        event_json['date'] = (self.date_time).strftime(date_format)
        event_json['time'] = "%s - %s"%((self.date_time).strftime(time_format),
                                        (self.date_time + timedelta(hours=self.duration)).strftime(time_format))
        event_json['description'] = self.description
        event_json['link'] = self.link
        event_json['snapshot'] = self.snapshot
        return event_json

    @staticmethod
    def get_events(type=None):
        past_events = []
        upcoming_events = []
        for event in Event.all().order('-date_time'):
            if event.date_time < datetime.now():     #change to gmt+530
                past_events.append(event.json())
            elif event.date_time >= datetime.now():
                upcoming_events.append(event.json())
        return upcoming_events, past_events

    @staticmethod
    def get_paged_events(type=None):
        past_events = {}
        past_events_temp = []
        upcoming_events = []
        for event in Event.all().order('-date_time'):
            if event.date_time < datetime.now():     #change to gmt+530
                past_events_temp.append(event.json())
            elif event.date_time >= datetime.now():
                upcoming_events.append(event.json())
        if past_events_temp:
            counter = 0
            for event in past_events_temp:
                if not counter/3 in past_events:
                    past_events[counter/3] = []
                past_events[counter/3].append(event)
                counter+=1
        return upcoming_events, past_events