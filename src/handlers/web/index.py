import webapp2
from auth import access_code_required, login_required
from handlers.web import WebRequestHandler
import re
from model import Member, Newsletter
from google.appengine.api import mail
from google.appengine.api.blobstore import blobstore
import json
import logging

class IndexPage(WebRequestHandler):
    def get(self):
        path = 'landing.html'
        template_values = {'is_member': True if 'member' in self.session else False}
        if 'member' in self.session:
            template_values['member'] = Member.get_member_json(self.session['member'])
        self.render_template(template_name=None, template_values=template_values)

class CalendarPage(WebRequestHandler):
    def get(self):
        path = 'calendar.html'
        ua = self.request.headers['User-Agent']
        b = reg_b.search(ua)
        v = reg_v.search(ua[0:4])
        template_values = {'ua' : 'non-mobile'}
        if b or v:
            template_values['ua'] = 'mobile'
        self.write(self.get_rendered_html(path, template_values), 200)

class MemberRegistrationPage(WebRequestHandler):
    @access_code_required
    def get(self):
        redirect_url = self['redirect_url'] if self['redirect_url'] else '/community'
        path = 'member_registration.html'
        template_values = {}
        template_values['redirect_url'] = redirect_url
        template_values['is_member'] = True if 'member' in self.session else False
        if 'member' in self.session:
            template_values['member'] = Member.get_member_json(self.session['member'])
        self.write(self.get_rendered_html(path, template_values), 200)

class MemberFBRegistrationPage(WebRequestHandler):
    def get(self):
        path = 'member_fbregistration.html'
        self.write(self.get_rendered_html(path, {}), 200)

class MemberAccessPage(WebRequestHandler):
    def get(self):
        redirect_url = self['redirect_url'] if self['redirect_url'] else '/community'
        template_values = {}
        template_values['redirect_url'] = redirect_url
        template_values['is_member'] = True if 'member' in self.session else False
        if 'member' in self.session:
            template_values['member'] = Member.get_member_json(self.session['member'])
        self.render_template(template_name=None, template_values=template_values)

class AcceptContact(WebRequestHandler):
    def post(self):
        name = self['contact_name']
        from_email = self['contact_email']
        message = self['contact_message']

        to_email = "BeaglesLoft Contact <bangalore@b-eagles.com>"
        subject = "Message from BeaglesLoft Contact Page"
        body = """ Name: %s , Email: %s , Message: %s """ % (name, from_email, message)
        mail.send_mail(from_email, to_email, subject, body)
        self.redirect("/")

class PeoplePage(WebRequestHandler):
    def get(self):
        template_values = {}
        template_values['paged_member_keys'] = Member.get_paged_member_keys()
        template_values['is_member'] = True if 'member' in self.session else False
        if 'member' in self.session:
            template_values['member'] = Member.get_member_json(self.session['member'])
        self.render_template(template_name=None, template_values=template_values)

class ContactPage(WebRequestHandler):
    def get(self):
        path = 'contact.html'
        self.write(self.get_rendered_html(path, {}), 200)

class NewslettersPage(WebRequestHandler):
    def get(self):
        template_values = {}
        newsletters = Newsletter.get_paged_newsletters()
        template_values['newsletters'] = newsletters
        template_values['is_member'] = True if 'member' in self.session else False
        if 'member' in self.session:
            template_values['member'] = Member.get_member_json(self.session['member'])
        self.render_template(template_name=None, template_values=template_values)

class CreateNewsletterPage(WebRequestHandler):
    def get(self):
        path = 'create_newsletter.html'
        template_values = {}
        form_url = blobstore.create_upload_url('/api/common/save_newsletter')
        template_values['form_url'] = form_url
        template_values['is_member'] = True if 'member' in self.session else False
        if 'member' in self.session:
            template_values['member'] = Member.get_member_json(self.session['member'])
        self.write(self.get_rendered_html(path, template_values), 200)

app = webapp2.WSGIApplication(
    [
    ]
)