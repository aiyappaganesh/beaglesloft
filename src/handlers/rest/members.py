import logging
import json
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
import random
from handlers.rest.rest_application import RestApplication
from handlers import RequestHandler
from model import Member
from handlers.sessions import BaseHandler
from auth import login_required

class MemberSaveHandler(blobstore_handlers.BlobstoreUploadHandler, RequestHandler):
    def post(self):
        image = self.get_uploads("member-image")
        image_key = str(image[0].key()) if image else None
        Member.create_or_update(email=self["email"], name=self['name'], organization=self["organization"],
                                designation=self["designation"], image=image_key, website=self["website"],
                                twitter_handle=self["twitter_handle"], facebook_id=self["facebook_id"], bio=self["bio"],
                                password=self['password'])
        self.redirect("/")

class MemberFetchHandler(RequestHandler):
    def post(self):
        logging.info("Trying to fetch member")
        email = self["email"]
        member_json = Member.get_member_json(email)
        self.write(
            json.dumps(
                member_json
            ),200,'application/json'
        )

class AllMembersFetchHandler(RequestHandler):
    def post(self):
        logging.info("Trying to fetch all members")
        members_json = Member.get_members_json()
        self.write(
            json.dumps(
                members_json
            ),200,'application/json'
        )

class ValidateAccessCodeHandler(RequestHandler):
    def post(self):
        logging.info("Trying to validate access code")
        result_json = {'url':''}
        access_code = self["accessCode"]
        logging.info(access_code)
        if access_code and int(access_code) == 1234:
            result_json['url'] = '/member_registration'
        self.write(
            json.dumps(
                result_json
            ),200,'application/json'
        )

class ProcessAccessAnswerHandler(RequestHandler):
    def post(self):
        logging.info("Trying to process access answer")
        result_json = {'url':''}
        access_answer = str(self["access_answer"])
        question_id = str(self["qid"])
        logging.info(access_answer + ',' + question_id)
        if question_id and access_answer:
            if question_id == 'M1':
                if access_answer=='1' or access_answer.lower().strip()=='one':
                    result_json['url'] = '/member_registration'
            elif question_id == 'S1':
                if access_answer.lower().strip().find('higg')!=-1 or access_answer.lower().strip().find('boson')!=-1:
                    result_json['url'] = '/member_registration'
            elif question_id == 'B1':
                if access_answer.lower().strip().find('whiskey')!=-1 or access_answer.lower().strip().find('whisky')!=-1:
                    result_json['url'] = '/member_registration'
            elif question_id == 'A1':
                if access_answer.lower().strip().find('acrylic')!=-1:
                    result_json['url'] = '/member_registration'
        self.write(
            json.dumps(
                result_json
            ),200,'application/json'
        )

class FetchAccessQuestionHandler(RequestHandler):
    def post(self):
        logging.info("Trying to provide access question")
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

class ImageHandler(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self, email):
        member = Member.get_by_email(email)
        if member and member.image:
            image = blobstore.BlobInfo.get(member.image)
            self.send_blob(image)

app = RestApplication([ ("/api/members/save_member", MemberSaveHandler),
                        ("/api/members/get_member", MemberFetchHandler),
                        ("/api/members/([^/]+)/image", ImageHandler),
                        ("/api/members/get_all_members", AllMembersFetchHandler),
                        ("/api/members/validate_access_code", ValidateAccessCodeHandler),
                        ("/api/members/process_access_answer", ProcessAccessAnswerHandler),
                        ("/api/members/fetch_access_question", FetchAccessQuestionHandler)])
