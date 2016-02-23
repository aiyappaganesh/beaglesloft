from model.ui_models.track import Track, Program, Module

mobile_track = 'Mobile Developer'
web_track = 'Full Stack Developer'
designer = 'Designer'
product_manager = 'Product Manager'
founder = 'Founder'

math_for_cs = 'Mathematics for Computer Science'
beyond_html = 'Going beyond HTML and CSS'
algs_and_ds = 'Algorithms and Datastructures revisited'
distributed_computing = 'Distributed Computing'
non_relational_databases = 'Non Relational Databases'
big_data = 'Big Data 101'
nlp = 'NLP'
ios_101 = 'iOS Programming 101'
build_ios_app = 'Building an iOS App'
high_quality_ios = 'High quality iOS code'
app_analytics = 'App Analytics and Audience Engagement'
appstore_optimize = 'App Store Optimization'
user_acquisition = 'User acquisition'
android_101 = 'Android Programming 101'
build_android_app = 'Building an Android App'
high_quality_android = 'High quality Android code'
android_app_analytics = 'Android App Analytics and Audience Engagement'
playstore_optimize = 'Google Play Store Optimization'
android_user_acquisition = 'Android user acquisition'

def get_modules_for(track):
    modules = { math_for_cs: [  Module('Unit 1: Counting numbers', ['Fundamental counting principle', 'Permutations and combinations', 'Sums and recurrences', 'Manipulation of sums', 'Infinite sums', 'Asymptotes']),
                                Module('Unit 2: Structures', ['Graph definitions', 'Graph coloring', 'Directed graphs', 'Relations and partial orders']),
                                Module('Unit 3: Probability', ['Events and probability spaces', 'Conditional probability', 'Random variables and distribution', 'Deviations'])],
                beyond_html: [  Module('Unit 1: Current Front End limitations', ['Writing DRY code', 'Limitations of CSS and the need for pre-compilation', 'Limitation of HTML and the need for pre-compilation']),
                                Module('Unit 2: SASS Concepts', ['Installation and setup', '@import directive and modularising CSS code', '@include directive and mixins', '@extend directive', '@at-root directive']),
                                Module('Unit 3: HAML concepts', ['Installation and setup', 'HAML syntax', 'Eliminating white space', 'Eliminating deep nesting'])  ],
                algs_and_ds: [  Module('Unit 1: Algorithms', ['Algorithm analysis', 'Sorting and searching', 'Combinatorial search and hueristics', 'Dynamic programming', 'P vs. NP']),
                                Module('Unit 2: Data structures', ['Stacks and queues', 'Binary search trees', 'Priority queues', 'Hashing and strings', 'Graph traversals', 'Weighted graphs'])],
                web_track: [  Module('Unit 1: Frontend development', ['HTML basics', 'CSS basics', 'Javascript basics', 'Intro to jQuery', 'Arrays and traversing the DOM']),
                              Module('Unit 2: Back end development', ['DEVOPS intensive environments like AWS', 'DEVOPS free environments like GAE']),
                              Module('Unit 3: Basics of Amazon Web Services', ['Procuring instances', 'Setting up a web server', 'Setting up a DB server', 'Tying it together and making a backend work', 'Scaling a backend on AWS']),
                              Module('Unit 4: Basics of Google AppEngine', ['Setting up a backend on GAE', 'Scaling a backend on GAE', 'Implementing map reduce on GAE'])],
                nlp: [  Module('Unit 1: Processing raw text', ['Text processing with unicode', 'Regular expressions for detecting word patterns', 'Normalizing text', 'Segmentation', 'Regular expressions for tokenizing text']),
                        Module('Unit 2: Categorizing and tagging words', ['Automatic tagging', 'N-Gram tagging', 'Transformation-Based tagging', 'Using a tagger']),
                        Module('Unit 3: Classifying text', ['Naive Bayes classifiers', 'Decision trees', 'Maximum entropy classifiers', 'Supervised classification']),
                        Module('Unit 4: Extracting information from text', ['Developing and evaluating chunkers', 'Recursion in linguistic structure', 'Named entity recognition', 'Relation extraction'])],
                distributed_computing: [  Module('Unit 1: Theory', ['Required properties of a distributed system', 'Putting everything together: CAP theorem', 'Distributed transactions', 'Data replication and consistency', 'Networking infrastructures']),
                                          Module('Unit 2: Practise', ["MapReduce and Google's implementation", "A look at Google's BigTable", "Horizontally scaling webservers"])],
                non_relational_databases: [Module('Unit 1: Why NoSQL?', ['Impedance mismatch', 'Scalability and clusters', 'Schema-less data representation']),
                                          Module('Unit 2: Data models', ["Key-Value and document data models", "Column-Family stores", "Graph data models", "Schemaless databases"]),
                                          Module('Unit 3: Consistency', ["Update consistency", "Read consistency", "Relaxing consistency", "Relaxing durability"]),
                                          Module('Unit 4: Commercial databases', ["Google's BigTable", "MongoDB", "Neo4J"]),
                                          Module('Unit 5: When not to use', ["Key-Value and Document databases", "Column-Family stores", "Graph databases"])],
                big_data: [Module('Unit 1: Storage of Big Data', ['Impedance mismatch', 'Scalability requirements of the new age', "Key-Value datastores - Google's BigTable", 'Document datastores - MongoDB', 'Graph Databases - Neo4J']),
                          Module('Unit 2: Analysis of Big Data - Theory', ["Summarising and exploring data", "Inferences for single samples", "Inferences for two samples", "Simple linear regression and co-relation", 'Multiple linear regression', 'Likelihood, Bayesian and Decision Theory models']),
                          Module('Unit 3: Analysis of Big Data - Practise', ["MapReduce using Google AppEngine", "Intro to Hadoop", "A look at Google's BigTable", "A look at HBase", 'Intro to Lucene', 'Text search using Google AppEngine'])],
                ios_101: [  Module('Unit 1: The Language', ['Objective C fundamentals', 'Objective C constructs and control flow']),
                            Module('Unit 2: The Run Time', ['Procuring a developer certificate', "Setting up your team on Apple's member center", 'Preparing your machine with the developer certificate']),
                            Module('Unit 3: Installation', ['Installing a simple app on your phone via Xcode']),
                            Module('Unit 4: Deep Dive', ['View controller modelling for iOS apps', 'Storyboarding your app', 'Gestures and interactions'])],
                build_ios_app: [  Module('Unit 1: Foundation', ['Classes, Objects', 'Variables, Types and Functions']),
                                  Module('Unit 2: MVC', ['Models, Views, Controllers and Lifecycles', 'Multiple Model-View-Controllers']),
                                  Module('Unit 3: Animation', ['Protocols', 'Blocks', 'Animation', 'Autolayout']),
                                  Module('Unit 4: Data and Views', ['Table View, Scroll View', 'IPad, Documents', 'Core data']),
                                  Module('Unit 5: Segue', ['Embed Segue', 'Modal Segue']),
                                  Module('Unit 6: Networking', ['HTTP and HTTPS Requests', 'Sockets and Socket Streams', 'URL Session Programming']),
                                  Module('Unit 7: Localization', ['Internationalizing', 'Locale Settings', 'Choosing Languages, Locking Views, Exporting & Importing Localizations'])],
                high_quality_ios: [ Module('Unit 1: Project Structure', ['Model-View-Controller', 'Loose Coupling']),
                                    Module('Unit 2: Design Patterns and Architecture', ['Target Action', 'Notification', 'Delegation', 'Optimal Architecture']),
                                    Module('Unit 3: Storing Data', ['Property Lists', 'Archives', 'Custom Files', 'Cloud', 'SQLite', 'CoreData']),
                                    Module('Unit 4: Coding Conventions', ['Key-Value Observing KVO'])],
                app_analytics: [  Module('Unit 1: What to Track and Why', ['KPI', 'Cohort Analysis']),
                                  Module('Unit 2: In-App Usage Analytics', ['Flurry', 'Universal Analytics', 'Apple Analytics', 'Mixpanel', 'Facebook Analytics', 'Amplitude', 'Fabric', 'Countly', 'Appsee', 'Localytics'])],
                appstore_optimize: [  Module('Unit 1: Keyword Optimization (KWO)', ['How to choose App Store Keywords']),
                                      Module('Unit 2: Asset Optimization (AO)', ['Icon Design', 'Screenshots', 'Video Previews']),
                                      Module('Unit 3: Best Practices', ['Choosing Titles', 'Descriptions', 'Localization'])],
                user_acquisition: [ Module('Unit 1: Secret Sauce', ['Survey Findings', 'Mobile First App Development']),
                                    Module('Unit 2: Lifetime Customer Value(LTV)', ['Methodology', 'Advantages and Disadvantages'])],
                android_101: [  Module('Unit 1: The Language', ['Java fundamentals', 'Java constructs and control flow']),
                                Module('Unit 2: The Run Time', ['Install Java, JDK and JRE, Eclipse IDE','Android Studio, Genymotion, Gradle, and debugging tools']),
                                Module('Unit 3: Deep Dive', ['Inputs, Buttons and Reactive (Tap) Interfaces', 'Android Building blocks', 'Variables, Arrays, Loops, ArrayLists, Listview'])],
                build_android_app: [  Module('Unit 1: Installation', ['Install and Setup for Windows Users', 'Install and Setup for MAC users']),
                                      Module('Unit 2: Java Refresher', ['Basics of Java', 'Advanced Java']),
                                      Module('Unit 3: Tools', ['Android Studio IDE', 'Android File Structure', 'XML Files : Android User Interface']),
                                      Module('Unit 4: App Views', ['TextViews', 'Background Colors', 'ImageViews']),
                                      Module('Unit 5: Activities', ['Activity Life Cycle', 'Navigation']),
                                      Module('Unit 6: ListViews and Input Controls', ['Introduction to ListViews', 'Navigation']),
                                      Module('Unit 7: UI Layouts', ['Linear Layouts, Relative Layouts, Table Layouts', 'ScrollViews'])],
                high_quality_android: [ Module('Unit 1: Managing Memory', ['Android Memory Management', 'Managing Memory in the App']),
                                        Module('Unit 2: Performance Improvement', ['Tips and Tricks']),
                                        Module('Unit 3: Layout Performance', ['Optimizing Layout Hierarchies', 'Re-using Layouts', 'Loading Views On Demand', 'Making View Scrolling Smooth']),
                                        Module('Unit 4: Optimizing Battery Life', ['Network Traffic', 'Optimizing Network Use', 'Monitoring']),
                                        Module('Unit 5: Multi Threaded Operations', ['Threads', 'Thread Pool']),
                                        Module('Unit 6: App Responsiveness', ['ANR - Application Not Responding', 'Avoiding ANR'])],
                android_app_analytics: [  Module('Unit 1: Setup', ['Configuration', 'Adding Screen Tracking']),
                                          Module('Unit 2: Tools', ['Google Play Services SDK', 'Unity Plugin', 'Google Tag Manager'])],
                playstore_optimize: [ Module('Unit 1: Getting Discovered', ['Comprehensive Store Listing', 'Graphic and Image Assets', 'Localization']),
                                      Module('Unit 2: Monitoring', ['App Statistics and Reports', 'Ratings and Reviews'])],
                android_user_acquisition: [ Module('Unit 1: Advertising', ['Getting Featured', 'Cross Promotion', 'Incentivized Installs']),
                                            Module('Unit 2: Campaings', ['Interstitals', 'Video'])]
    }
    return modules[track]

def get_programs(track):
    programs = {
        mobile_track:
            [
                Program('iOS Programming 101', 'Aug 01 2015', 15, mobile_track, 'Learn the basics of programming in Objective C and setting up the fundamentals of iOS Dev Environment.', 'xcode', get_modules_for(ios_101)),
                Program('Building an iOS App', 'Aug 08 2015', 20, mobile_track, 'Build an iOS App from scratch with a deep dive into iOS Programming.', 'dev_ios', get_modules_for(build_ios_app)),
                Program('High quality iOS code', 'Aug 14 2015', 15, mobile_track, 'Learn what differentiates a high quality app from a mediocre one and how to code for excellence.', 'high_quality_ios_code', get_modules_for(high_quality_ios)),
                Program('App Analytics and Audience Engagement', 'Aug 01 2015', 25, mobile_track, 'Deep dive into analytics, data monitoring, audience segmentation and engagement.', 'analytics', get_modules_for(app_analytics)),
                Program('App Store Optimization', 'Aug 21 2015', 15, mobile_track, 'How to launch your app effectively and optimize for success in the app store.', 'appstore_opt', get_modules_for(appstore_optimize)),
                Program('User acquisition', 'Aug 28 2015', 20, mobile_track, 'Learn how to go from zero to the first thousand users to prove product market fit.', 'useracquisition', get_modules_for(user_acquisition)),
                Program('Android Programming 101', 'Sep 05 2015', 20, mobile_track, 'Android Development with a deep dive into Java Programming.', 'android_programming', get_modules_for(android_101)),
                Program('Building an Android App', 'Sep 12 2015', 20, mobile_track, 'Build an Android App from scratch.', 'building_an_android_app', get_modules_for(build_android_app)),
                Program('High quality Android code', 'Sep 19 2015', 25, mobile_track, 'What can make your App written the best way.', 'android_coding', get_modules_for(high_quality_android)),
                Program('Android App Analytics and Audience Engagement', 'Sep 26 2015', 20, mobile_track, 'Deep dive into analytics, data monitoring, audience segmentation and engagement.', 'analytics', get_modules_for(android_app_analytics)),
                Program('Google Play Store Optimization', 'Oct 01 2015', 25, mobile_track, 'Show your app to your customers.', 'google_play', get_modules_for(playstore_optimize)),
                Program('Android user acquisition', 'Oct 08 2015', 10, mobile_track, 'Techniques to soar your user base.', 'useracquisition', get_modules_for(android_user_acquisition))
            ],
        web_track:[Program('Building a Web App 101', 'Aug 02 2015', 20, web_track, 'A beginner course to understand all the skills required to be a good web developer.', 'full_stack', get_modules_for(web_track)),
                   Program('Going beyond HTML and CSS', 'Aug 09 2015', 20, web_track, 'Learn how to write D.R.Y code and the frameworks and libraries to achieve that.', 'less', get_modules_for(beyond_html)),
                   Program('Mathematics for Computer Science', 'Aug 23 2015', 30, web_track, 'The Calculus, Statistics, Combinatorics, Graph Theory, Probablity and number theory every data scientist should know.', 'cont_math', get_modules_for(math_for_cs)),
                   Program('Algorithms and Datastructures revisited', 'Aug 30 2015', 20, web_track, 'Computer science fundamentals which separates a good programmer from the best.', 'algo', get_modules_for(algs_and_ds)),
                   Program('Distributed computing', 'Sep 07 2015', 25, web_track, 'Basic concepts of distributed computing and how to execute it on the cloud.', 'dist', get_modules_for(distributed_computing)),
                   Program('Non-relational Databases', 'Sep 14 2015', 30, web_track, 'The new Non-relational mathematics and how commercial databases implement them.', 'no_sql', get_modules_for(non_relational_databases)),
                   Program('NLP 101', 'Sep 21 2015', 25, web_track, 'Tools and frameworks for processing and mining data from natural language text.', 'nlp', get_modules_for(nlp)),
                   Program('Big Data 101', 'Sep 28 2015', 20, web_track, 'Learn how to store massive amounts of data in distributed databases and process them using MapReduce.', 'big_data', get_modules_for(big_data))],
        designer:[
                Program('Design Thinking', 'Aug 03 2015', 15, designer, 'Learn the methods and approaches to use design as a "way of thinking" for creative action.', 'design_thinking', None),
                Program('iOS App Design', 'Aug 10 2015', 20, designer, 'From using 3D depth to layered design. Learn the design concepts required to make world class iOS Apps.', 'ios_design', None),
                Program('Android App Design', 'Aug 17 2015', 10, designer, """An in-depth look at Android's implementation of "material design" and how you can use it make elegant Android Apps.""", 'android_design', None),
                Program('Web Design', 'Aug 24 2015', 15, designer, "Parallax, Single Scroll pages, Sticky menus and other new age design paradigms which is shaping today's web pages.", 'web_design', None),
                Program('Responsive Design', 'Sep 03 2015', 20, designer, 'Learn how to make your website render seamlessly across a multitude of devices and resolutions.', 'responsive_design', None),
                Program('Branding Concepts', 'Sep 10 2015', 20, designer, 'How to turn an idea into a product and brand that people love.', 'branding', None)
            ],
        product_manager:[
            Program('The new age Product Manager', 'Aug 04 2015', 10, product_manager, 'Learn to handle challenges in software development with ever changing requirements and faster iterations.', 'product', None),
            Program('Tools for Product Management', 'Aug 11 2015', 15, product_manager, 'Master new age product management tools like Trello, Typeform and Quip to make you more productive and agile.', 'tools', None),
            Program('Design Thinking for Management', 'Aug 18 2015', 10, product_manager, 'Integrate pillars of design thinking- desirability, feasibility and viability into product management.', 'design_thinking', None),
            Program('Agile based Product Management', 'Aug 25 2015', 20, product_manager, 'Embrace changes and make it work to your favor through agile based product management.', 'agile', None),
            Program('Client Management', 'Sep 01 2015', 20, product_manager, 'Learn all the tricks of the trade to develop a long lasting and happy relationship with your clients.', 'client_managament', None),
            Program('Lean Product Management', 'Sep 08 2015', 15, product_manager, 'Learn to work in iterations to build, measure and learn only what is required and save valuable resources.', 'product_management', None)
            ],
        founder: [
            Program('Bootstrapping your startup', 'Aug 05 2015', 10, founder, 'Make the most of your own resources to build a startup without an outside investor', 'bootstrap', None),
            Program('Raising the seed round', 'Aug 12 2015', 15, founder, 'Learn the nuances of acquiring a seed round investment to shape up your idea', 'seed', None),
            Program('Raising the Series A round', 'Aug 19 2015', 10, founder, 'Obtain the skills it takes to get the best term sheet from an investor at the most crucial stage of your startup', 'series-a', None),
            Program('MVP and Product Market Fit', 'Aug 26 2015', 25, founder, 'Decide the right features that goes into your MVP to produce highest return on investment', 'mvp', None),
            Program('Investor Management', 'Sep 02 2015', 20, founder, 'Understand how to choose investors and strategize accepting funds', 'investor', None)
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