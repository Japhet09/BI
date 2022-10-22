# =====================================================================
# This script contains a Menu class with methods  to create, show,
# update  and delete teams as well as methods to save the data to a txt
# file and read it from the text file
# =====================================================================
# import team class
from team import Team

# All teams created will be stored in the variable teams
# we use a global variable to allow all methods to have access to it
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

        # Create and ppend the team to the list of teams
        teams.append(Team(name, type, fee_paid))
        return teams


    def show_team_by_id():
        """Print team information using the team id"""
        while True:
            team_id = int(input("Id of team you would like to show: "))
            for t in teams:
                if t.id == team_id:
                    return (print(t))
                else:
                    continue # ask user to enter the team id again


    def show_team_by_type():
        """Print team information using team type"""
        while True:
            team_type = input("Type of team to show (B/G): ").strip()
            for t in teams:
                if t.type == team_type:
                    return (print(t))
                else:
                    continue


    def show_all_teams():
        """Print all teams created by the user"""
        for t in teams:
            print(t)


    def update_name():
        '''Update the team name based on the team id'''
        global teams
        team_id = int(input("Enter team id to update: "))
        new_name = input("New Team Name")
        for t in teams:
            if t.id == team_id:
                t.name = new_name
        return teams

    def update_type():
        '''Update the type of the team'''
        global teams
        team_id = int(input("Enter team id to update: "))
        new_type = input("New Team type")
        for t in teams:
            if t.id == team_id:
                t.type = new_type
        return teams

    def update_fees():
        '''Update the fee status and fee amount '''
        global teams
        team_id = int(input("Enter team id to update: "))
        new_fee_paid = input("New Fee status (Y/N): ")
        for t in teams:
            if t.id == team_id:
                t.fee_paid = new_fee_paid
        return teams

    def delete_team():
        '''Delete a team from the list of teams based on the id'''
        global teams
        team_id = int(input("Enter ID of the team you want to delete:"))
        # remove team from the list
        for t in teams:
            if t.id == team_id:
                teams.remove(t)
        return teams

    def save_data():
        '''Write each object to a file as a string'''
        outfile = open('my_teams.txt', 'w')
        for t in teams:
            t_txt = f"{t.id}, {t.date}, {t.name}, {t.type}, {t.fee_paid}, {t.fee_amount}"
            outfile.write(t_txt + '\n')
        outfile.close()

    def read_data():
        ''' Read the data from the txt file and create
        objects using that data'''
        infile = open('my_teams.txt', 'r')
        t_temp_list = infile.readlines()
        infile.close()
        global teams
        teams.clear()
        for i in t_temp_list:
            t = i.rstrip('\n')
            t = t.split(',')
            teams.append(Team(t[2].strip(), t[3].strip(), t[4].strip()))






    def display_main_menu():
        print('\tMAIN MENU ')
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
        print('\tUPDATE SUB MENU')
        print('51) Update Team Name')
        print('52) Update Team Type')
        print('53) Update Team Fee Status')


def main():
    pass
    #Menu.read_data()

main()