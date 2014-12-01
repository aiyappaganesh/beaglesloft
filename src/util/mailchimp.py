from google.appengine.api import urlfetch
import urllib

api_key = '45f37b02b487238a7c8d0bb66b0e5049-us8'
subscribe_url = 'https://us8.api.mailchimp.com/2.0/lists/subscribe.json'
list_id = '07c01016bf'

def subscribe(email, fname, lname):
    return urlfetch.fetch(subscribe_url,
                          urllib.urlencode(
                              {'apikey': api_key,
                               'id': list_id,
                               'email[email]': email,
                               'merge_vars[FNAME]': fname,
                               'merge_vars[LNAME]': lname,
                               'double_optin': False,
                               'send_welcome': True}),
                          urlfetch.POST,
                          deadline = 60)