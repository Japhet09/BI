# This program
from team import Team

teams = [
    ]


def main():
    pass



def create_team():
    """Return a new team an instance from the Team class"""
    global teams
    # Get the name, type , fee status  from the user
    name = input("Name of the team: ").strip()
    type = input("Type of team (B/G): ").strip()
    fee_paid = input("Fee paid (Y/N: ").strip()

    # create and return the team object
    team = Team(name, type, fee_paid)

    teams.append(team.store_data())
    # print(teams)
    return teams


def show_team_by_id(teams):
    """Return team information based on the team id"""
    while True:
        team_id = int(input("Id of team you would like to show: "))
        for team in teams:
            if team["id"] == team_id:
                return (print(team))  
            elif team["id"] != team_id:
                continue # ask user to enter the team id again


def show_team_by_type(teams_list):
    """Return team information based on type"""
    while True:
        team_type = input("Type of team to show (B/G): ").strip()
        if team_type.upper() == 'B':
            type = 'BOYS'
        elif team_type.upper() == 'G':
            type = 'GIRLS'
        else:
            type = None
            print('Please Enter a valid team type')
            
        for team in teams_list:
            if team["type"] == type:
                return (print(team))
            else:
                continue


def show_all_teams(teams_list):
    """Print all teams created by the user"""
    for team in teams_list:
        print(team)
 

def update_name():
    '''Update the team name based on the team id'''
    global teams 
    team_id = int(input("Enter team id to update: "))
    new_name = input("New Team Name").upper()
    for team in teams:
        if team['id'] == team_id:
            team['name'] = new_name         
    return teams

def update_type():
    '''Update the type of the team'''
    global teams 
    team_id = int(input("Enter team id to update: "))
    new_type = input("New Team type").upper()
    for team in teams:
        if team['id'] == team_id:
            team['type'] = new_type         
    return teams

def update_fees():
    '''Update the fee status and fee amount '''
    global teams 
    team_id = int(input("Enter team id to update: "))
    new_fee_paid = input("New Fee status (Y/N): ").upper()
    for team in teams:
        if team['id'] == team_id:
            if new_fee_paid == 'Y':
                team['fee_paid'] = True
                team['fee_amount'] = 99
            elif new_fee_paid == 'N':
                team['fee_paid'] = False
                team['fee_amount'] = 0        
    return teams
    
    
def display_menu():
    print('\t MENU ')
    print('1) Create a new team ')
    print('2) Show a team using ID ')
    print('3) Show a team using type ')
    print('4) Show all teams ')
    print('5) Update team ')
    print('0) Quit Program ')
    
def update_submenu():
    print('\t UPDATE SUB MENU')
    print('51) Update Team Name')
    print('52) Update Team Type')
    print('53) Update Team Fee Status')
    
    
    
    
    
    
if __name__ == "__main__":
    main()
