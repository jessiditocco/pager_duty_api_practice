import sys
import requests
import json

api_key = sys.argv[1]

base_url = 'https://api.pagerduty.com/users'
authorization_token = 'w_8PcNuhHa-y3xYdmc1x'

def update_user(user_id):
    """Updates a user from a pagerduty account"""

    url = base_url + "/{}".format(user_id)
    headers = {
      "Content-Type": "application/json",
      "Accept": "application/vnd.pagerduty+json;version=2",
      "Authorization": "Token token=wGYXckCvnLAWa_B6zj2m"
    }

    payload = {"name": "hannah2"}


    pagerduty_session = requests.Session()
    request = pagerduty_session.put(url, headers=headers, data=json.dumps(payload))

    print request.json()


update_user('PRS2BTV')




