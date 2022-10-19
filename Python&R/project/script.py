# import menu to be able to use all
# the functions in the menu script
# import sys to use it to exit the program
import sys
import menu

# constants for the menu items
CREATE = 1
SHOW_BY_ID = 2
SHOW_BY_TYPE = 3
SHOW_ALL_TEAMS = 4
UPDATE_TEAMS = 5
DELETE_TEAM = 6
QUIT_CHOICE = 0

teams = menu.teams
print(teams)


# constants for the SUB MENU FOR UPDATE_TEAMS
UPDATE_NAME = 51
UPDATE_TYPE = 52
UPDATE_FEES = 53

def main():
    while True:
        #DISPLAY THE MENU
        menu.display_main_menu()
        
        # get the user choice
        choice = int(input('Enter choice: '))
        if choice == CREATE:
            menu.create_team()
        elif choice == SHOW_BY_ID:
            menu.show_team_by_id(teams)
        elif choice == SHOW_BY_TYPE:
            menu.show_team_by_type(teams)
        elif choice == SHOW_ALL_TEAMS:
            menu.show_all_teams(teams)
        elif choice == QUIT_CHOICE:
            sys.exit("Exiting the program")
        elif choice == DELETE_TEAM:
            menu.delete_team()
        elif choice ==UPDATE_TEAMS:
            #display update sub menu
            menu.display_update_submenu()
            choice = int(input('Enter Fiels to update'))
            if choice == UPDATE_NAME:
                menu.update_name()
            elif choice == UPDATE_TYPE:
                menu.update_type()
            elif choice == UPDATE_FEES:
                menu.update_fees()
        else:
            print("Error: Invalid choice" )
            
if __name__ == "__main__":
    main()
        