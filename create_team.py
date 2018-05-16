import csv
import sys
import requests
import json

base_url = 'https://api.pagerduty.com/teams'


def proccess_csv(team_data):
    """Function that parses csv file with team information"""

    with open(team_data) as csvfile:
        team_data = csv.reader(csvfile, delimiter=',')
        for line in team_data:
            team_type = line[0]
            name = line[1]
            description = line[2]


            create_team(team_type, name, description)




def create_team(team_type, name, description):
    """Function that creates a team from csv file with team information"""
    
    payload = {"type": team_type, 'name': name, 'description': description}

    headers = {
      "Content-Type": "application/json",
      "Accept": "application/vnd.pagerduty+json;version=2",
      "Authorization": "Token token=wGYXckCvnLAWa_B6zj2m"
      }

    pd_session = requests.Session()

    request = pd_session.post(base_url, headers=headers, data=json.dumps(payload))

    print request.json()


if __name__ == "__main__":

    api_key='wGYXckCvnLAWa_B6zj2m'
    team_data = sys.argv[1]
 
    proccess_csv(team_data)
