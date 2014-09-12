import urllib
from handlers.rest.rest_application import RestApplication
from handlers import RequestHandler
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
from model import Newsletter
from datetime import datetime

class ImageDownloadHandler(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self, picture_key):
        if picture_key:
            resource = str(urllib.unquote(picture_key))
            blob_info = blobstore.BlobInfo.get(resource)
            self.send_blob(blob_info)
            return

class CreateNewsletterHandler(blobstore_handlers.BlobstoreUploadHandler, RequestHandler):
    def post(self):
        snapshot = self.get_uploads("snapshot")
        snapshot_key = str(snapshot[0].key()) if snapshot else None
        date_time = self['date_time']
        link = self['link']
        Newsletter.get_or_insert(date_time, link=link, date_time=datetime.strptime(date_time,"%Y-%m-%dT%H:%M"), snapshot=snapshot_key)
        self.redirect("/newsletters")

app = RestApplication([("/api/common/download_image/([^/]+)",ImageDownloadHandler),
                       ("/api/common/save_newsletter",CreateNewsletterHandler)])