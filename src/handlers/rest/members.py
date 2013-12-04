import logging
import json
import random
from handlers.rest.rest_application import RestApplication
from handlers import RequestHandler
from model import Member

class MemberSaveHandler(RequestHandler):
    def post(self):
        logging.info("Trying to save member")
        email = self["email"]
        if email:
            name = self["name"]
            designation = self["designation"]
            organization = self["organization"]
            website = self["website"]
            twitter_handle = self["twitter_handle"]
            facebook_id = self["facebook_id"]
            bio = self["bio"]
            influence_score = self["influence_score"]
            activity_score = self["activity_score"]
            proficiency_score = self["proficiency_score"]
            access_code = self["access_code"]
            member = Member.get_or_insert(email)
            if member:
                if name:
                    member.name = name
                if designation:
                    member.designation = designation
                if organization:
                    member.organization = organization
                if website:
                    member.website = website
                if twitter_handle:
                    member.twitter_handle = twitter_handle
                if facebook_id:
                    member.facebook_id = facebook_id
                if bio:
                    member.bio = bio
                member.influence_score = random.randint(0, 100)
                member.activity_score = random.randint(0, 100)
                member.proficiency_score = random.randint(0, 100)
                member.put()
                self.redirect("/")
            else:
                self.write("Member could not be found or created", status=500)
        else:
            self.write("Please provide an email", status=400)

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
        access_answer = self["access_answer"]
        question_id = self["qid"]
        logging.info(access_answer + ',' + question_id)
        if question_id and access_answer:
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
            result_json['question'] = 'If 10 men can build 10 houses in 10 days, how many houses can 1 man build in 10 days?'
            result_json['question_id'] = 'B1'
        elif category == 'Art':
            result_json['question'] = 'If 10 men can build 10 houses in 10 days, how many houses can 1 man build in 10 days?'
            result_json['question_id'] = 'A1'
        self.write(
            json.dumps(
                result_json
            ),200,'application/json'
        )

app = RestApplication([("/api/members/save_member", MemberSaveHandler),
                       ("/api/members/get_member", MemberFetchHandler),
                       ("/api/members/get_all_members", AllMembersFetchHandler),
                       ("/api/members/validate_access_code", ValidateAccessCodeHandler),
                       ("/api/members/process_access_answer", ProcessAccessAnswerHandler),
                       ("/api/members/fetch_access_question", FetchAccessQuestionHandler)])