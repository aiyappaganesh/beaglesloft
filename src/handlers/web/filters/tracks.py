from google.appengine.ext.webapp import template
import logging
from model.managed_user import ManagedUser
from model.enroll_track import EnrollTrack
from model.ui_models.factories.donut_factory import DonutFactory
from model.ui_models.donut import DonutSegment
from random import randint

register =  template.create_template_register()

@register.filter(name='is_enrolled')
def is_enrolled(value, arg):
    return value.get(arg)

@register.filter(name='get_managed')
def get_managed(value, arg):
    managed_users = ManagedUser.get_managed_users(value)
    donut_vals = []
    if managed_users and len(managed_users) > 0:
        for managed_user in managed_users:
            if EnrollTrack.is_enrolled(managed_user.user.email, arg):
                donut_vals.append((managed_user.user.name,[DonutSegment(randint(0,50), '#1c758a'), DonutSegment(randint(0,50), '#58c4dd')]))
    else:
        donut_vals = [
            ('James', [DonutSegment(randint(0,50), '#1c758a'), DonutSegment(randint(0,50), '#58c4dd')], '/assets/img/tracks/mobile_dev.png'),
            ('Abdul', [DonutSegment(randint(0,50), '#1c758a'), DonutSegment(randint(0,50), '#58c4dd')], '/assets/img/tracks/mobile_dev.png'),
            ('Raj', [DonutSegment(randint(0,50), '#1c758a'), DonutSegment(randint(0,50), '#58c4dd')], '/assets/img/tracks/mobile_dev.png'),
            ('David', [DonutSegment(randint(0,50), '#1c758a'), DonutSegment(randint(0,50), '#58c4dd')], '/assets/img/tracks/mobile_dev.png'),
            ('Chang', [DonutSegment(randint(0,50), '#1c758a'), DonutSegment(randint(0,50), '#58c4dd')], '/assets/img/tracks/mobile_dev.png')
            ]
    return DonutFactory.get_donuts(100, 0.875, donut_vals, 'transparent', '#ddd')