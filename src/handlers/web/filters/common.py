from handlers.web.web_request_handler import register

@register.filter(name='dict_lookup')
def dict_lookup(value, arg):
    return value.get(arg)