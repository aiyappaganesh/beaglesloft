from model.member import Member
import logging

def _member_logged_in(handler):
    if not 'member' in handler.session:
        handler.redirect('/members/login')
        return False
    if Member.get_by_email(handler.session['member']):
        return True
    return False

def login_required(fn):
    def check_login(self, *args):
        if _member_logged_in(self):
            fn(self, *args)
    return check_login
