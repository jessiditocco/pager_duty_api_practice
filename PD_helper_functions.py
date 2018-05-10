import os
import requests


# This is how to set the header in python
# Note that this only sets the header; other code may be needed to 
#create and process the request.

authorization_token = os.environ.get('API_KEY')

pagerduty_session = requests.Session()
pagerduty_session.headers.update({
  'Authorization': 'Token token=' + authorization_token,
  'Accept': 'application/vnd.pagerduty+json;version=2'
})

json = pagerduty_session.get('https://api.pagerduty.com/users')

print json