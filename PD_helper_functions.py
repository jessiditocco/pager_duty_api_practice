# import os
# import requests


# # This is how to set the header in python
# # Note that this only sets the header; other code may be needed to 
# #create and process the request.

# authorization_token = os.environ.get('API_KEY')

# pagerduty_session = requests.Session()
# pagerduty_session.headers.update({
#   'Authorization': 'Token token=' + authorization_token,
#   'Accept': 'application/vnd.pagerduty+json;version=2'
# })

# request = pagerduty_session.get('https://api.pagerduty.com/users')

# data = request.json()

# print data["users"][0]["name"]


################################# POST REQUEST #################################
# ############################# Adding users to Demo Account #####################

#  # Say, try writing a python script to add users to your demo account
#  # given a CSV file of the user's info.


import os
import requests
import json
import csv

pd_base_url = 'https://api.pagerduty.com/users'

authorization_token = os.environ.get('API_KEY')

headers = {
            "Content-Type": "application/json",
            "Accept": "application/vnd.pagerduty+json;version=2",
            "From": "jessi.ditocco@gmail.com",
            "Authorization": "Token token={}".format(authorization_token)
           }

def get_users():
    """Get all of the users"""

    pagerduty_session = requests.Session()

    headers = {
      "Accept": "application/vnd.pagerduty+json;version=2",
      "Authorization": "Token token=wGYXckCvnLAWa_B6zj2m"
    }

    request = pagerduty_session.get(pd_base_url, headers=headers)

    data = request.json()

    return data['users'][2]['id']

# print get_users()

def get_user_by_id(user_id):
    """Get all of the users"""

    url = pd_base_url + "/{}".format(user_id)

    pagerduty_session = requests.Session()

    headers = {
      "Accept": "application/vnd.pagerduty+json;version=2",
      "Authorization": "Token token=wGYXckCvnLAWa_B6zj2m"
    }


    request = pagerduty_session.get(url, headers=headers)

    data = request.json()

    return data

# print get_user_by_id("PRS2BTV")


def create_user(name, email, role):
    """Creates a user. Returns user information"""

    payload = {
            "type": "user",
            "name": name,
            "email": email,
            "role": role,
            }
    pagerduty_session = requests.Session()

    request = pagerduty_session.post(pd_base_url, headers=headers, data=json.dumps(payload))

    data = request.json()

    return data['user']['id']

# print create_user("Lorin", "lorin@gmail.com", "admin")


def create_user_contact_method(user_id, contact_type, address):
    """Creates a contact method of the user and returns ID."""

    url = pd_base_url + "/{}/contact_methods".format(user_id)
    payload =  {
        "contact_method": {
            "type": contact_type,
            "label": "Work",
            "address": address
            }
        }

    pagerduty_session = requests.Session()

    request = pagerduty_session.post(url, headers=headers, data=json.dumps(payload))

    data = request.json()

    return data.keys()


def proccess_csv():
    """Parses and reads the contents of the csv file with user info"""

    with open('users.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            print row
            name = row[0]
            email = row[1] 
            role = row[2]
            address = row[3]
            contact_type = row[4]

            user = create_user(name, email, role)

            user_id = user['id']

            create_user_contact_method(user_id, contact_type, address)


# proccess_csv()