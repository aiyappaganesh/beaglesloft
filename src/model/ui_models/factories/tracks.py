from model.ui_models.track import Track, Program, Module

mobile_track = 'Mobile Developer'
web_track = 'Full Stack Developer'
designer = 'Designer'
product_manager = 'Product Manager'
founder = 'Founder'

math_for_cs = 'Mathematics for Computer Science'
beyond_html = 'Going beyond HTML and CSS'

def get_modules_for(track):
    modules = { math_for_cs: [  Module('Unit 1: Counting numbers', ['Fundamental counting principle', 'Permutations and combinations', 'Sums and recurrences', 'Manipulation of sums', 'Infinite sums', 'Asymptotes']),
                                Module('Unit 2: Structures', ['Graph definitions', 'Graph coloring', 'Directed graphs', 'Relations and partial orders']),
                                Module('Unit 3: Probability', ['Events and probability spaces', 'Conditional probability', 'Random variables and distribution', 'Deviations'])],
                beyond_html: [  Module('Unit 1: Current Front End limitations', ['Writing DRY code', 'Limitations of CSS and the need for pre-compilation', 'Limitation of HTML and the need for pre-compilation']),
                                Module('Unit 2: SASS Concepts', ['Installation and setup', '@import directive and modularising CSS code', '@include directive and mixins', '@extend directive', '@at-root directive']),
                                Module('Unit 3: HAML concepts', ['Installation and setup', 'HAML syntax', 'Eliminating white space', 'Eliminating deep nesting'])  ],
                web_track: [  Module('Unit 1: Current Front End Limitations', ['Limitations of CSS and the need for pre-compilation', 'Limitation of HTML and the need for pre-compilation']),
                              Module('Unit 2: SASS Concepts', ['Installation and setup', 'Import directive and modularising CSS code', 'Include directive and mixins', 'Extend directive', 'At-root directive']),
                              Module('Unit 3: HAML Concepts', ['DRY HTML', 'Installation and setup', 'HAML syntax', 'Eliminating white space', 'Eliminating deep nesting']),
                              Module('Unit 4: Back End Development Flavours', ['DEVOPS intensive environments -- AWS', 'DEVOPS free environments -- GAE']),
                              Module('Unit 5: Basics of AWS', ['Procuring instances', 'Setting up a web server', 'Setting up a DB server', 'Tying it together and making a backend work', 'Scaling a backend on AWS']),
                              Module('Unit 6: Basics of GAE', ['Setting up a backend on GAE', 'Scaling a backend on GAE', 'Implementing map reduce on GAE'])],
                mobile_track: [ Module('Unit 1: The Language', ['Objective C fundamentals', 'Objective C constructs and control flow']),
                                Module('Unit 2: The Run Time', ['Procuring a developer certificate', "Setting up your team on Apple's member center", 'Preparing your machine with the developer certificate']),
                                Module('Unit 3: Installation', ['Installing a simple app on your phone via Xcode']),
                                Module('Unit 4: Deep Dive', ['View controller modelling for iOS apps', 'Storyboarding your app', 'Gestures and interactions'])]}
    return modules[track]

def get_programs(track):
    programs = {
        mobile_track:
            [
                Program('iOS Programming 101', 'Aug 1 2015', 15, mobile_track, 'Learn the basics of programming in Objective C and setting up the fundamentals of iOS Dev Environment.', 'xcode', get_modules_for(mobile_track)),
                Program('Building an iOS App', 'Aug 8 2015', 20, mobile_track, 'Build an iOS App from scratch with a deep dive into iOS Programming.', 'dev_ios', get_modules_for(mobile_track)),
                Program('High quality iOS code', 'Aug 14 2015', 15, mobile_track, 'Learn what differentiates a high quality app from a mediocre one and how to code for excellence.', 'high_quality_ios_code', get_modules_for(mobile_track)),
                Program('App Analytics and Audience Engagement', 'Aug 1 2015', 25, mobile_track, 'Deep dive into analytics, data monitoring, audience segmentation and engagement.', 'analytics', get_modules_for(mobile_track)),
                Program('App Store Optimization', 'Aug 21 2015', 15, mobile_track, 'How to launch your app effectively and optimize for success in the app store.', 'appstore_opt', get_modules_for(mobile_track)),
                Program('User acquisition', 'Aug 28 2015', 20, mobile_track, 'Learn how to go from zero to the first thousand users to prove product market fit.', 'useracquisition', get_modules_for(mobile_track)),
                Program('Android Programming 101', 'Sept 5 2015', 20, mobile_track, 'Build an iOS App from scratch with a deep dive into iOS Programming.', 'android_programming', get_modules_for(mobile_track)),
                Program('Building an Android App', 'Sept 12 2015', 20, mobile_track, 'Build an iOS App from scratch with a deep dive into iOS Programming.', 'building_an_android_app', get_modules_for(mobile_track)),
                Program('High quality Android code', 'Sept 19 2015', 25, mobile_track, 'Build an iOS App from scratch with a deep dive into iOS Programming.', 'android_coding', get_modules_for(mobile_track)),
                Program('Android App Analytics and Audience Engagement', 'Sept 26 2015', 20, mobile_track, 'Build an iOS App from scratch with a deep dive into iOS Programming.', 'analytics', get_modules_for(mobile_track)),
                Program('Google Play Store Optimization', 'Oct 1 2015', 25, mobile_track, 'Build an iOS App from scratch with a deep dive into iOS Programming.', 'google_play', get_modules_for(mobile_track)),
                Program('Android user acquisition', 'Oct 8 2015', 10, mobile_track, 'Build an iOS App from scratch with a deep dive into iOS Programming.', 'useracquisition', get_modules_for(mobile_track))
            ],
        web_track:[Program('Building a Web App 101', 'Aug 2 2015', 20, web_track, 'A beginner course to understand all the skills required to be a good web developer.', 'full_stack', get_modules_for(web_track)),
                   Program('Going beyond HTML and CSS', 'Aug 9 2015', 20, web_track, 'Learn how to write D.R.Y code and the frameworks and libraries to achieve that.', 'less', get_modules_for(beyond_html)),
                   Program('Mathematics for Computer Science', 'Aug 23 2015', 30, web_track, 'The Calculus, Statistics, Combinatorics, Graph Theory, Probablity and number theory every data scientist should know.', 'cont_math', get_modules_for(math_for_cs)),
                   Program('Algorithms and Datastructures revisited', 'Aug 30 2015', 20, web_track, 'Computer science fundamentals which separates a good programmer from the best.', 'algo', get_modules_for(web_track)),
                   Program('Distributed computing', 'Sept 7 2015', 25, web_track, 'Basic concepts of distributed computing and how to execute it on the cloud.', 'dist', get_modules_for(web_track)),
                   Program('Non-relational Databases', 'Sept 14 2015', 30, web_track, 'The new Non-relational mathematics and how commercial databases implement them.', 'no_sql', get_modules_for(web_track)),
                   Program('NLP 101', 'Sept 21 2015', 25, web_track, 'Tools and frameworks for processing and mining data from natural language text.', 'nlp', get_modules_for(web_track)),
                   Program('Big Data 101', 'Sept 28 2015', 20, web_track, 'Learn how to store massive amounts of data in distributed databases and process them using MapReduce.', 'big_data', get_modules_for(web_track))],
        designer:[
                Program('Design Thinking', 'Aug 3 2015', 15, designer, 'Learn the methods and approaches to use design as a "way of thinking" for creative action.', 'design_thinking', None),
                Program('iOS App Design', 'Aug 10 2015', 20, designer, 'From using 3D depth to layered design. Learn the design concepts required to make world class iOS Apps.', 'ios_design', None),
                Program('Android App Design', 'Aug 17 2015', 10, designer, """An in-depth look at Android's implementation of "material design" and how you can use it make elegant Android Apps.""", 'android_design', None),
                Program('Web Design', 'Aug 24 2015', 15, designer, "Parallax, Single Scroll pages, Sticky menus and other new age design paradigms which is shaping today's web pages.", 'web_design', None),
                Program('Responsive Design', 'Sept 3 2015', 20, designer, 'Learn how to make your website render seamlessly across a multitude of devices and resolutions.', 'responsive_design', None),
                Program('Branding Concepts', 'Sept 10 2015', 20, designer, 'How to turn an idea into a product and brand that people love.', 'branding', None)
            ],
        product_manager:[
            Program('The new age Product Manager', 'Aug 4 2015', 10, product_manager, 'Learn to handle challenges in software development with ever changing requirements and faster iterations.', 'product', None),
            Program('Tools for Product Management', 'Aug 11 2015', 15, product_manager, 'Master new age product management tools like Trello, Typeform and Quip to make you more productive and agile.', 'tools', None),
            Program('Design Thinking for Management', 'Aug 18 2015', 10, product_manager, 'Integrate pillars of design thinking- desirability, feasibility and viability into product management.', 'design_thinking', None),
            Program('Agile based Product Management', 'Aug 25 2015', 20, product_manager, 'Embrace changes and make it work to your favor through agile based product management.', 'agile', None),
            Program('Client Management', 'Sept 1 2015', 20, product_manager, 'Learn all the tricks of the trade to develop a long lasting and happy relationship with your clients.', 'client_managament', None),
            Program('Lean Product Management', 'Sept 8 2015', 15, product_manager, 'Learn to work in iterations to build, measure and learn only what is required and save valuable resources.', 'product_management', None)
            ],
        founder: [
            Program('Bootstrapping your startup', 'Aug 5 2015', 10, founder, 'Make the most of your own resources to build a startup without an outside investor', 'bootstrap', None),
            Program('Raising the seed round', 'Aug 12 2015', 15, founder, 'Learn the nuances of acquiring a seed round investment to shape up your idea', 'seed', None),
            Program('Raising the Series A round', 'Aug 19 2015', 10, founder, 'Obtain the skills it takes to get the best term sheet from an investor at the most crucial stage of your startup', 'series-a', None),
            Program('MVP and Product Market Fit', 'Aug 26 2015', 25, founder, 'Decide the right features that goes into your MVP to produce highest return on investment', 'mvp', None),
            Program('Investor Management', 'Sept 2 2015', 20, founder, 'Understand how to choose investors and strategize accepting funds', 'investor', None)
            ]
    }
    return programs[track]

tracks = [Track(mobile_track, '/assets/img/tracks/mobile_dev', get_programs(mobile_track)),
          Track(web_track, '/assets/img/tracks/full_stack', get_programs(web_track)),
          Track(designer, '/assets/img/tracks/designer', get_programs(designer)),
          Track(product_manager, '/assets/img/tracks/product_manager', get_programs(product_manager)),
          Track(founder, '/assets/img/tracks/founder', get_programs(founder))]

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