import webapp2
from .web_request_handler import WebRequestHandler
from .index import IndexPage, CalendarPage, MemberRegistrationPage, MemberFBRegistrationPage, MemberAccessPage, AcceptContact, PeoplePage, ContactPage, NewslettersPage, CreateNewsletterPage
from .events import CreateEventPage, EditEventPage, SearchEventPage, EventsPage

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
    ('/newsletters', NewslettersPage),
    ('/create_newsletter', CreateNewsletterPage),
    ('/', IndexPage)
])