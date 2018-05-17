# create a service pagerduty
import sys
import requests
import csv
import json

api_key='wGYXckCvnLAWa_B6zj2m'

pd_base_url = 'https://api.pagerduty.com/'

csv_file = sys.argv[1]

def parse_csv():
    """Parses csv file of services and calls function to create a service"""

    with open(csv_file, 'rb') as csvfile:
        service_info = csv.reader(csvfile, delimiter=",")
        for row in service_info:
            service_type = row[0]
            name = row[1]
            description = row[2]
            escalation_policy_type = row[3]

            create_service(service_type, name, description, escalation_policy_type)


def create_service(service_type, name, description, escalation_policy_type):
    """Creates a service using PD REST api."""

    headers = {
      "Content-Type": "application/json",
      "Accept": "application/vnd.pagerduty+json;version=2",
      "Authorization": "Token token=wGYXckCvnLAWa_B6zj2m"
    }

    url = pd_base_url + "/{}".format('services')

    service = {
          "service": {
            "type": service_type,
            "name": name,
            "description": description,
            # "escalation_policy": {
            #   "id": "PWIP6CQ",
            #   "type": escalation_policy_type
            #   }
            }
        }

    r = requests.post(url, headers=headers, data=json.dumps(service))

    print r.json()

parse_csv()