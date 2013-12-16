import webapp2
import webapp2_extras
from webapp2_extras import sessions

webapp2_extras.sessions.default_config['secret_key'] = 'asdasd'         #change this to something random and unguessable
webapp2_extras.sessions.default_config['cookie_name'] = 'beaglesloft'

class BaseHandler(webapp2.RequestHandler):
    def dispatch(self):
        self.session_store = sessions.get_store(request=self.request)
        try:
            webapp2.RequestHandler.dispatch(self)
        finally:
            self.session_store.save_sessions(self.response)

    @webapp2.cached_property
    def session(self):
        return self.session_store.get_session()

