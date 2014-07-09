import logging
import json
import random
import time
from time import mktime
from datetime import datetime
from handlers.rest.rest_application import RestApplication
from handlers import RequestHandler
from model import Event
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers

class CreateEventHandler(blobstore_handlers.BlobstoreUploadHandler, RequestHandler):
    def post(self):
        snapshot = self.get_uploads("snapshot")
        snapshot_key = str(snapshot[0].key()) if snapshot else None
        name = self['name']
        type = self['type']
        description = self['description']
        date_time = self['date_time']
        duration = int(self['duration'])
        link = self['link']
        attendees = int(self['attendees'] if self['attendees'] else 0)
        Event.get_or_insert(type+date_time, name=name, type=type, description=description, duration=duration, link=link,
                            date_time=datetime.strptime(date_time,"%Y-%m-%dT%H:%M"), snapshot=snapshot_key, attendees=attendees)
        self.redirect("/")

class EditEventHandler(blobstore_handlers.BlobstoreUploadHandler, RequestHandler):
    def post(self):
        snapshot = self.get_uploads("snapshot")
        snapshot_key = str(snapshot[0].key()) if snapshot else None
        name = self['name']
        description = self['description']
        duration = int(self['duration'])
        link = self['link']
        attendees = int(self['attendees'] if self['attendees'] else 0)
        key = self['key']
        event = Event.get(key)
        if event:
            event.update(name=name, description=description, duration=duration, link=link, snapshot=snapshot_key, attendees=attendees)
        self.redirect("/events/search_event")

class DeleteEventHandler(RequestHandler):
    def post(self):
        key = self['id']
        event = Event.get(key)
        if event:
            event.delete()

class SearchEventHandler(RequestHandler):
    def post(self):
        type = self['type']
        events = Event.get_all_events(type)
        self.write(json.dumps({'events':events}), 200, "application/json")

app = RestApplication([("/api/events/save_event",CreateEventHandler),
                       ("/api/events/edit_event",EditEventHandler),
                       ("/api/events/delete_event",DeleteEventHandler),
                       ("/api/events/search",SearchEventHandler)])