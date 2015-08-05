from google.appengine.ext import db
from model.track import Track
from model.program import Program
import logging

class EnrollProgram(db.Model):
    engagement = db.FloatProperty(indexed=False)
    completed_courses = db.IntegerProperty(indexed=False)

    @classmethod
    def create(cls, member, program):
        cls(key_name=member.email, parent=program).put()

    @classmethod
    def is_enrolled_program(cls, email, program_id):
        return EnrollProgram.get_by_key_name(email, parent=Program.get_by_key_name(program_id))

    @classmethod
    def is_enrolled_track(cls, email, track_id):
        enrolled_programs = EnrollProgram.get_enrolled_programs(email, track_id)
        return len(enrolled_programs) > 0

    @classmethod
    def get_enrolled_programs(cls, email, track_id):
        track_programs = Program.all().ancestor(Track.get_by_key_name(track_id))
        enrolled_programs = []
        for program in track_programs:
            enrolled_program = EnrollProgram.get_by_key_name(email, parent=program)
            if enrolled_program:
                enrolled_programs.append(enrolled_program)
        logging.info(enrolled_programs)
        return enrolled_programs