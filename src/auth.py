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
