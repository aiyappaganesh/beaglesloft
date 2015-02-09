from google.appengine.api import urlfetch
import urllib
import logging
import base64
import json

api_public_key = 'db43ff2f5a3bdde4a5f2a2a391e982bd'
api_private_key = 'b7d311796b51ea4f7865ccf1807bc044'
contact_url = 'https://api.mailjet.com/v3/REST/contact'
add_to_list_url = 'https://api.mailjet.com/v3/REST/listrecipient'
list_id = 8  # Use 8 for prod and 4 for testing

def get_contact(email):
    error_msg = ''
    result = urlfetch.fetch(contact_url+'/'+email,
                          urlfetch.GET,
                          headers = {"Authorization": "Basic %s" % base64.b64encode(api_public_key+':'+api_private_key)},
                          deadline = 60)
    status_code = result.status_code
    content = json.loads(result.content)
    if 200 <= status_code < 300:
        if 'Data' in content:
            if 'ID' in content['Data'][0]:
                contact_id = content['Data'][0]['ID']
                return {'id':contact_id, 'error':error_msg}
    else:
        if 'ErrorMessage' in content:
            error_msg = content['ErrorMessage']
    return {'id':-1, 'error':error_msg}

def create_contact(email, name):
    error_msg = ''
    result = urlfetch.fetch(contact_url,
                          urllib.urlencode(
                              {
                                  'Email': email,
                                  'Name': name
                              }
                          ),
                          urlfetch.POST,
                          headers = {"Authorization": "Basic %s" % base64.b64encode(api_public_key+':'+api_private_key)},
                          deadline = 60)
    status_code = result.status_code
    content = json.loads(result.content)
    if 200 <= status_code < 300:
        if 'Data' in content:
            if 'ID' in content['Data'][0]:
                contact_id = content['Data'][0]['ID']
                return {'id':contact_id, 'error':error_msg}
    else:
        if 'ErrorMessage' in content:
            error_msg = content['ErrorMessage']
    return {'id':-1, 'error':error_msg}

def add_contact_to_list(contact_id):
    error_msg = ''
    result = urlfetch.fetch(add_to_list_url,
                          urllib.urlencode(
                              {
                                  'ContactID': contact_id,
                                  'ListID': list_id,
                                  'IsActive': 'true'
                              }
                          ),
                          urlfetch.POST,
                          headers = {"Authorization": "Basic %s" % base64.b64encode(api_public_key+':'+api_private_key)},
                          deadline = 60)
    status_code = result.status_code
    content = json.loads(result.content)
    if 200 <= status_code < 300:
        if 'Data' in content:
            if 'ID' in content['Data'][0]:
                list_contact_id = content['Data'][0]['ID']
                return {'id':list_contact_id, 'error':error_msg}
    else:
        if 'ErrorMessage' in content:
            error_msg = content['ErrorMessage']
    return {'id':-1, 'error':error_msg}

def subscribe(email, fname, lname):
    subscribe_result = ''
    get_contact_result = get_contact(email)
    if get_contact_result['id'] == -1:
        create_contact_result = create_contact(email, fname+' '+lname)
        if create_contact_result['id'] != -1:
            list_result = add_contact_to_list(create_contact_result['id'])
            if list_result != -1:
                subscribe_result = 'Successfully subscribed'
            else:
                subscribe_result = 'Error: '+list_result['error']
        else:
            subscribe_result = 'Error: '+create_contact_result['error']
    else:
        list_result = add_contact_to_list(get_contact_result['id'])
        if list_result['id'] != -1:
            subscribe_result = 'Successfully subscribed'
        else:
            subscribe_result = 'Error: '+list_result['error']
    return subscribe_result