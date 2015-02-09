import urllib
import json
import logging
from handlers.rest.rest_application import RestApplication
from handlers import RequestHandler
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.api import mail
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

class SendNewsletterConfirmationEmail(RequestHandler):
    def post(self):
        firstname = str(self['fname'])
        lastname = str(self['lname'])
        to_email = str(self['email'])

        if to_email:
            logging.info('Trying to subscribe: '+firstname+' '+lastname+' with email: '+to_email)
            from_email = "Niranjan Salimath <ranju@beaglesloft.com>"
            subject = "Confirm your Beaglesloft newsletter subscription"
            body = """Hey %s! \nThank you for signing up to the BeaglesLoft Newsletter. Please access the following link to confirm your subscription. http://www.beaglesloft.com/confirm_subscribe_newsletter?email=%s&firstname=%s&lastname=%s . \nNiranjan Salimath""" % (firstname+' '+lastname, to_email, firstname, lastname)
            mail.send_mail(from_email, to_email, subject, body)
            self.write(json.dumps({'status':'success', 'email':to_email}),200,'application/json')

app = RestApplication([("/api/common/download_image/([^/]+)",ImageDownloadHandler),
                       ("/api/common/save_newsletter",CreateNewsletterHandler),
                       ("/api/common/subscribe_to_newsletter",SendNewsletterConfirmationEmail)])