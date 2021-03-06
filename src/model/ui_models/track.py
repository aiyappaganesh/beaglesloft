class Module():
    def __init__(self, title, units):
        self.title = title
        self.units = units

class Program():
    def __init__(self, title, start_date, num_spots, track, description, snapshot, modules):
        self.title = title
        self.description = description
        self.start_date = start_date
        self.num_spots = num_spots
        self.track = track
        self.id = title.lower().replace(' ', '_')
        self.snapshot = '/assets/img/tracks/snapshots/' + snapshot + '.png'
        self.link = '/tracks/program_listing?id=' + self.id
        self.modules = modules

class Track():
    def __init__(self, title, icon, programs):
        self.icon = icon + '.png'
        self.highlight_icon = icon + '_dark.png'
        self.name = title
        self.programs = programs
        self.id = title.lower().replace(' ', '_')