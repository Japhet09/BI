# This script contains functions to be imported 
# by other programs to create, show, update  and delete teams

# import the Team class to be used to create teams(instances
# of the Team class)
from team import Team
# json module to save and load team data
import json
import ast

# All teams created will be stored in the variable teams
teams = []

class Menu:
    '''Menu class for creating, updating, displaying and deleting teams'''
    
    def create_team():
        """Return a list teams  instances from the Team class"""
        # We use global teams variable since we are going to modify the list
        global teams
        
        # Get the name, type , fee status  from the user
        name = input("Name of the team: ").strip()
        type = input("Type of team (B/G): ").strip()
        fee_paid = input("Fee paid (Y/N: ").strip()

        # create and return the team object
        t = Team(name, type, fee_paid)
        
        # Call the store_data method from the Team class to store the team
        # object as a dictionary
        team = t.store_data()
        
        # Append the dictionary (team) to the list of teams
        teams.append(team)
        return teams


    def show_team_by_id():
        """Print team information using the team id"""
        while True:
            team_id = int(input("Id of team you would like to show: "))
            for team in teams:
                if team["id"] == team_id:
                    return (print(team))  
                elif team["id"] != team_id:
                    continue # ask user to enter the team id again


    def show_team_by_type():
        """Print team information using team type"""
        while True:
            team_type = input("Type of team to show (B/G): ").strip()
            if team_type.upper() == 'B':
                type = 'BOYS'
            elif team_type.upper() == 'G':
                type = 'GIRLS'
            else:
                type = None
                print('Please Enter a valid team type')
                
            for team in teams:
                if team["type"] == type:
                    return (print(team))
                else:
                    continue


    def show_all_teams():
        """Print all teams created by the user"""
        for team in teams:
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
        if new_type.upper() == 'B':
            type = 'BOYS'
        elif new_type.upper() == 'G':
            type = 'GIRLS'
        else:
            type = None
            print('Please Enter a valid team type')
        for team in teams:
            if team['id'] == team_id:
                team['type'] = type         
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
        
    def delete_team():
        '''Delete a team from the list of teams based on the id'''
        global teams 
        team_id = int(input("Enter ID of the team you want to delete:"))
        # remove dictionary(team) from list of dictionaries(teams) 
        # by slicing and list comprehension
        teams[:] = [team for team in teams if team.get('id') != team_id]
        return teams
            
    def display_main_menu():
        print('\t MENU ')
        print('1) Create a new team ')
        print('2) Show a team using ID ')
        print('3) Show a team using type ')
        print('4) Show all teams ')
        print('5) Update team ')
        print('6) Delete team ')
        print('7) Save Data')
        print('8) Read Data')
        print('0) Quit Program ')
        
    def display_update_submenu():
        print('\t UPDATE SUB MENU')
        print('51) Update Team Name')
        print('52) Update Team Type')
        print('53) Update Team Fee Status')
        
    def save_data():
        with open('data.txt', 'a+') as f:
            # write each teams to aaon a new line
            for team in teams:
                f.write(json.dumps(team, indent= 4))
                

            
            
    def read_data():
        global teams
        n = []
        with open('data.txt', 'r') as f:
            f = f.read()
            for team in f:
                teams.append(json.loads(team)  )          
        return teams
    
    
        
    