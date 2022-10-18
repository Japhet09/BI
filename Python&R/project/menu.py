# This program
from team import Team
teams =[
    {
        "id": 1,
        "date": "2022/10/19",
        "name": "simba",
        "type": "Boys",
        "fee": True,
        "fee_amount": 99,
    },
    {
        "id": 2,
        "date": "2022/10/19",
        "name": "quenss",
        "type": "girls",
        "fee": False,
        "fee_amount": 0,
    },
    {
        "id": 3,
        "date": "2022/10/19",
        "name": "luton",
        "type": "Boys",
        "fee": True,
        "fee_amount": 990,
    },
    {
        "id": 4,
        "date": "2022/10/19",
        "name": "jkt",
        "type": "Boys",
        "fee": True,
        "fee_amount": 990,
    },
    {
        "id": 5,
        "date": "2022/10/19",
        "name": "atleti",
        "type": "Boys",
        "fee": True,
        "fee_amount": 990,
    },
    {
        "id": 6,
        "date": "2022/10/19",
        "name": "crown",
        "type": "girls",
        "fee": True,
        "fee_amount": 100,
    },
]


def main():
    # print(create_team())
    #teams = [] # a list of dictinary of teams created
    #create_team(teams)
 
   # update_team(teams)
    
    
    update_team()
    show_all_teams(teams)


def create_team(teams):
    """Return a new team an instance from the Team class"""

    # Get the name, type , fee status and fee amount from the user
    name = input("Name of the team: ").strip()
    type = input("Type of team: ").strip()
    fee_paid = bool(input("Fee paid (True/False): ").strip())
    fee_amount = int(input("Fee amount: "))

    # create and return the team object
    team = Team(name, type, fee_paid, fee_amount)
    
    teams.append(team.store_data())
    return teams
    


def show_team(teams):
    """Print team information based on the team id"""
    team_id = int(input("Id of time you would like to show: "))
    for team in teams:
        if team['id']== team_id:
            print(team)


def show_team_by_type(teams_list):
    '''Print team based on type'''
    team_type = input("Type of team to show: ").strip()
    for team in teams_list:
        if team['type'] == team_type:
            print(team)

def show_all_teams(teams_list):
    '''Print all teams created by the user'''
    for team in teams_list:
        print(team)


def update_team():
    '''Update the team name, type, fee status or fee amount'''
    team_id = int(input('Enter id of team to update: '))
    item = input('Field to update')
    new_value = input('New value: ')
    global teams
    for t in teams:
        if t['id'] == team_id:
            if t['name'] == item:
                t['name'] = new_value
            elif t['type'] == item:
                t['type'] = new_value
            elif t['fee_paid'] == item:
                t['fee_paid'] = bool(new_value)
            elif t['fee_amount'] == item:
                t['fee_amount'] = int(new_value)
    return teams
                
            
            
    
    
if __name__ == "__main__":
    main()
