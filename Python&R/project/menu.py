# This program
from team import Team

teams = [
        {
            "id": 1,
            "date": "2022/10/19",
            "name": "SIMBA",
            "type": "BOYS",
            "fee_paid": True,
            "fee_amount": 99,
        },
        {
            "id": 2,
            "date": "2022/10/19",
            "name": "YANGA",
            "type": "GIRLS",
            "fee_paid": True,
            "fee_amount": 99,
        },
        {
            "id": 3,
            "date": "2022/10/19",
            "name": "AZAM",
            "type": "BOYS",
            "fee_paid": True,
            "fee_amount": 99,
        },
    ]


def main():

    for i in range(3):
        create_team()
    print(teams)


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


def show_team(teams):
    """Print team information based on the team id"""
    team_id = int(input("Id of time you would like to show: "))
    for team in teams:
        if team["id"] == team_id:
            print(team)


def show_team_by_type(teams_list):
    """Print team based on type"""
    team_type = input("Type of team to show: ").strip()
    for team in teams_list:
        if team["type"] == team_type:
            print(team)


def show_all_teams(teams_list):
    """Print all teams created by the user"""
    for team in teams_list:
        print(team)


def update_team():
    """Update the team name, type, fee status or fee amount"""
    team_id = int(input("Enter id of team to update: "))
    item = input("Field to update")
    new_value = input("New value: ")
    global teams
    for t in teams:
        if t["id"] == team_id:
            if t["name"] == item:
                t["name"] = new_value
            elif t["type"] == item:
                t["type"] = new_value
            elif t["fee_paid"] == item:
                t["fee_paid"] = bool(new_value)
            elif t["fee_amount"] == item:
                t["fee_amount"] = int(new_value)
    return teams


if __name__ == "__main__":
    main()
