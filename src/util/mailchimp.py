from google.appengine.api import urlfetch
import urllib

api_key = '45f37b02b487238a7c8d0bb66b0e5049-us8'
subscribe_url = 'https://us8.api.mailchimp.com/2.0/lists/subscribe.json'
list_id = '5f30839cdd' #change to the real list id when ready for production

def subscribe(email):
    return urlfetch.fetch(subscribe_url,
                          urllib.urlencode(
                              {'apikey': api_key,
                               'id': list_id,
                               'email[email]': email,
                               'double_optin': False,
                               'send_welcome': True}),
                          urlfetch.POST,
                          deadline = 60)