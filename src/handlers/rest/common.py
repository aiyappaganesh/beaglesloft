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
from util import mailjet
from model.program import Program
from model.track import Track
from model.expert import Expert

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
            result = mailjet.send_mail(from_email, to_email, subject, body)
            if result['id'] != -1:
                self.write(json.dumps({'status':'success', 'email':to_email}),200,'application/json')
            else:
                self.write(json.dumps({'status':'error', 'email':to_email, 'name':result['error']}),200,'application/json')

class SaveAssociationHandler(RequestHandler):
    def post(self):
        track_id = self['track']
        program_id = self['program']
        expert_email = self['expert']
        program = Program.get_by_key_name(program_id, parent=Track.get_by_key_name(track_id))
        program.expert = Expert.get_by_key_name(expert_email)
        program.put()
        self.redirect("/tracks/program_listing?program_id=%s&track_id=%s"%(program_id, track_id))

app = RestApplication([("/api/common/download_image/([^/]+)",ImageDownloadHandler),
                       ("/api/common/save_newsletter",CreateNewsletterHandler),
                       ("/api/common/subscribe_to_newsletter",SendNewsletterConfirmationEmail),
                       ("/api/common/save_association", SaveAssociationHandler)])