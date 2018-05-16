# write a python script to add users to your demo account 
# given a CSV file of the user's info. Basically go through 
# and practice making API calls.

# name,email,role,address,type
# John Doe,john.doe@example.com,admin,5555555555,phone

import csv
import sys
import requests
import json

api_key='wGYXckCvnLAWa_B6zj2m'
pd_base_url = 'https://api.pagerduty.com/'



def proccess_csv():
    """Proccesses the CSV file and creates a user for each line."""

    csv_file = sys.argv[1]

    with open(csv_file) as user_file:
        for user in user_file:
            user_info = user.split(",")

            name = user_info[0]
            email = user_info[1]
            account_type = user_info[2]
            address = user_info[3]
            contact_type = user_info[4]

            # Add contact methods

            if contact_type == "email":
                contact_method = {"contact_method": {
                    "type": "email_contact_method",
                    "label": "Work",
                    "address": email
                    }
                    }
            elif contact_type == "phone":
                contact_method = {"contact_method": {
                "type": "phone_contact_method",
                "label": "Work",
                "address": address
                }}

            # Create a new User
            new_user_id = create_user(name, email, account_type)

            
            create_user_contact_method(new_user_id, address, contact_method)


def create_user(name, email, account_type):
    """Creates a PD user using REST api."""

    url = pd_base_url + '/{}'.format('users')
    headers = {
      "Content-Type": "application/json",
      "Accept": "application/vnd.pagerduty+json;version=2",
      "From": "jessi.ditocco@gmail.com",
      "Authorization": "Token token={}".format(api_key)
    }

    payload = {'type': 'user', 
                'name': name, 
                'email': email, 
                'role': account_type}

    r = requests.post(url, data=json.dumps(payload), headers=headers)

    new_user_id = r.json()['user']['id']
    
    print new_user_id
    return new_user_id


def create_user_contact_method(new_user_id, address, contact_method):
    """Creates a contact method based on user_id"""

    headers = {
          "Content-Type": "application/json",
          "Accept": "application/vnd.pagerduty+json;version=2",
          "Authorization": "Token token=wGYXckCvnLAWa_B6zj2m"
        }

    url = pd_base_url + "/users/{}/contact_methods".format(new_user_id)



    r = requests.post(url, data=json.dumps(contact_method), headers=headers)

    print r.json()




proccess_csv()

