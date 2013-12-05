import logging
from google.appengine.ext import db

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

    @classmethod
    def get_or_insert(cls, key_name, **kwds):
        kwds['email'] = key_name
        return super(Member, cls).get_or_insert(key_name, **kwds)

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
            member_keys[member.email] = member.facebook_id
        return member_keys

    @staticmethod
    def get_paged_member_keys():
        paged_member_keys = {}
        members = Member.all().fetch(limit=200)
        c1 = 0
        for member in members:
            if not c1/10 in paged_member_keys:
                paged_member_keys[c1/10] = {}
            paged_member_keys[c1/10][member.email] = member.facebook_id
            c1+=1
        return paged_member_keys

    @staticmethod
    def get_members_json():
        members_json = {}
        members = Member.all().fetch(limit=200)
        for member in members:
            members_json[member.email] = Member.get_member_json(member.email)
        return members_json