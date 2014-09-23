from google.appengine.api import urlfetch
import urllib

api_key = '45f37b02b487238a7c8d0bb66b0e5049-us8'
subscribe_url = 'https://us8.api.mailchimp.com/2.0/lists/subscribe.json'
list_id = '938a272040' #change to '5f30839cdd' when testing and '938a272040' for production

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