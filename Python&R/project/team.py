# import datetime module to get the date
import datetime

"""Team class definition."""


class Team:
    """Team class for registering and administrating handball  teams."""

    # A class attribute that will be used to increment the id attribute for each object created
    counter = 1

    def __init__(self, name, type, fee_paid, fee_amount = 99):
        """
        Initialize the team object
        """
        # use the class counter variable to initialize the id attribute
        self.__id = Team.counter  # private attribute
        Team.counter += 1  # increment the class variable for the next object creation
        self.__date = datetime.date.today()  # private attribute
        self.name = name
        self.type = type
        self.fee_paid = fee_paid
        self.fee_amount = fee_amount

    # Read only method for the id
    @property
    def id(self):
        """Return the id of the team"""
        return self.__id

    # Read only method for the date
    @property
    def date(self):
        """Return the date the team was created"""
        return self.__date

    # accessor method for getting the name of the team
    @property
    def name(self):
        """Return the name of the team"""
        return self._name

    # mutator method for setting the name of the team
    @name.setter
    def name(self, name):
        """Set the name of the team"""
        self._name = name.title()

    # accessor method for getting the type of the team
    @property
    def type(self):
        """Return the type of the team"""
        return self._type

    # Mutator method for setting the type of the team
    @type.setter
    def type(self, type):
        """Set the type of the team"""
        # team type can only be boys or girls
        if type.lower() in ['b', 'boys','boy']:
            self._type = "Boys"
        elif type.lower() in ['g','girls','girl']:
            self._type = "Girls"
        else:
            raise ValueError("Invalid team type ")

    # accessor method for getting the fee status
    @property
    def fee_paid(self):
        """Return the status of the fee if paid or not"""
        return self._fee_paid

    # mutator method for setting the fee status
    @fee_paid.setter
    def fee_paid(self, fee_paid):
        """Set the status of the fee if paid or not"""
        # Fee is paid True(Y) or False (N)
        if fee_paid.lower() in ['y', 'yes', 'true']:
            self._fee_paid = True
        elif fee_paid.lower() in ['n', 'no', 'false']:
            self._fee_paid = False
        else:
            raise ValueError("Enter Yes or No")

    # accessor method for getting the fee amount
    @property
    def fee_amount(self):
        """Returns the amount of the fee paid"""
        return self._fee_amount

    # mutator method for setting the fee amount
    @fee_amount.setter
    def fee_amount(self, fee_amount):
        """
        Set the amount of the fee paid
        depending on the fee status
        """
        # If fee is paid, set fee_amount to default value(99)
        if self._fee_paid == True:
            self._fee_amount = fee_amount
        else:
            self._fee_amount = 0

    def __str__(self):
        return (f"Team Info\n"
        f"ID: {self.__id}\n"
        f"Date: {self.__date}\n"
        f"Name: {self._name}\n"
        f"Type: {self._type}\n"
        f"Fee Paid: {self._fee_paid}\n"
        f"Fee Amount: {self._fee_amount}\n")
'''
t = Team('Simba', 'B', 'Y')
t2 = Team('Young', 'g', 'n')

#t.update_type('yeye')
#print(t,t2)

print(t.date)
'''