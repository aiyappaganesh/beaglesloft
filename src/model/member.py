import random
import logging
from google.appengine.ext import db
from google.appengine.ext import blobstore
from webapp2_extras.security import generate_password_hash, check_password_hash


class Member(db.Model):
    email = db.StringProperty()
    name = db.StringProperty(indexed=False)
    designation = db.StringProperty(indexed=False)
    organization = db.StringProperty(indexed=False)
    website = db.StringProperty(indexed=False)
    twitter_handle = db.StringProperty(indexed=False)
    facebook_id = db.StringProperty(indexed=False)
    bio = db.TextProperty(indexed=False)
    influence_score = db.RatingProperty(indexed=False)
    activity_score = db.RatingProperty(indexed=False)
    proficiency_score = db.RatingProperty(indexed=False)
    image = db.StringProperty(indexed=False)
    password = db.StringProperty(indexed=False)
    image_coords = db.ListProperty(float, indexed=False)

    @classmethod
    def get_or_insert(cls, key_name, **kwds):
        kwds['email'] = key_name
        return super(Member, cls).get_or_insert(key_name, **kwds)

    @classmethod
    def create_or_update(cls, email, name=None, organization=None, designation=None, website=None,
                      twitter_handle=None, facebook_id=None, bio=None, image=None, password=None, image_coords=None):
        member = Member.get_by_email(email)
        if not member:
            member = Member(key_name=email)
        if name != None:
            member.name = name
        if email != None:
            member.email = email
        if designation != None:
            member.designation = designation
        if organization != None:
            member.organization = organization
        if website != None:
            member.website = website
        if twitter_handle != None:
            member.twitter_handle = twitter_handle
        if facebook_id != None:
            member.facebook_id = facebook_id
        if bio != None:
            member.bio = bio
        if image != None:
            if member.image:
                Member.delete_image(member.image)
            member.image = image
        if image_coords != None:
            member.image_coords = image_coords
        if password != None:
            member.password = generate_password_hash(password)
        member.influence_score = random.randint(0, 100)
        member.activity_score = random.randint(0, 100)
        member.proficiency_score = random.randint(0, 100)
        member.put()

    @staticmethod
    def get_by_email(email):
        return Member.get_by_key_name(email)

    @staticmethod
    def get_member_json(email):
        member_json = {}
        if email:
            member = Member.get_by_email(email)
            if member:
                member_json['email'] = member.email
                if member.name:
                    member_json['name'] = member.name
                if member.designation:
                    member_json['designation'] = member.designation
                if member.organization:
                    member_json['organization'] = member.organization
                if member.website:
                    member_json['website'] = member.website
                if member.twitter_handle:
                    member_json['twitter_handle'] = member.twitter_handle
                if member.facebook_id:
                    member_json['facebook_id'] = member.facebook_id
                if member.image:
                    member_json['image'] = member.image
                if member.bio:
                    member_json['bio'] = member.bio
                if member.influence_score:
                    member_json['influence_score'] = member.influence_score
                if member.activity_score:
                    member_json['activity_score'] = member.activity_score
                if member.proficiency_score:
                    member_json['proficiency_score'] = member.proficiency_score
        return member_json

    @staticmethod
    def get_member_keys():
        member_keys = {}
        members = Member.all().fetch(limit=200)
        for member in members:
            if not member.email in member_keys:
                member_keys[member.email] = []
            member_keys[member.email].append(member.image)
            member_keys[member.email].append(member.facebook_id)
        return member_keys

    @staticmethod
    def get_paged_member_keys():
        paged_member_keys = []
        page = []
        members = Member.all().fetch(limit=200)
        c1 = 0
        for member in members:
            paged_member = []
            paged_member.append(member.email)
            paged_member.append(member.image)
            paged_member.append(member.facebook_id)
            paged_member.append(c1+1)
            if len(page) >= 7:
                paged_member_keys.append(page)
                page = []
            page.append(paged_member)
            c1+=1
        paged_member_keys.append(page)
        logging.info(paged_member_keys)
        return paged_member_keys

    @staticmethod
    def get_members_json():
        members_json = {}
        members = Member.all().fetch(limit=200)
        for member in members:
            members_json[member.email] = Member.get_member_json(member.email)
        return members_json

    @classmethod
    def delete_image(cls, key):
        blobstore.delete(key)