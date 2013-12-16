from handlers.rest.rest_application import RestApplication
from handlers.sessions import BaseHandler
from auth import login_required
from model import Member
#from handlers import RequestHandler
from google.appengine.api.blobstore import blobstore
from handlers.web import WebRequestHandler


class LoginHandler(BaseHandler, WebRequestHandler):
    def post(self):
        email = self['email']
        password = self['password']
        member = Member.get_by_email(email)
        if 'member' in self.session and not email is self.session['member']:
            self.response.out.write('another user already logged in')
            return
        if not email or not member:
            self.response.out.write('user not in db')
            return
        if not password == member.password:
            self.response.out.write('wrong password')
            return
        self.session['member'] = email

    def get(self):
        path = 'login.html'
        self.write(self.get_rendered_html(path, {}), 200)

class MemberProfilePage(BaseHandler, WebRequestHandler):
    @login_required
    def get(self):
        path = 'member_profile.html'
        email = self.session['member']
        member = Member.get_by_email(email)
        form_url = blobstore.create_upload_url('/api/members/save_member')
        template_values = {'member': member, 'form_url': form_url}
        self.write(self.get_rendered_html(path, template_values), 200)


class TempHandler(BaseHandler):
    @login_required
    def get(self):
        self.response.out.write(self.session['member'])


app = RestApplication([("/members/login", LoginHandler),
                       ('/members/profile', MemberProfilePage),
                       ("/members/temp", TempHandler)])
