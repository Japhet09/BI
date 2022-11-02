# =========================================================================
# This program contains an Interface class with methods  to create, show,
# update  and delete teams as well as methods to save the data to a txt
# file and read it from the text file. It imports the Team class from the
# team.py file
# ========================================================================
# import Team class
from team import Team


class Interface:
    """Interface class for creating, updating, displaying and deleting teams"""

    # A class variable to store all the teams created
    teams = []

    # CREATE TEAMS
    def create_team():
        """Returns a list of instances from the Team class"""

        # Get the name, type , fee status  from the user and remove whitespaces
        name = input("Name of the team: ").strip()
        type = input("Type of team (Boys/Girls): ").strip()
        fee_paid = input("Fee paid (Yes/No: ").strip()

        # Create and append the team to the list of teams(class variable)
        Interface.teams.append(Team(name, type, fee_paid))
        return Interface.teams

    # DISPLAY TEAM USING ID
    def show_team_by_id():
        """Display team information using the team id"""
        try:
            team_id = int(input("ID of team you would like to show: "))
            for t in Interface.teams:
                if t.id == team_id:
                    print(t)
        except ValueError:
            print("Team ID should be an integer")

    # DISPLAY TEAMS BY TYPE
    def show_team_by_type():
        """Display team information by type"""
        try:
            team_type = input("Type of team to show (Boys/Girls): ").title()
            for t in Interface.teams:
                if t.type == team_type:
                    print(t)
        except:
            print("Team type should be Boys/Girls")

    # DISPLAY ALL TEAMS
    def show_all_teams():
        """Print all teams created by the user"""
        # Loop through the teams list and print them
        for t in Interface.teams:
            print(t)

    # UPDATE TEAM NAME
    def update_name():
        """Update the team name based on the team id"""
        try:
            team_id = int(input("Enter id of team to update: "))
            new_name = input("New Team Name: ")
            for t in Interface.teams:
                if t.id == team_id:
                    t.name = new_name
            return Interface.teams
        except ValueError:
            print("Team ID should be an integer")

    # UPDATE TEAM TYPE
    def update_type():
        """Update the type of the team"""
        try:
            team_id = int(input("Enter id of team to update: "))
            new_type = input("New Team type: ")
            for t in Interface.teams:
                if t.id == team_id:
                    t.type = new_type
            return Interface.teams
        except ValueError:
            print("Enter valid ID")

    # UPDATE TEAM FEE STATUS
    def update_fees():
        """Update the fee status and fee amount"""
        try:
            team_id = int(input("Enter id of team to update: "))
            new_fee_paid = input("New Fee status (Yes/No): ")
            new_fee_amount = int(input("New Fee amount: "))
            for t in Interface.teams:
                if t.id == team_id:
                    t.fee_paid = new_fee_paid
                    t.fee_amount = new_fee_amount
            return Interface.teams
        except ValueError:
            print("Team ID/ Fee amount should be an integer")

    # DELETE TEAM FROM LIST
    def delete_team():
        """Delete a team from the list of teams based on the id"""
        try:
            team_id = int(input("Enter ID of the team you want to delete: "))
            # remove team from the list
            for t in Interface.teams:
                if t.id == team_id:
                    Interface.teams.remove(t)
            return Interface.teams
        except ValueError:
            print("Invalid team ID ")

    # SAVE ALL THE TEAM INFO IN A TEXT FILE
    def save_data():
        """Write each object to a file as a string"""
        with open("my_teams.txt", "w") as outfile:
            # assign each team object to a variable as a string
            for t in Interface.teams:
                t_txt = f"{t.id}, {t.date}, {t.name}, {t.type}, {t.fee_paid}, {t.fee_amount}, {t.cancel}"
                # write each team to the file in separate lines
                outfile.write(t_txt + "\n")

    # READ THE TEAM FROM A TEXT FILE THEN CREATE AND APPEND THEM TO A LIST AS OBJECTS
    def read_data():
        """Read the data from the txt file and create
        objects using that data"""
        with open("my_teams.txt", "r") as infile:
            # Read all the teams in each line in the file
            # and store them in a temporary list
            t_temp_list = infile.readlines()

            # Clear teams list to make sure its empty before adding data
            Interface.teams.clear()

            # since the data are stored as string in the temporary list
            # Remove the new line from each line in the temporary list
            # make each line a list by splitting the string

            for i in t_temp_list:
                t = i.rstrip("\n")
                t = t.split(",")
                # strip any whitespace from the data and create team and append to the teams list
                Interface.teams.append(
                    Team(
                        t[2].strip(),  # name
                        t[3].strip(),  # type
                        t[4].strip(),  # fee_paid
                        (t[5].strip()),  # amount
                        t[6].strip(),  # cancellation date
                    )
                )

    # TOTAL NUMBER OF TEAMS AND THE PERCENTAGE OF TEAMS WHICH HAVE PAID THE FEE
    def count_teams():
        print(f"Total Number of teams: {len(Interface.teams)}")
        try:
            paid = 0
            total_fees = 0

            for t in Interface.teams:
                if t.fee_paid == True:
                    paid += 1
                    total_fees += int(t.fee_amount)
            print(
                f"Percent of all teams which have paid the fee: {paid/len(Interface.teams):.1%}"
            )
            print(f"Total Amount of Fees Paid: {total_fees}$")

        except ZeroDivisionError:
            print("Please make sure there are teams in the list")

    # CANCEL TEAM PARTCIPATION BY ADDING A CANCELLATION DATE TO THE OBJECT(TEAM)
    def participation():
        team_id = int(input("ID of team which cancelled: "))
        cancel = input("Enter the date of cancellation (YYYY-MM-DD): ")
        for t in Interface.teams:
            if t.id == team_id:
                t.cancel = cancel

    # DISPLAY THE PROGRAM MAIN MENU
    def display_main_menu():
        print("---------------------------")
        print("\tMAIN MENU ")
        print("---------------------------")
        print("1) Create a new team ")
        print("2) Show a team using ID ")
        print("3) Show a team by type ")
        print("4) Show all teams ")
        print("5) Update team ")
        print("6) Delete team ")
        print("7) Save Data")
        print("8) Read Data")
        print("9) Total number of teams ")
        print("10) Cancel Participation ")
        print("---------------------------")
        print()

    # DISPLAY A SUB MENU WHEN UPDATING TEAM INFO
    def display_update_submenu():
        print()
        print("\tUPDATE SUB-MENU")
        print("---------------------------")
        print("51) Update Team Name")
        print("52) Update Team Type")
        print("53) Update Team Fee Status")
        print("---------------------------")
        print()
