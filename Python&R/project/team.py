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
        now = datetime.datetime.now()
        self.__date = now.strftime('%Y/%m/%d') # private attribute
        self.name = name
        self.type = type
        self.fee_paid = fee_paid
        self.fee_amount = fee_amount

    # accessor methods for  the attributes (getter)

    # Read only method for the id(will not have a correspomding mutator method/setter)

    def get_id(self):
        """Return the id of the team"""
        print("getting id")
        return self.__id

    # Read only method for the date(will not have a correspomding mutator method/setter)

    def get_date(self):
        """Return the date the team was created"""
        print("getting date")
        return self.__date

    # accessor method for getting the name of the team
    def get_name(self):
        """Return the name of the team"""
        print("getting name")
        return self.name

    # mutator method for setting the name of the team
    def set_name(self, name):
        """Set the name of the team"""
        print("setting name")

        # if name is not a string, raise a Value error

        if type(name) == str:
            self.name = name.upper()
        else:
            raise ValueError("Name must be a string")

    # accessor method for getting the type of the team
    def get_type(self):
        """Return the type of the team"""
        print("getting types")
        return self.type

    # Mutator method for setting the type of the team
    def set_type(self, type):
        """Set the type of the team"""
        print("setting type")
        # team type can only be boys or girls
        if type.upper() in ["BOYS", "GIRLS"]:
            self.type = type.upper()
        else:
            raise ValueError("Invalid team type: can only be boys/girls")

    # accessor method for getting the fee status
    def get_fee_paid(self):
        """Return the status of the fee if paid or not"""
        print("getting fee paid")
        return self.fee_paid

    # mutator method for setting the fee status
    def set_fee_paid(self, fee_paid):
        """Set the status of the fee if paid or not"""
        print("setting fee paid")
        # chekc if fee_paid is of class boolean
        # if fee_paid is not of class boolean, then raise a value error
        if type(fee_paid) == bool:
            self.fee_paid = fee_paid
        else:
            raise ValueError("fee_paid must be a boolean True/False")

    # accessor method for getting the fee amount
    def get_fee_amount(self):
        """Returns the amount of the fee paid"""
        print("getting fee_amount")
        return self.fee_amount

    # mutator method for setting the fee amount
    def set_fee_amount(self, fee_amount):
        """Set the amount of the fee paid"""
        print("setting fee_amount")
        # if fee_amount is not an integer raise ValueError
        if type(fee_amount) == int:
            self.fee_amount = fee_amount
        else:
            raise ValueError("fee_amount must be an integer")
        
    # A method to to store the team information as a dictionary
    def store_data(self):
        return {
            "id": self.__id,
            "date": self.__date,
            "name": self.name,
            "type": self.type,
            "fee": self.fee_paid,
            "fee_amount": self.fee_amount,
        }
        
    # A method to show the string representation of the team object
    def __str__(self):
        return f"ID: {self.__id}, Date: {self.__date}, Name: {self.name}, Type: {self.type}, Fee Paid: {self.fee_paid}, Fee Amount: {self.fee_amount}"

''' 
t = Team("simba", "Boys", True, 99)
t2 = Team("quenss", "girls", False, 0)
t3 = Team("luton", "Boys", True, 990)
t4 = Team("jkt", "Boys", True, 990)
t5 = Team("atleti", "Boys", True, 990)
t6 = Team("crown", "girls", True, 100)

lst = [t, t2, t3, t4, t5, t6]
c = []

for t in lst:
    c.append(t.store_data())
print(c)

'''