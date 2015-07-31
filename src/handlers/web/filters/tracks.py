from google.appengine.ext.webapp import template
import logging

register =  template.create_template_register()

@register.filter(name='is_enrolled')
def is_enrolled(value, arg):
    return value.get(arg)