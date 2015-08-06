import logging
import json
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.api import images
from handlers.rest.rest_application import RestApplication
from handlers import RequestHandler
from model import Member
from auth import login_required
from handlers.web import WebRequestHandler
from webapp2_extras.security import generate_password_hash, check_password_hash
from config.config import *
from util import mailchimp
from util.util import MEMBER_ROLE, MANAGER, ENGINEER
from model.manager import Manager
from model.managed_user import ManagedUser
from model.enroll_program import EnrollProgram
from model.program import Program
from model.track import Track

class MemberCreateHandler(RequestHandler):
    def post(self):
        key = self['email']
        redirect_url = str(self['redirect_url']) if self['redirect_url'] else '/community'
        if self['fb-pic-checkbox']:
            image_url = 'https://graph.facebook.com/'+self["facebook_id"]+'/picture?type=normal&height=300&width=300'
        else:
            image_url = '/assets/img/landing/default_member.png'
        role = int(self['role']) if self['role'] else MEMBER_ROLE[ENGINEER]
        member = Member.create_or_update(key, name=self['name'], organization=self["organization"],
                                designation=self["designation"], website=self["website"],
                                twitter_handle=self["twitter_handle"], facebook_id=self["facebook_id"], bio=self["bio"],
                                password=self['password'], image_url=image_url, role=role)
        self.session['member'] = key
        redirect_url = '/tracks'
        if role == MEMBER_ROLE[MANAGER]:
            Manager.create(member)
        else:
            managed_by = self['manager']
            ManagedUser.create(member, Manager._for(managed_by))
        self.redirect(redirect_url)

class AddMemberEmailHandler(RequestHandler):
    def post(self):
        key = self['email']
        Member.create_or_update(key)


class MemberUpdateHandler(blobstore_handlers.BlobstoreUploadHandler, RequestHandler):
    @login_required
    def post(self, email):
        if not self.session['member'] == email:
            self.response.out.write('access denied')
            return
        image = self.get_uploads("member-image-upload")
        image_key = str(image[0].key()) if image else None
        image_coords = [float(coord) for coord in self['image_coords'].split(',')] if self['image_coords'] else None
        key = email if email else self['email']
        image_url = '/api/members/'+key+'/image' if image_key else None
        Member.create_or_update(key, name=self['name'], organization=self["organization"],
                                designation=self["designation"], image=image_key, website=self["website"],
                                twitter_handle=self["twitter_handle"], facebook_id=self["facebook_id"], bio=self["bio"],
                                password=self['password'], image_coords=image_coords, image_url=image_url)
        self.redirect("/members/profile")


class MemberFetchHandler(RequestHandler):
    def post(self):
        email = self["email"]
        member_json = Member.get_member_json(email)
        #if not 'member' in self.session:
        #    member_json['website'] = ''
        #    member_json['twitter_handle'] = ''
        self.write(
            json.dumps(
                member_json
            ),200,'application/json'
        )


class AllMembersFetchHandler(RequestHandler):
    def post(self):
        members_json = Member.get_members_json()
        self.write(
            json.dumps(
                members_json
            ),200,'application/json'
        )


class ValidateAccessCodeHandler(WebRequestHandler):
    def post(self):
        result_json = {'url':''}
        access_code = self["accessCode"]
        if access_code and access_code == coded_access:
            self.session['access_code'] = access_code
            result_json['url'] = '/member_registration'
        self.write(
            json.dumps(
                result_json
            ),200,'application/json'
        )

class ProcessAccessAnswerHandler(RequestHandler):
    def post(self):
        result_json = {'url':''}
        access_answer = str(self["access_answer"])
        question_id = str(self["qid"])
        if question_id and access_answer:
            if question_id == 'M1':
                if access_answer=='1' or access_answer.lower().strip()=='one':
                    self.session['access_code'] = coded_access
                    result_json['url'] = '/member_registration'
            elif question_id == 'S1':
                if access_answer.lower().strip().find('higg')!=-1 or access_answer.lower().strip().find('boson')!=-1:
                    self.session['access_code'] = coded_access
                    result_json['url'] = '/member_registration'
            elif question_id == 'B1':
                if access_answer.lower().strip().find('whiskey')!=-1 or access_answer.lower().strip().find('whisky')!=-1:
                    self.session['access_code'] = coded_access
                    result_json['url'] = '/member_registration'
            elif question_id == 'A1':
                if access_answer.lower().strip().find('acrylic')!=-1:
                    self.session['access_code'] = coded_access
                    result_json['url'] = '/member_registration'
        self.write(
            json.dumps(
                result_json
            ),200,'application/json'
        )

class FetchAccessQuestionHandler(RequestHandler):
    def post(self):
        result_json = {'question':'If 10 men can build 10 houses in 10 days, how many houses can 1 man build in 10 days?','question_id':'O1'}
        category = self['category']
        if category == 'Mathematics':
            result_json['question'] = 'If 10 men can build 10 houses in 10 days, how many houses can 1 man build in 10 days?'
            result_json['question_id'] = 'M1'
        elif category == 'Science':
            result_json['question'] = 'The Large Hadron Collider (LHC) was built to confirm the existence of which particle?'
            result_json['question_id'] = 'S1'
        elif category == 'Business':
            result_json['question'] = "With what product did the term 'brand name' originate?"
            result_json['question_id'] = 'B1'
        elif category == 'Art':
            result_json['question'] = 'What kind of paint is made from pigments and plastic?'
            result_json['question_id'] = 'A1'
        self.write(
            json.dumps(
                result_json
            ),200,'application/json'
        )


class ImageHandler(blobstore_handlers.BlobstoreDownloadHandler, WebRequestHandler):
    def get(self, email):
        member = Member.get_by_email(email)
        if member and member.image:
            if member.image_coords:
                left_x, top_y, right_x, bottom_y = member.image_coords
                image = images.Image(blob_key=member.image)
                image.crop(left_x=left_x, top_y=top_y, right_x=right_x, bottom_y=bottom_y)
                self.response.headers['Content-Type'] = 'image/png'
                self.response.out.write(image.execute_transforms())
            else:
                image = blobstore.BlobInfo.get(member.image)
                self.send_blob(image)

class LoginHandler(RequestHandler):
    def post(self):
        result_json = {'redirect_url': str(self['redirect_url']) if self['redirect_url'] else '/community', 'error': False}
        email = self['email']
        password = self['password'] if self['password'] else None
        member = Member.get_by_email(email)
        if 'member' in self.session and not email is self.session['member']:
            del self.session['member']
        if not email or not member:
            result_json['error'] = True
            result_json['errormsg'] = 'Member not found'
        elif not check_password_hash(password, member.password):
            result_json['error'] = True
            result_json['errormsg'] = 'Incorrect password'
        else:
            self.session['member'] = email
            redirect_url = '/tracks'
            result_json['redirect_url'] = redirect_url
        self.write(
            json.dumps(
                result_json
            ),200,'application/json'
        )

class SubscribeNewsletterHandler(RequestHandler):
    def post(self):
        email = self['email']
        fname = self['fname']
        lname = self['lname']
        if email:
            logging.info('Trying to subscribe: '+fname+' '+lname+' with email: '+email)
            res = mailchimp.subscribe(email,fname,lname).content
            logging.info('Subscription Result: '+res)
            self.write(
                json.dumps(
                    res
                ),200,'application/json'
            )

class EnrollTrackHandler(RequestHandler):
    @login_required
    def post(self):
        email = self.session['member']
        track_id = self['track_id']
        program_id = self['program_id']
        program = Program.get_by_key_name(program_id, parent=Track.get_by_key_name(track_id))
        EnrollProgram.create(Member.get_by_email(email), program)
        self.redirect("/tracks/program_listing?program_id=%s&track_id=%s"%(program_id, track_id))

app = RestApplication([ ("/api/members/login", LoginHandler),
                        ("/api/members/([^/]+)/update", MemberUpdateHandler),
                        ("/api/members/create", MemberCreateHandler),
                        ("/api/members/add_email", AddMemberEmailHandler),
                        ("/api/members/get_member", MemberFetchHandler),
                        ("/api/members/([^/]+)/image", ImageHandler),
                        ("/api/members/get_all_members", AllMembersFetchHandler),
                        ("/api/members/validate_access_code", ValidateAccessCodeHandler),
                        ("/api/members/process_access_answer", ProcessAccessAnswerHandler),
                        ("/api/members/fetch_access_question", FetchAccessQuestionHandler),
                        ("/api/members/subscribe_to_newsletter", SubscribeNewsletterHandler),
                        ("/api/members/enroll", EnrollTrackHandler)])
