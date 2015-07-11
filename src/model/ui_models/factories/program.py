from model.ui_models.program import Program

mobile_dev = 'MOBILE DEVELOPMENT' 
full_stack = 'Full Stack Developer' 

programs = {mobile_dev: [Program('iOS Programming 101', 'Aug 1 2015', 20, mobile_dev, '/assets/img/landing/lofts.png')],
			full_stack: [Program('Web Development 101', 'Aug 1 2015', 20, full_stack)]}

class Programs():
	@classmethod
	def get_tracks(cls):
		return [mobile_dev, full_stack]

	@classmethod
	def get_programs_for(cls, track):
		return programs[track]

	@classmethod
	def get_programs_dict(cls):
		tracks = Programs.get_tracks()
		ret_val = {}
		for track in tracks:
			ret_val[track] = Programs.get_programs_for(track)
		return ret_val