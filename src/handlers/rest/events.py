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
        logging.info('Trying to save event')
        snapshot = self.get_uploads("snapshot")
        snapshot_key = str(snapshot[0].key()) if snapshot else None
        name = self['name']
        type = self['type']
        date_time = self['date_time']
        link = self['link']
        Event.get_or_insert(type+date_time,name=name,type=type,date_time=datetime.fromtimestamp(mktime(time.strptime(date_time,"%Y-%m-%dT%H:%M"))),link=link, snapshot=snapshot_key)
        self.redirect("/")

app = RestApplication([("/api/events/save_event",CreateEventHandler)])