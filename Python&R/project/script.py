# import menu to be able to use all
# the functions in the menu script
# import sys to use it to exit the program
from os import read
import sys
from menu import Menu

# constants for the menu items
CREATE = 1
SHOW_BY_ID = 2
SHOW_BY_TYPE = 3
SHOW_ALL_TEAMS = 4
UPDATE_TEAMS = 5
DELETE_TEAM = 6
SAVE_DATA = 7
READ_DATA = 8
QUIT_CHOICE = 0

# constants for the SUB MENU FOR UPDATE_TEAMS
UPDATE_NAME = 51
UPDATE_TYPE = 52
UPDATE_FEES = 53

def main():
    while True:
        #DISPLAY THE MENU
        Menu.display_main_menu()
        
        # get the user choice
        choice = int(input('Enter choice: '))
        if choice == CREATE:
            Menu.create_team()
        elif choice == SHOW_BY_ID:
            Menu.show_team_by_id()
        elif choice == SHOW_BY_TYPE:
            Menu.show_team_by_type()
        elif choice == SHOW_ALL_TEAMS:
            Menu.show_all_teams()
        elif choice == QUIT_CHOICE:
            sys.exit("Exiting the program")
        elif choice == SAVE_DATA:
            Menu.save_data()
        elif choice == READ_DATA:
            Menu.read_data()
        elif choice == DELETE_TEAM:
            Menu.delete_team()
        elif choice ==UPDATE_TEAMS:
            #display update sub menu
            Menu.display_update_submenu()
            choice = int(input('Enter Fiels to update'))
            if choice == UPDATE_NAME:
                Menu.update_name()
            elif choice == UPDATE_TYPE:
                Menu.update_type()
            elif choice == UPDATE_FEES:
                Menu.update_fees()
        else:
            print("Error: Invalid choice" )
            
if __name__ == "__main__":
    main()
        