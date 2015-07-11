from model.ui_models.track import Track
from model.ui_models.track import Program

mobile_track = 'Mobile Development'
web_track = 'Web Development'

def get_programs(track):
    programs = {mobile_track:[Program('iOS Programming 101', 'Aug 1 2015', 20, mobile_track)],
                web_track:[Program('Web Development 101', 'Aug 1 2015', 20, web_track)]}
    return programs[track]

tracks = {mobile_track:Track(mobile_track, '/assets/img/tracks/mobile_dev.png', get_programs(mobile_track)),
             web_track:Track(web_track, '/assets/img/tracks/mobile_dev.png', get_programs(web_track))}

class Tracks():
    @classmethod
    def get_tracks(cls):
        return tracks

    @classmethod
    def get_listing(cls, pg_id):
        for name, track in tracks.iteritems():
            for program in track.programs:
                if program.id == pg_id:
                    return program
        return None