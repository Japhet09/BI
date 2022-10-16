#import datetime module to get the date
import datetime

"""Team class definition."""


class Team:
    """Team class for registering and administrating handball  teams."""

    #
    def __init__(self, name, type, fee_paid, fee_amount):
        """Initialize the team object"""

        # use the datettime timestamp as a unique identifier
        self.__id = 1  # private attribute
        self.__date = datetime.datetime.now()  # private attribute
        self.name = name
        self.type = type
        self.fee_paid = fee_paid
        self.fee_amount = fee_amount

    # accessor methods for  the attributes (getter)
    @property
    def id(self):  # Read only method (will not have a correspomding mutator method/setter)
        '''Return the id of the team'''
        return self.__id

    @property
    def date(self):  # Read only method (will not have a corresponding mutator/setter)
        '''Return the date the team was created'''
        return self.__date

    @property
    def name(self):
        '''Return the name of the team'''
        return self.name
    
    @name.setter
    def name(self, name):
        '''Set the name of the team'''
        # Check if name is an instance of class string
        # if name is not a string, raise a Value error
        a_string = isinstance(name, str)
        if not a_string:
            raise ValueError("Name must be a string")
        self._name = name

    @property
    def type(self):
        '''Return the type of the team'''
        return self.type
    
    @type.setter
    def type(self, type):
        '''Set the type of the team'''
        # team type can only be boys or girls
        team_type = ["boys", "girls"]
        if type.lower() not in team_type:
            raise ValueError("Invalid team type: can only be boys/girls" )
        self.type = type

    @property
    def fee_paid(self):
        '''Return the status of the fee if paid or not'''
        return self.fee_paid
    
    @fee_paid.setter
    def fee_paid(self,fee_paid):
        '''Set the status of the fee if paid or not'''
        # chekc if fee_paid is of class boolean
        # if fee_paid is not of class boolean, then raise a value error
        a_bool = isinstance(fee_paid, bool)
        if not a_bool:
            raise ValueError('fee_paid must be a boolean True/False')
        self.fee_paid = fee_paid

    @property
    def fee_amount(self):
        '''Returns the amount of the fee paid'''
        return self.fee_amount
        
    @fee_amount.setter
    def fee_amount(self,fee_amount):
        '''Set the amount of the fee paid'''
        an_int = isinstance(fee_amount, int)
        if not an_int:
            raise ValueError('fee_amount must be an integer')
        self.fee_amount = fee_amount
        
    def __str__(self):
        return f'ID: {self.__id} Date: {self.__date} Name: {self.name} Fee Paid: {self.fee_paid} Fee Amount: {self.fee_amount}'
        
team = Team('simba', 'Boys', True, 500)
print(team)