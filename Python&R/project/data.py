import datetime
import json

teams = [
    {
        "id": 1,
        "date": datetime.date(2022, 10, 18),
        "name": "simba",
        "type": "Boys",
        "fee": True,
        "fee_amount": 99,
    },
    {
        "id": 2,
        "date": datetime.date(2022, 10, 18),
        "name": "quenss",
        "type": "girls",
        "fee": False,
        "fee_amount": 0,
    },
    {
        "id": 3,
        "date": datetime.date(2022, 10, 18),
        "name": "luton",
        "type": "Boys",
        "fee": True,
        "fee_amount": 990,
    },
    {
        "id": 4,
        "date": datetime.date(2022, 10, 18),
        "name": "jkt",
        "type": "Boys",
        "fee": True,
        "fee_amount": 990,
    },
    {
        "id": 5,
        "date": datetime.date(2022, 10, 18),
        "name": "atleti",
        "type": "Boys",
        "fee": True,
        "fee_amount": 990,
    },
    {
        "id": 6,
        "date": datetime.date(2022, 10, 18),
        "name": "crown",
        "type": "girls",
        "fee": True,
        "fee_amount": 100,
    },
]
'''
for team in teams:
    if team['id'] == 1:
        team['name'] = 'yangaan'
        print(team)
#print(teams)
'''
def show_team(teams):
    """Print team information based on the team id"""
    team_id = int(input("Id of time you would like to show: "))
    for team in teams:
        if team['id']== team_id:
            print(team)
            
show_team(teams)



'''
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
'''
