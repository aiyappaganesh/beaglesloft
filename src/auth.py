from model.member import Member
import urllib
import logging

def _member_logged_in(handler):
    if not 'member' in handler.session:
        handler.redirect('/members/login?' + urllib.urlencode({'redirect_url': handler.request.url}))
        return False
    member = Member.get_by_email(handler.session['member'])
    if not member:
        return False
    return True

def login_required(fn):
    def check_login(self, *args):
        if _member_logged_in(self):
            fn(self, *args)
    return check_login

def _check_access_code(handler):
    if not 'access_code' in handler.session:
        handler.redirect('/member_access')
        return False
    if not handler.session['access_code'] == '2013':
        return False
    return True

def access_code_required(fn):
    def check_access_code(self, *args):
        if _check_access_code(self):
            fn(self, *args)
    return check_access_code
