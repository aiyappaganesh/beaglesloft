from model.ui_models.track import Track, Program, Module

mobile_track = 'Mobile Development'
web_track = 'Full Stack Developer'
designer = 'Designer'
product_manager = 'Product Manager'

def get_modules_for(track):
    modules = {mobile_track: [Module('Current Front End Limitations', ['Limitations of CSS and the need for pre-compilation', 'Limitation of HTML and the need for pre-compilation']),
                              Module('SASS Concepts', ['Installation and setup', 'Import directive and modularising CSS code', 'Include directive and mixins', 'Extend directive', 'At-root directive']),
                              Module('HAML Concepts', ['DRY HTML', 'Installation and setup', 'HAML syntax', 'Eliminating white space', 'Eliminating deep nesting']),
                              Module('Back End Development Flavours', ['DEVOPS intensive environments -- AWS', 'DEVOPS free environments -- GAE']),
                              Module('Basics of AWS', ['Procuring instances', 'Setting up a web server', 'Setting up a DB server', 'Tying it together and making a backend work', 'Scaling a backend on AWS']),
                              Module('Basics of GAE', ['Setting up a backend on GAE', 'Scaling a backend on GAE', 'Implementing map reduce on GAE'])],
                web_track: [Module('The Language', ['Objective C fundamentals', 'Objective C constructs and control flow']),
                            Module('The Run Time', ['Procuring a developer certificate', "Setting up your team on Apple's member center", 'Preparing your machine with the developer certificate']),
                            Module('Installation', ['Installing a simple app on your phone via Xcode']),
                            Module('Deep Dive', ['View controller modelling for iOS apps', 'Storyboarding your app', 'Gestures and interactions'])]}
    return modules[track]

def get_programs(track):
    programs = {
        mobile_track:
            [
                Program('iOS Programming 101', 'Aug 1 2015', 20, mobile_track, 'Learn the basics of programming in Objective C and setting up the fundamentals of iOS Dev Environment', 'ios', get_modules_for(mobile_track)),
                Program('Building an iOS App', 'Aug 1 2015', 20, mobile_track, 'Build an iOS App from scratch with a deep dive into iOS Programming', 'ios', get_modules_for(mobile_track)),
                Program('High quality iOS code', 'Aug 1 2015', 20, mobile_track, 'Learn what differentiates a high quality app from a mediocre one and how to code for excellence', 'ios', get_modules_for(mobile_track)),
                Program('App Analytics and Audience Engagement', 'Aug 1 2015', 20, mobile_track, 'Deep dive into analytics, data monitoring, audience segmentation and engagement', 'ios', get_modules_for(mobile_track)),
                Program('App Store Optimization', 'Aug 1 2015', 20, mobile_track, 'How to launch your app effectively and optimize for success in the app store', 'ios', get_modules_for(mobile_track)),
                Program('User acquisition', 'Aug 1 2015', 20, mobile_track, 'Learn how to go from zero to the first thousand users to prove product market fit', 'ios', get_modules_for(mobile_track)),
                Program('Android Programming 101', 'Aug 1 2015', 20, mobile_track, 'Build an iOS App from scratch with a deep dive into iOS Programming', 'ios', get_modules_for(mobile_track)),
                Program('Building an Android App', 'Aug 1 2015', 20, mobile_track, 'Build an iOS App from scratch with a deep dive into iOS Programming', 'ios', get_modules_for(mobile_track)),
                Program('High quality Android code', 'Aug 1 2015', 20, mobile_track, 'Build an iOS App from scratch with a deep dive into iOS Programming', 'ios', get_modules_for(mobile_track)),
                Program('Android App Analytics and Audience Engagement', 'Aug 1 2015', 20, mobile_track, 'Build an iOS App from scratch with a deep dive into iOS Programming', 'ios', get_modules_for(mobile_track)),
                Program('Google Play Store Optimization', 'Aug 1 2015', 20, mobile_track, 'Build an iOS App from scratch with a deep dive into iOS Programming', 'ios', get_modules_for(mobile_track)),
                Program('Android user acquisition', 'Aug 1 2015', 20, mobile_track, 'Build an iOS App from scratch with a deep dive into iOS Programming', 'ios', get_modules_for(mobile_track))
            ],
        web_track:[Program('Web Development Limitations', 'Aug 1 2015', 20, web_track, 'Learn about writing D.R.Y web code and the limitations of HTML and CSS in achieving that', 'full_stack', None),
                   Program('SASS', 'Aug 1 2015', 20, web_track, 'Why is CSS pre-compilation necessary and how does it help make CSS modular and D.R.Y', 'full_stack', None),
                   Program('HAML', 'Aug 1 2015', 20, web_track, 'Eliminate deep nested HTML and learn to cut down the HTML code you write by half through pre-compilation', None),
                   Program('Backend infrastructure for web apps', 'Aug 1 2015', 20, web_track, 'Explore 2 different types of backend infrastructure. One DEVOPS intensive and one without DEVOPS.', None)],
        designer:[Program('Designing 101', 'Aug 1 2015', 20, designer, '', 'designer', None)],
        product_manager:[Program('Product Management 101', 'Aug 1 2015', 20, product_manager, '', 'product', None)]}
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