from handlers.rest.rest_application import RestApplication
from handlers.sessions import BaseHandler
from auth import login_required
from model import Member
#from handlers import RequestHandler
from handlers.web import WebRequestHandler


class LoginHandler(BaseHandler, WebRequestHandler):
    def post(self):
        email = self['email']
        if not email or not Member.get_by_email(email):
            self.response.out.write('user not in db')
            return
        self.session['member'] = email

    def get(self):
        path = 'login.html'
        self.write(self.get_rendered_html(path, {}), 200)


class TempHandler(BaseHandler):
    @login_required
    def get(self):
        self.response.out.write('temp handler')


app = RestApplication([("/members/login", LoginHandler),
                       ("/members/temp", TempHandler)])
