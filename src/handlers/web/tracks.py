from handlers.web import WebRequestHandler
from model import Member
from model.enroll_track import EnrollTrack
from handlers.rest.rest_application import RestApplication
from model.ui_models.centered_contents import CenteredContents, CenteredContent
from model.ui_models.factories.tracks import Tracks
from util.util import MEMBER_ROLE, MANAGER
from model.ui_models.factories.donut_factory import DonutFactory
from model.ui_models.donut import DonutSegment
from random import randint

import logging

def get_centered_contents_for(contents_arr):
    contents = [CenteredContent(s[0], s[1]) for s in contents_arr]
    return CenteredContents(None, 0, contents, False)

def get_page_title_centered_contents():
    contents_arr = [("LEARNING TRACKS",["page_heading", "tracks-page-title"])]
    return get_centered_contents_for(contents_arr)

def get_listing_centered_contents(program):
    contents_arr = [(program.title,["page_heading", "tracks-page-title"])]
    return get_centered_contents_for(contents_arr)

class TracksPage(WebRequestHandler):
    def get(self):
        template_values = {}
        template_values['page_title_centered'] = get_page_title_centered_contents()
        template_values['tracks'] = Tracks.get_tracks()
        template_values['is_member'] = True if 'member' in self.session else False
        if 'member' in self.session:
            email = self.session['member']
            member = Member.get_by_email(email)
            template_values['member'] = member
            template_values['enrolled_tracks'] = {}
            for track in Tracks.get_tracks():
                template_values['enrolled_tracks'][track.id] =EnrollTrack.is_enrolled(email, track.id)
            if member.role == MEMBER_ROLE[MANAGER]:
                template_values['is_manager'] = True
                template_values['donuts'] = \
                    DonutFactory.get_donuts\
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
        self.render_template(template_name='tracks.html', template_values=template_values)

class ProgramListingPage(WebRequestHandler):
    def get(self):
        program = Tracks.get_listing(self['id'])
        template_values = {'program':program,
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
