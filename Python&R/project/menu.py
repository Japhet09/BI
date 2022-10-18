# This program
from team import Team


def main():
    # print(create_team())
    t = Team("simba", "Boys", True, 99)
    t2 = Team("quenss", "girls", False, 0)
    t3 = Team("luton", "Boys", True, 990)
    t4 = Team("jkt", "Boys", True, 990)
    t5 = Team("atleti", "Boys", True, 990)
    t6 = Team("crown", "girls", True, 99)
    teams_list = [t, t2, t3, t4, t5, t6]
    
    update_team(teams_list)
    
    show_all_teams(teams_list)


def create_team():
    """Return a new team an instance from the Team class"""

    # Get the name, type , fee status and fee amount from the user
    name = input("Name of the team: ").strip()
    type = input("Type of team: ").strip()
    fee_paid = bool(input("Fee paid (True/False): ").strip())
    fee_amount = int(input("Fee amount: "))

    # create and return the team object
    return Team(name, type, fee_paid, fee_amount)



            
            
        
    
    
    
if __name__ == "__main__":
    main()
