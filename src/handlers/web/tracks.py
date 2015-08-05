from handlers.web import WebRequestHandler
from model import Member
from model.enroll_program import EnrollProgram
from handlers.rest.rest_application import RestApplication
from model.ui_models.centered_contents import CenteredContents, CenteredContent
from model.ui_models.factories.tracks import Tracks
from util.util import MEMBER_ROLE, MANAGER
from model.ui_models.factories.donut_factory import DonutFactory
from model.ui_models.donut import DonutSegment
from random import randint
from model.managed_user import ManagedUser
from model.program import Program
from model.track import Track
from model.program_module import ProgramModule

import logging

def get_centered_contents_for(contents_arr):
    contents = [CenteredContent(s[0], s[1]) for s in contents_arr]
    return CenteredContents(None, 0, contents, False)

def get_page_title_centered_contents():
    contents_arr = [("LEARNING TRACKS",["page_heading", "tracks-page-title"])]
    return get_centered_contents_for(contents_arr)

def get_listing_centered_contents(program):
    contents_arr = [(program.name,["page_heading", "tracks-page-title"])]
    return get_centered_contents_for(contents_arr)

class TracksPage(WebRequestHandler):
    def _make_json(self, track):
        response = {}
        response['icon'] = track.icon
        response['highlight_icon'] = track.highlight_icon
        response['name'] = track.name
        response['id'] = track.id
        response['programs'] = Program.all().ancestor(Track.get_by_key_name(track.id))
        return response

    def get(self):
        template_values = {}
        template_values['page_title_centered'] = get_page_title_centered_contents()
        template_values['tracks'] = [self._make_json(track) for track in Track.all()]
        template_values['is_member'] = True if 'member' in self.session else False
        if 'member' in self.session:
            email = self.session['member']
            member = Member.get_by_email(email)
            template_values['member'] = member
            template_values['enrolled_tracks'] = {}
            for track in Tracks.get_tracks():
                template_values['enrolled_tracks'][track.id] = EnrollProgram.is_enrolled_track(email, track.id)
            if member.role == MEMBER_ROLE[MANAGER]:
                template_values['is_manager'] = True
            else:
                template_values['donuts'] = DonutFactory.get_donuts(100, 0.875, [('Engineer1', [DonutSegment(randint(0,50), '#1c758a'), DonutSegment(randint(0,50), '#58c4dd')], '/assets/img/tracks/mobile_dev.png')], 'transparent', '#ddd')
        self.render_template(template_name='tracks.html', template_values=template_values)

class ProgramListingPage(WebRequestHandler):
    def get(self):
        track = Track.get_by_key_name(self['track_id'])
        program = Program.get_by_key_name(self['program_id'], parent=track)
        modules = ProgramModule.all().ancestor(program)
        template_values = {'modules': modules,
                           'listing_heading':get_listing_centered_contents(program)}
        template_values['is_member'] = True if 'member' in self.session else False
        if 'member' in self.session:
            email = self.session['member']
            member = Member.get_by_email(email)
            template_values['member'] = member
            if member.role == MEMBER_ROLE[MANAGER]:
                template_values['donuts'] = DonutFactory.get_donuts\
                        (100, 0.875,
                         [
                             ('James', [DonutSegment(randint(0,50), '#1c758a'), DonutSegment(randint(0,50), '#58c4dd')], '/assets/img/tracks/mobile_dev.png'),
                             ('Abdul', [DonutSegment(randint(0,50), '#1c758a'), DonutSegment(randint(0,50), '#58c4dd')], '/assets/img/tracks/mobile_dev.png'),
                             ('Raj', [DonutSegment(randint(0,50), '#1c758a'), DonutSegment(randint(0,50), '#58c4dd')], '/assets/img/tracks/mobile_dev.png'),
                             ('David', [DonutSegment(randint(0,50), '#1c758a'), DonutSegment(randint(0,50), '#58c4dd')], '/assets/img/tracks/mobile_dev.png'),
                             ('Chang', [DonutSegment(randint(0,50), '#1c758a'), DonutSegment(randint(0,50), '#58c4dd')], '/assets/img/tracks/mobile_dev.png')
                         ],
                         'transparent', '#ddd'
                        )
            else:
                template_values['donuts'] = DonutFactory.get_donuts(100, 0.875, [('Engineer1', [DonutSegment(randint(0,50), '#1c758a'), DonutSegment(randint(0,50), '#58c4dd')], '/assets/img/tracks/mobile_dev.png')], 'transparent', '#ddd')
        self.render_template(template_name='program_listing.html', template_values=template_values)

app = RestApplication([('/tracks', TracksPage),
                       ('/tracks/program_listing', ProgramListingPage)])
