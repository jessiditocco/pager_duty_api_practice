import requests
import os
import json

api_key = os.environ.get('API_KEY')
base_url = 'https://api.pagerduty.com/users'


def list_users():
    """List all users"""

    headers = {
      "Accept": "application/vnd.pagerduty+json;version=2",
      "Authorization": "Token token={}".format(api_key)
    }

    pd_session = requests.Session()
    request = pd_session.get(base_url, headers=headers)

    data = request.json()
    user_id = data['users'][4]['id']

    print user_id


def get_user_by_id(user_id):
    """Returns a user object by id"""

    headers = {
        "Accept": "application/vnd.pagerduty+json;version=2",
        "Authorization": "Token token={}".format(api_key)
    }

    url = base_url + '/{}'.format(user_id)

    pd_session = requests.Session()

    request = pd_session.get(url, headers=headers)

    data = request.json()
    print data

    return data