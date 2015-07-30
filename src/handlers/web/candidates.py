from handlers.rest.rest_application import RestApplication
from auth import login_required
from model import Member
from handlers.web import WebRequestHandler
from model.ui_models.donut import DonutSegment
from random import randint
from model.ui_models.factories.donut_factory import DonutFactory
from model.ui_models.centered_contents import CenteredContents, CenteredContent

def get_centered_contents_for(contents_arr):
    contents = [CenteredContent(s[0], s[1]) for s in contents_arr]
    return CenteredContents(None, 0, contents, False)

def get_page_title_centered_contents():
    contents_arr = [("MY PROFILE",["page_heading", "manager-page-title"])]
    return get_centered_contents_for(contents_arr)

class ManagerTrackHandler(WebRequestHandler):
    @login_required
    def get(self):
        path = 'candidate_profile.html'
        template_values = {}
        email = self.session['member']
        member = Member.get_by_email(email)
        template_values['member'] = member
        template_values['is_member'] = True if 'member' in self.session else False
        template_values['page_title_centered'] = get_page_title_centered_contents()
        template_values['donuts'] = DonutFactory.get_donuts(128, 0.8, [('Engineer1', [DonutSegment(randint(0,50), '#1c758a'), DonutSegment(randint(0,50), '#58c4dd')], '/assets/img/tracks/mobile_dev.png')], 'transparent', '#ddd')
        self.write(self.get_rendered_html(path, template_values), 200)

app = RestApplication([("/candidate/profile", ManagerTrackHandler)])