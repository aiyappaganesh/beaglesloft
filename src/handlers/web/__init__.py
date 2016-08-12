import webapp2
from .web_request_handler import WebRequestHandler
from .index import IndexPage, CalendarPage, MemberRegistrationPage, MemberFBRegistrationPage, MemberAccessPage, AcceptContact, PeoplePage, ContactPage, NewslettersPage, CreateNewsletterPage, SubscribeNewsletterPage, ConfirmSubscribeNewsletterPage, MembershipPage, CreateAssociationPage
from .events import CreateEventPage, EditEventPage, SearchEventPage, EventsPage
from django import template

template.add_to_builtins('handlers.web.filters')

app = webapp2.WSGIApplication([
    ('/calendar', CalendarPage),
    ('/member_registration', MemberRegistrationPage),
    ('/member_fbregistration', MemberFBRegistrationPage),
    ('/member_access', MemberAccessPage),
    ('/accept_contact', AcceptContact),
    ('/community', PeoplePage),
    ('/contact', ContactPage),
    ('/events/create_event', CreateEventPage),
    ('/events/edit_event', EditEventPage),
    ('/events/search_event', SearchEventPage),
    ('/events', EventsPage),
    ('/membership', MembershipPage),
    ('/newsletters', NewslettersPage),
    ('/create_newsletter', CreateNewsletterPage),
    ('/subscribe_newsletter', SubscribeNewsletterPage),
    ('/confirm_subscribe_newsletter', ConfirmSubscribeNewsletterPage),
    ('/associate', CreateAssociationPage),
    ('/', IndexPage)
])