class Track():
    def __init__(self, title, id=None, subtracks=None):
        self.title = title
        if subtracks:
        	self.subtracks = subtracks
    	if id:
    		self.id = id