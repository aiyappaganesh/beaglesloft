from model.ui_models.track import Track
from model.ui_models.track import Program

mobile_track = 'Mobile Development'
web_track = 'Full Stack Developer'
designer = 'Designer'
product_manager = 'Product Manager'

def get_programs(track):
    programs = {mobile_track:[Program('iOS Programming 101', 'Aug 1 2015', 20, mobile_track, 'Build, distribute and measure the performance of your first iOS app!', 'ios')],
                web_track:[Program('Web Development 101', 'Aug 1 2015', 20, web_track, 'Go beyond plain HTML and CSS and be cloud ready', 'full_stack')],
                designer:[Program('Designing 101', 'Aug 1 2015', 20, designer, '', 'designer')],
                product_manager:[Program('Product Management 101', 'Aug 1 2015', 20, product_manager, '', 'product')]}
    return programs[track]

tracks = [Track(mobile_track, '/assets/img/tracks/mobile_dev', get_programs(mobile_track)),
          Track(web_track, '/assets/img/tracks/full_stack', get_programs(web_track)),
          Track(designer, '/assets/img/tracks/designer', get_programs(designer)),
          Track(product_manager, '/assets/img/tracks/product_manager', get_programs(product_manager))]

class Tracks():
    @classmethod
    def get_tracks(cls):
        return tracks

    @classmethod
    def get_listing(cls, pg_id):
        for track in tracks:
            for program in track.programs:
                if program.id == pg_id:
                    return program
        return None