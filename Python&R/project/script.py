# import menu to be able to use all
# the functions in the menu script
# import sys to use it to exit the program
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
TOTAL_TEAMS = 9
CANCEL_PARTICIPATION = 10
QUIT_CHOICE = 0

# constants for the SUB MENU FOR UPDATE_TEAMS
UPDATE_NAME = 51
UPDATE_TYPE = 52
UPDATE_FEES = 53


def main():

    while True:
        # DISPLAY THE MENU
        Menu.display_main_menu()
        try:
            # get the user choice
            choice = int(input("Enter choice from main menu: "))
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
            elif choice == TOTAL_TEAMS:
                Menu.count_teams()
            elif choice == CANCEL_PARTICIPATION:
                Menu.participation()
            elif choice == UPDATE_TEAMS:
                # display update sub menu
                Menu.display_update_submenu()
                choice = int(input("Enter Field to update: "))
                if choice == UPDATE_NAME:
                    Menu.update_name()
                elif choice == UPDATE_TYPE:
                    Menu.update_type()
                elif choice == UPDATE_FEES:
                    Menu.update_fees()
                else:
                    print("You can only update team name/type/fee_status")
            else:
                print("Error: Invalid choice, use the menu")
                continue
        except:
            print("Choice should be an integer")
            continue


if __name__ == "__main__":
    main()
