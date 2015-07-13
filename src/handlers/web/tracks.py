from handlers.web import WebRequestHandler
from handlers.rest.rest_application import RestApplication
from model.ui_models.centered_contents import CenteredContents, CenteredContent
from model.ui_models.factories.tracks import Tracks

import logging

def get_centered_contents_for(contents_arr):
    contents = [CenteredContent(s[0], s[1]) for s in contents_arr]
    return CenteredContents(None, 0, contents, False)

def get_page_title_centered_contents():
    contents_arr = [("PROGRAM TRACKS",["page_heading", "tracks-page-title"])]
    return get_centered_contents_for(contents_arr)

def get_listing_centered_contents(program):
    contents_arr = [(program.title,["page_heading", "tracks-page-title"])]
    return get_centered_contents_for(contents_arr)

class TracksPage(WebRequestHandler):
    def get(self):
        template_values = {}
        template_values['page_title_centered'] = get_page_title_centered_contents()
        template_values['tracks'] = Tracks.get_tracks()
        self.render_template(template_name='tracks.html', template_values=template_values)

class ListingPage(WebRequestHandler):
    def get(self):
    	program = Tracks.get_listing(self['id'])
        template_values = {'program':program,
                           'listing_heading':get_listing_centered_contents(program)}
    	self.render_template(template_name='listing.html', template_values=template_values)

app = RestApplication([('/tracks', TracksPage),
					   ('/tracks/program_listing', ListingPage)])
