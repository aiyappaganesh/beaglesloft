from model.ui_models.track import Track


TRACKS = [  {'id': 'web_dev', 'image': '/assets/img/tracks/mobile_dev.png', 'title': 'Web Development', 'subtracks': [
                {'title': 'Current Front End Limitations', 'subtracks':[
                        {'title': 'Limitations of CSS and the need for pre-compilation'},
                        {'title': 'Limitation of HTML and the need for pre-compilation'}
                        ]
                },
                {'title': 'SASS Concepts', 'subtracks': [
                        {'title': 'Installation and setup'},
                        {'title': 'Import directive and modularising CSS code'},
                        {'title': 'Include directive and mixins'},
                        {'title': 'Extend directive'},
                        {'title': 'At-root directive'}
                        ]
                },
                {'title': 'HAML Concepts', 'subtracks': [
                        {'title': 'DRY HTML'},
                        {'title': 'Installation and setup'},
                        {'title': 'HAML syntax'},
                        {'title': 'Eliminating white space'},
                        {'title': 'Eliminating deep nesting'}
                        ]
                },
                {'title': 'Back End Development Flavours', 'subtracks': [
                        {'title': 'DEVOPS intensive environments -- AWS'},
                        {'title': 'DEVOPS free environments -- GAE'}
                        ]
                },
                {'title': 'Basics of AWS', 'subtracks': [
                        {'title': 'Procuring instances'},
                        {'title': 'Setting up a web server'},
                        {'title': 'Setting up a DB server'},
                        {'title': 'Tying it together and making a backend work'},
                        {'title': 'Scaling a backend on AWS'}
                        ]
                },
                {'title': 'Basics of GAE', 'subtracks': [
                        {'title': 'Setting up a backend on GAE'},
                        {'title': 'Scaling a backend on GAE'},
                        {'title': 'Implementing map reduce on GAE'}
                        ]
                }
            ]
            },
            {'id': 'ios', 'image': '/assets/img/tracks/mobile_dev.png', 'title': 'iOS', 'subtracks': [
                {'title': 'The Language', 'subtracks':[
                        {'title': 'Objective C fundamentals'},
                        {'title': 'Objective C constructs and control flow'}
                        ]
                },
                {'title': 'The Run Time', 'subtracks':[
                        {'title': 'Procuring a developer certificate'},
                        {'title': "Setting up your team on Apple's member center"},
                        {'title': 'Preparing your machine with the developer certificate'}
                        ]
                },
                {'title': 'Installation', 'subtracks':[
                        {'title': 'Installing a simple app on your phone via Xcode'}
                        ]
                },
                {'title': 'Deep Dive', 'subtracks':[
                        {'title': 'View controller modelling for iOS apps'},
                        {'title': 'Storyboarding your app'},
                        {'title': 'Gestures and interactions'},
                        {'title': 'Working with some of the often used concepts like UITableViews, UICollectionViews etc...'},
                        {'title': 'Efficient networking for iOS apps'}
                        ]
                },
                {'title': 'Instrumenting your App', 'subtracks':[
                        {'title': 'Measure allocations and catch leaks'},
                        {'title': 'Measure battery and CPU performance'},
                        {'title': 'Measure network performance'}
                        ]
                },
                {'title': 'Distributing and Measuring Engagement', 'subtracks':[
                        {'title': 'Distribute your app via iTunes and TestFlight'},
                        {'title': 'Measure user engagement using AppBoy and Flurry'}
                        ]
                }
            ]
            }
        ]

class Tracks():
    @classmethod
    def get_tracks(cls, tracks=TRACKS):
        track_objs = []
        for track in tracks:
            subtracks = track['subtracks'] if 'subtracks' in track else None
            track_obj = Track(title=track['title'])
            if subtracks:
                subtracks_objs = cls.get_tracks(tracks=track['subtracks'])
                track_obj.subtracks = subtracks_objs
            id = track['id'] if 'id' in track else None
            if id:
                track_obj.id = id
            image = track['image'] if 'image' in track else None
            if image:
                track_obj.image = image
            track_objs.append(track_obj)
        return track_objs
