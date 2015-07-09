from handlers.web import WebRequestHandler
from handlers.rest.rest_application import RestApplication

class TracksPage(WebRequestHandler):
    def get(self):
        template_values = {}
        self.render_template(template_name='tracks.html', template_values=template_values)

app = RestApplication([('/tracks', TracksPage)])
