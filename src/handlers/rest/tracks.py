from datetime import datetime, timedelta
from model.ui_models.factories.tracks import Tracks, get_programs, tracks
from model.program import Program
from model.track import Track
from model.program_module import ProgramModule
from handlers.rest.rest_application import RestApplication
from handlers import RequestHandler

track_imgs = {'mobile_developer': 'mobile_dev', 'full_stack_developer': 'full_stack', 'designer': 'designer', 'product_manager': 'product_manager', 'founder': 'founder'}

def setup_tracks():
        for i, track in enumerate(tracks):
            Track(key_name=track.id, name=track.name, order=i, image=track_imgs[track.id]).put()

def setup_programs():
    for track in tracks:
        track_obj = Track.get_by_key_name(track.id)
        for program in track.programs:
            Program(key_name=program.id, parent=track_obj, image=program.snapshot, slots=program.num_spots , name=program.title, description=program.description, start_date=datetime.strptime(program.start_date, "%b %d %Y")).put()

def setup_modules():
    for track in tracks:
        track_obj = Track.get_by_key_name(track.id)
        for program in track.programs:
            start_date = datetime.now()
            program_obj = Program.get_by_key_name(program.id, parent=track_obj)
            if program.modules:
                for module in program.modules:
                    start_date = start_date + timedelta(days=3)
                    ProgramModule(parent=program_obj, name=module.title, units=module.units, start_date=start_date).put()

class PopulateTracksHandler(RequestHandler):
    def get(self):
        setup_tracks()
        self.redirect("/tracks")

class PopulateProgramsHandler(RequestHandler):
    def get(self):
        setup_programs()
        self.redirect("/tracks")

class PopulateModulesHandler(RequestHandler):
    def get(self):
        setup_modules()
        self.redirect("/tracks")

app = RestApplication([("/api/tracks/populate/tracks",PopulateTracksHandler),
                        ("/api/tracks/populate/programs",PopulateProgramsHandler),
                        ("/api/tracks/populate/modules",PopulateModulesHandler)])
