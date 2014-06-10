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

app = RestApplication([("/api/events/save_event",CreateEventHandler)])