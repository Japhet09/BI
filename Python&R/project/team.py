# import datetime module to get the date
import datetime

"""Team class definition."""


class Team:
    """Team class for registering and administrating handball  teams."""

    # A class attribute that will be used to increment the id attribute for each object created
    counter = 1

    def __init__(self, name, type, fee_paid, fee_amount):
        """Initialize the team object"""

        # use the class counter variable to initialize the id attribute
        self.__id = Team.counter  # private attribute
        Team.counter += 1  # increment the class variable
        self.__date = datetime.datetime.now()  # private attribute
        self.name = name
        self.type = type
        self.fee_paid = fee_paid
        self.fee_amount = fee_amount

    # accessor methods for  the attributes (getter)

    # Read only method (will not have a correspomding mutator method/setter)
    @property
    def id(self):
        """Return the id of the team"""
        print('getting id')
        return self.__id

    # Read only method (will not have a correspomding mutator method/setter)
    @property
    def date(self):
        """Return the date the team was created"""
        print('getting date')
        return self.__date
    @property
    def name(self):
        """Return the name of the team"""
        print('getting name')
        return self._name
    
    @name.setter
    def name(self, name):
        """Set the name of the team"""
        print('setting name')
        
        # Check if name is an instance of class string
        # if name is not a string, raise a Value error
       
        if type(name) == str:
            self._name = name
        else:
            raise ValueError("Name must be a string")
        
    @property
    def type(self):
        """Return the type of the team"""
        print('getting types')
        return self._type
    
    @type.setter
    def type(self, type):
        """Set the type of the team"""
        print('setting type')
        # team type can only be boys or girls
        if type.lower() in ["boys", "girls"]:
            self._type = type
        else:
            raise ValueError("Invalid team type: can only be boys/girls")
        
    @property
    def fee_paid(self):
        """Return the status of the fee if paid or not"""
        print('getting fee paid')
        return self._fee_paid
    
    @fee_paid.setter
    def fee_paid(self, fee_paid):
        """Set the status of the fee if paid or not"""
        print('setting fee paid')
        # chekc if fee_paid is of class boolean
        # if fee_paid is not of class boolean, then raise a value error
        if type(fee_paid) == bool:
            self._fee_paid = fee_paid
        else:
            raise ValueError("fee_paid must be a boolean True/False")
    @property
    def fee_amount(self):
        """Returns the amount of the fee paid"""
        print('getting fee_amount')
        return self._fee_amount
    
    @fee_amount.setter
    def fee_amount(self, fee_amount):
        """Set the amount of the fee paid"""
        print('setting fee_amount')
        if  type(fee_amount) == int:
            self._fee_amount = fee_amount
        else:
            raise ValueError("fee_amount must be an integer")

    def __str__(self):
        return f"ID: {self.__id} Date: {self.__date} Name: {self._name} Fee Paid: {self._fee_paid} Fee Amount: {self._fee_amount}"


t = Team('simba', 'boys',True, 5)
print(t)