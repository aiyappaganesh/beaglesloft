import webapp2
from auth import access_code_required, login_required
from handlers.web import WebRequestHandler
import re
from model import Member, Newsletter
from google.appengine.api import mail
from google.appengine.api.blobstore import blobstore
import json
import logging
from util import mailjet
from model.ui_models.factories.services import Services
from model.ui_models.centered_contents import CenteredContents, CenteredContent
from model.ui_models.carousel import Carousel
from model.ui_models.image_carousel_slide import Image_Carousel_Slide

def get_loft_images():
    return ['/assets/img/landing/service_imgs/easychair.jpg','/assets/img/landing/service_imgs/terrace.jpg','/assets/img/landing/service_imgs/sunlight.jpg']

def get_lofts_carousel():
    id = "services-lofts"
    classes = "service-carousel"
    slides = [Image_Carousel_Slide(img) for img in get_loft_images()]
    slide_classes= "landing-carousel-item"
    indicator_classes= "landing-carousel-indicators"
    lofts_carousel = Carousel(id, classes, slides, slide_classes, indicator_classes)
    return lofts_carousel

def get_program_images():
    return ['/assets/img/landing/service_imgs/tb1.jpg','/assets/img/landing/service_imgs/tb2.jpg']

def get_programs_carousel():
    id = "services-programs"
    classes = "service-carousel"
    slides = [Image_Carousel_Slide(img) for img in get_program_images()]
    slide_classes= "landing-carousel-item"
    indicator_classes= "landing-carousel-indicators"
    programs_carousel = Carousel(id, classes, slides, slide_classes, indicator_classes)
    return programs_carousel

def get_startup_images():
    return ['/assets/img/landing/service_imgs/st1.jpg','/assets/img/landing/service_imgs/st2.jpg', '/assets/img/landing/service_imgs/st3.jpg']

def get_startups_carousel():
    id = "services-startups"
    classes = "service-carousel"
    slides = [Image_Carousel_Slide(img) for img in get_startup_images()]
    slide_classes= "landing-carousel-item"
    indicator_classes= "landing-carousel-indicators"
    startups_carousel = Carousel(id, classes, slides, slide_classes, indicator_classes)
    return startups_carousel

def get_community_images():
    return ['/assets/img/landing/service_imgs/cm1.jpg','/assets/img/landing/service_imgs/cm2.jpg']

def get_community_carousel():
    id = "services-community"
    classes = "service-carousel"
    slides = [Image_Carousel_Slide(img) for img in get_community_images()]
    slide_classes= "landing-carousel-item"
    indicator_classes= "landing-carousel-indicators"
    community_carousel = Carousel(id, classes, slides, slide_classes, indicator_classes)
    return community_carousel

def get_event_images():
    return ['/assets/img/landing/service_imgs/ev2.jpg','/assets/img/landing/service_imgs/ev3.jpg', '/assets/img/landing/service_imgs/ev1.jpg']

def get_events_carousel():
    id = "services-events"
    classes = "service-carousel"
    slides = [Image_Carousel_Slide(img) for img in get_event_images()]
    slide_classes= "landing-carousel-item"
    indicator_classes= "landing-carousel-indicators"
    events_carousel = Carousel(id, classes, slides, slide_classes, indicator_classes)
    return events_carousel

def get_services_list():
    services = [
        ('/assets/img/landing/lofts.png','/assets/img/landing/lofts_dark.png','LOFTS', get_lofts_carousel()),
        ('/assets/img/landing/programs.png','/assets/img/landing/programs_dark.png','PROGRAMS', get_programs_carousel()),
        ('/assets/img/landing/startups.png','/assets/img/landing/startups_dark.png','STARTUPS', get_startups_carousel()),
        ('/assets/img/landing/community.png','/assets/img/landing/community_dark.png','COMMUNITY', get_community_carousel()),
        ('/assets/img/landing/events.png','/assets/img/landing/events_dark.png','EVENTS', get_events_carousel())
    ]
    return services

def get_value_to_services_centered_contents():
    centered_contents = []
    contents_arr = [("We help IT Services companies significantly increase the revenue per employee",["header-2","black-font"])]
    contents = [CenteredContent(s[0], s[1]) for s in contents_arr]
    centered_contents.append(CenteredContents(360, 0, contents))
    contents_arr = [("We reduce your attrition by up to 30%",["header-2","black-font"])]
    contents = [CenteredContent(s[0], s[1]) for s in contents_arr]
    centered_contents.append(CenteredContents(256, 0, contents))
    return centered_contents

def get_why_beaglesloft_centered_contents():
    centered_contents = []
    contents_arr = [("WHY BEAGLES LOFT?",["header-2","white-font"])]
    contents = [CenteredContent(s[0], s[1]) for s in contents_arr]
    centered_contents.append(CenteredContents(300, 0, contents))
    contents_arr = [("The name is inspired by an old basketball playground in Bangalore. In this playground, we built "
                     "friendships that have lasted the length of our current lives, we discussed how we'd disrupt the "
                     "status quo and we tinkered with technology and music. We often underestimate the value of these "
                     "playgrounds in our lives, but these little playgrounds offer the three key tools that are "
                     "sufficient to work on the really big ideas that can push life forward - community, disruptive "
                     "ideas and a framework for tinkering.",["why-beaglesloft-copy","white-font"])]
    contents = [CenteredContent(s[0], s[1]) for s in contents_arr]
    centered_contents.append(CenteredContents(308, 0, contents))
    return centered_contents


class IndexPage(WebRequestHandler):
    def get(self):
        path = 'landing.html'
        template_values = {'is_member': True if 'member' in self.session else False}
        if 'member' in self.session:
            template_values['member'] = Member.get_member_json(self.session['member'])
        template_values['services'] = Services.get_services(get_services_list())
        template_values['value_to_services_centered'] = get_value_to_services_centered_contents()
        template_values['why_beaglesloft_centered'] = get_why_beaglesloft_centered_contents()
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

class ConfirmSubscribeNewsletterPage(WebRequestHandler):
    def get(self):
        path = 'confirm_newsletter_subscription.html'
        email = self['email']
        fname = self['firstname']
        lname = self['lastname']
        template_values = {}
        template_values['is_member'] = True if 'member' in self.session else False
        if 'member' in self.session:
            template_values['member'] = Member.get_member_json(self.session['member'])
        if not email:
            template_values['subscription_result'] = 'Error: Email not available'
        else:
            template_values['subscription_result'] = mailjet.subscribe(email,fname,lname)
        self.write(self.get_rendered_html(path, template_values), 200)

class SubscribeNewsletterPage(WebRequestHandler):
    def get(self):
        template_values = {}
        template_values['is_member'] = True if 'member' in self.session else False
        if 'member' in self.session:
            template_values['member'] = Member.get_member_json(self.session['member'])
        self.render_template(template_name=None, template_values=template_values)

app = webapp2.WSGIApplication(
    [
    ]
)