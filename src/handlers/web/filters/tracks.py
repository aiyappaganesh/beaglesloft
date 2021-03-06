import logging
from model.managed_user import ManagedUser
from model.enroll_program import EnrollProgram
from model.ui_models.factories.donut_factory import DonutFactory
from model.ui_models.donut import DonutSegment
from random import randint, random, uniform
from handlers.web.web_request_handler import register
from model.program import Program
from model.track import Track
from model.program_module import ProgramModule

@register.filter(name='is_enrolled')
def is_enrolled(value, arg):
    return value.get(arg)

@register.filter(name='is_enrolled_program')
def is_enrolled_program(value, arg):
    ids = arg.split(' ')
    return EnrollProgram.is_enrolled_program(value, ids[0], ids[1])

@register.filter(name='get_managed')
def get_managed(value, arg):
    managed_users = ManagedUser.get_managed_users(value)
    donut_vals = []
    if managed_users and len(managed_users) > 0:
        for managed_user in managed_users:
            args = arg.split(" ")
            if args[0] == "track":
                if EnrollProgram.is_enrolled_track(managed_user.user.email, args[1]):
                    enrolled_programs_count = float(len(EnrollProgram.get_enrolled_programs(managed_user.user.email, args[1])))
                    programs_count = float(Program.all().ancestor(Track.get_by_key_name(args[1])).count())
                    score = round((enrolled_programs_count/programs_count)*100,2)
                    engage_score = round(random()*score,0)
                    engage_score = int(engage_score) if engage_score > 1 else 1
                    donut_vals.append((managed_user.user.name,[DonutSegment(engage_score, '#1c758a'), DonutSegment(score, '#58c4dd')]))
            elif args[0] == "program":
                if EnrollProgram.is_enrolled_program(managed_user.user.email, args[1], args[2]):
                    track = Track.get_by_key_name(args[2])
                    program = Program.get_by_key_name(args[1], parent=track)
                    modules = ProgramModule.all().ancestor(program).order('name')
                    modules_count = modules.count()*1.0
                    completed_modules = []
                    for module in modules:
                        if module.completed:
                            completed_modules.append(module)
                    completed_modules_count = len(completed_modules)
                    score = (completed_modules_count/modules_count)*100.0
                    engage_score = round(score*random(),0)
                    engage_score = int(engage_score) if engage_score > 1 else 1
                    donut_vals.append((managed_user.user.name,[DonutSegment(engage_score, '#1c758a'), DonutSegment(score, '#58c4dd')]))
    return DonutFactory.get_donuts(100, 0.875, donut_vals, 'transparent', '#ddd')