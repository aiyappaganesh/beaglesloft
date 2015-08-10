import json
from google.appengine.ext import db

class Expert(db.Model):
    name = db.StringProperty(indexed=False)
    bio = db.TextProperty(indexed=False)
    image = db.StringProperty(indexed=False)

    @classmethod
    def create(cls, email, name=name, bio=bio, image=image):
        cls(key_name=email, name=name, bio=bio, image=image).put()

    @property
    def email(self):
        return self.key().name()

    @property
    def _json(self):
        return json.dumps({'name': self.name, 'bio': self.bio})

    @staticmethod
    def get_paged_expert_keys():
        paged_member_keys = []
        page = []
        members = Expert.all().fetch(limit=200)
        c1 = 0
        for member in members:
            paged_member = []
            paged_member.append(member.email)
            paged_member.append(member.image)
            # paged_member.append(member.facebook_id)
            paged_member.append(c1+1)
            if len(page) >= 7:
                paged_member_keys.append(page)
                page = []
            page.append(paged_member)
            c1+=1
        paged_member_keys.append(page)
        return paged_member_keys