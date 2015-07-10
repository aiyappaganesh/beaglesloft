from handlers.web import WebRequestHandler
from handlers.rest.rest_application import RestApplication
from model.ui_models.centered_contents import CenteredContents, CenteredContent
from model.ui_models.factories.tracks import Tracks

import logging

TRACKS = [  {'id': 'web_dev', 'title': 'Web development', 'subtracks': [
                {'title': 'SASS Concepts', 'subtracks': [
                        {'title': 'Installation and setup'}
                        ]
                }, 
                {'title': 'Current Front End limitations', 'subtracks':[
                        {'title': 'Limitations of CSS and the need for pre-compilation'},
                        {'title': 'Limitation of HTML and the need for pre-compilation'}
                        ]
                }
            ]
            }, 
            {'id': 'ios', 'title': 'iOS', 'subtracks': [
                {'title': 'The language', 'subtracks':[
                        {'title': 'Objective C (or swift?) fundamentals'}, 
                        {'title': 'Objective C (or swift?) constructs and control flow'}
                        ]
                }
            ]
            }
        ]

def get_page_title_centered_contents():
    contents_arr = [("TRACKS AT BEAGLES LOFT",["page_heading", "tracks-page-title"])]
    contents = [CenteredContent(s[0], s[1]) for s in contents_arr]
    return CenteredContents(None, 0, contents, False)


class TracksPage(WebRequestHandler):
    def get(self):
        template_values = {}
        template_values['page_title_centered'] = get_page_title_centered_contents()
        template_values['tracks'] = Tracks.get_tracks(TRACKS)
        self.render_template(template_name='tracks.html', template_values=template_values)

app = RestApplication([('/tracks', TracksPage)])
