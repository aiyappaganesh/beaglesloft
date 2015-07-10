from handlers.web import WebRequestHandler
from handlers.rest.rest_application import RestApplication
from model.ui_models.centered_contents import CenteredContents, CenteredContent
from model.ui_models.factories.tracks import Tracks

import logging

def get_page_title_centered_contents():
    contents_arr = [("TRACKS AT BEAGLES LOFT",["page_heading", "tracks-page-title"])]
    contents = [CenteredContent(s[0], s[1]) for s in contents_arr]
    return CenteredContents(None, 0, contents, False)


class TracksPage(WebRequestHandler):
    def get(self):
        template_values = {}
        template_values['page_title_centered'] = get_page_title_centered_contents()
        template_values['tracks'] = Tracks.get_tracks()
        self.render_template(template_name='tracks.html', template_values=template_values)

app = RestApplication([('/tracks', TracksPage)])
