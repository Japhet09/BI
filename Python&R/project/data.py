import datetime
import json

team = [
    {
        "id": 1,
        "date": "2022/10/19",
        "name": "SIMBA",
        "type": "BOYS",
        "fee": True,
        "fee_amount": 99,
    },
    {
        "id": 2,
        "date": "2022/10/19",
        "name": "QUENSS",
        "type": "GIRLS",
        "fee": True,
        "fee_amount": 99,
    },
    {
        "id": 3,
        "date": "2022/10/19",
        "name": "LUTON",
        "type": "BOYS",
        "fee": True,
        "fee_amount": 99,
    },
    {
        "id": 4,
        "date": "2022/10/19",
        "name": "JKT",
        "type": "BOYS",
        "fee": False,
        "fee_amount": 0,
    },
    {
        "id": 5,
        "date": "2022/10/19",
        "name": "ATLETI",
        "type": "BOYS",
        "fee": False,
        "fee_amount": 0,
    },
    {
        "id": 6,
        "date": "2022/10/19",
        "name": "CROWN",
        "type": "GIRLS",
        "fee": True,
        "fee_amount": 99,
    },
]
"""
for team in teams:
    if team['id'] == 1:
        team['name'] = 'yangaan'
        print(team)
#print(teams)
"""


def show_team(teams):
    """Print team information based on the team id"""
    team_id = int(input("Id of time you would like to show: "))
    for team in teams:
        if team["id"] == team_id:
            print(team)

for t in team:
    print(t["id"])

"""
def write_data(data):
    
    with open('team_data.txt', 'w') as f:
        for team in data:
            for key, value in team.items():
                f.write('%s:%s\n' % (key, value))
                
def write_data2(data):
    
    with open('team_data.txt', 'w') as f:
        for team in data:
            f.write(str(team)) 
            f.write('\n')
        
write_data2(teams)

def read_data(data):
    t = []
    with open('team_data.txt', 'r') as f:
        for i in f:
            k = i.strip('\n')
            t.append(k)
    return t

a = read_data('team_data.txt')
"""

dd = "{'id': 1, 'date': '2022/10/20', 'name': 'SASA', 'type': 'BOYS', 'fee_paid': False, 'fee_amount': 0}"
d = json.loads(dd)
