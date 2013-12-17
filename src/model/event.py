from google.appengine.ext import db

class Event(db.Model):
    name = db.StringProperty(indexed=False)
    type = db.StringProperty()
    date_time = db.DateTimeProperty()
    link = db.StringProperty(indexed=False)
    snapshot = db.StringProperty(indexed=False)

    @staticmethod
    def get_event_json(event):
        event_json = {}
        if event:
            event_json['name'] = event.name
            event_json['type'] = event.type
            event_json['date_time'] = event.date_time
            event_json['link'] = event.link
            event_json['snapshot'] = event.snapshot
        return event_json

    @staticmethod
    def get_events(type):
        events_json = []
        query = Event.all()
        if type:
            query = query.filter('type =', type)
        events = query.order('-date_time').fetch(limit=200)
        if events:
            for event in events:
                events_json.append(Event.get_event_json(event))
        return events_json