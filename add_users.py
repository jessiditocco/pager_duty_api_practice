import sys
import json
import requests
import csv


def parse_csv(user_info):
    """Parses a CSV file of user data"""

    with open(user_info) as csvfile:
        user_info = csv.reader(csvfile, delimiter=',')
        for line in user_info:
            name = line[0]
            email = line[1]
            role = line[2]
            phone_number = line[3]
            phone = line[4]

            create_user(name, email)

def create_user(name, email, type='user'):
    """Create a pagerduty user on demo account; returns user"""

    payload = {'type': type, 'name': name, 'email': email}

    headers = {
        'Authorization': 'Token token=' + api_key,
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'From':'jessi.ditocco@gmail.com',
        'Content-Type': 'application/json',

    }

    pagerduty_session = requests.Session()
    
    request = pagerduty_session.post(base_url, 
        headers=headers, data=json.dumps(payload))

    print request.json()


if __name__ == "__main__":

    api_key='wGYXckCvnLAWa_B6zj2m'
    user_info = sys.argv[1]
    base_url = 'https://api.pagerduty.com/users'

    parse_csv(user_info)
