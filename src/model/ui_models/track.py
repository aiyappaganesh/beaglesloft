class Program():
    def __init__(self, title, start_date, num_spots, track):
        self.title = title
        self.start_date = start_date
        self.num_spots = num_spots
        self.track = track
        self.id = title.lower().replace(' ', '_')
        self.link = '/tracks/program_listing?id=' + self.id

class Track():
    def __init__(self, title, icon, programs):
        self.icon = icon + '.png'
        self.highlight_icon = icon + '_dark.png'
        self.name = title
        self.programs = programs
        self.id = title.lower().replace(' ', '_')