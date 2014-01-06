import webapp2
import webapp2_extras
from webapp2_extras import sessions
from handlers import RequestHandler
from django.template import loader

webapp2_extras.sessions.default_config['secret_key'] = 'asdasd'         #change this to something random and unguessable
webapp2_extras.sessions.default_config['cookie_name'] = 'beaglesloft'

class WebRequestHandler(RequestHandler):
    def render_template(self, template_name, template_values = None):
        self.write(self.get_rendered_html(template_name, template_values))

    def get_rendered_html(self, template_name, template_values = None):
            return loader.render_to_string(template_name, template_values)

    def dispatch(self):
        self.session_store = sessions.get_store(request=self.request)
        try:
            webapp2.RequestHandler.dispatch(self)
        finally:
            self.session_store.save_sessions(self.response)

    @webapp2.cached_property
    def session(self):
        return self.session_store.get_session()
