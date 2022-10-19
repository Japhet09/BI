# import datetime module to get the date
import datetime

"""Team class definition."""


class Team:
    """Team class for registering and administrating handball  teams."""

    # A class attribute that will be used to increment the id attribute for each object created
    counter = 1

    def __init__(self, name, type, fee_paid):
        """Initialize the team object"""

        # use the class counter variable to initialize the id attribute
        self.__id = Team.counter  # private attribute
        Team.counter += 1  # increment the class variable
        now = datetime.datetime.now()
        self.__date = now.strftime("%Y/%m/%d")  # private attribute
        self.name = name
        self.type = type
        self.fee_paid = fee_paid
        self.fee_amount = 99

    # accessor methods for  the attributes (getter)

    # Read only method for the id(will not have a correspomding mutator method/setter)
    
    @property
    def id(self):
        """Return the id of the team"""
        print("getting id")
        return self.__id

    # Read only method for the date(will not have a correspomding mutator method/setter)
    
    @property
    def date(self):
        """Return the date the team was created"""
        print("getting date")
        return self.__date

    # accessor method for getting the name of the team
    @property
    def name(self):
        """Return the name of the team"""
        print("getting name")
        return self._name

    # mutator method for setting the name of the team
    @name.setter
    def name(self, name):
        """Set the name of the team"""
        print("setting name")

        # if name is not a string, raise a Value error
        if type(name) == str:
            self._name = name.upper()
        else:
            raise ValueError("Name must be a string")

    # accessor method for getting the type of the team
    @property
    def type(self):
        """Return the type of the team"""
        print("getting types")
        return self._type

    # Mutator method for setting the type of the team
    @type.setter
    def type(self, type):
        """Set the type of the team"""
        print("setting type")
        # team type can only be boys or girls
        if type.upper() == "B":
            self._type = "BOYS"
        elif type.upper() == "G":
            self._type = "GIRLS"
        else:
            raise ValueError("Invalid team type: Enter B or G")

    # accessor method for getting the fee status
    @property
    def fee_paid(self):
        """Return the status of the fee if paid or not"""
        print("getting fee paid")
        return self._fee_paid

    # mutator method for setting the fee status
    @fee_paid.setter
    def fee_paid(self, fee_paid):
        """Set the status of the fee if paid or not"""
        print("setting fee paid")
        # Fee is paid (Yes) or not (No)
        if fee_paid.upper() == "Y":
            self._fee_paid = True
        elif fee_paid.upper() == "N":
            self._fee_paid = False
        else:
            raise ValueError("Enter Y or N")

    # accessor method for getting the fee amount
    @property
    def fee_amount(self):
        """Returns the amount of the fee paid"""
        print("getting fee_amount")
        return self._fee_amount

    # mutator method for setting the fee amount
    @fee_amount.setter
    def fee_amount(self, fee_amount):
        """Set the amount of the fee paid"""
        print("setting fee_amount")
        # if fee_amount is not an integer raise ValueError
        if type(fee_amount) == int:
            if self._fee_paid == True:
                self._fee_amount = fee_amount
            else:
                self._fee_amount = 0
        else:
            raise ValueError("Amount must be an integer")

    # A method to to store the team information as a dictionary
    def store_data(self):
        return {
            "id": self.__id,
            "date": self.__date,
            "name": self._name,
            "type": self._type,
            "fee": self._fee_paid,
            "fee_amount": self._fee_amount,
        }

    # A method to show the string representation of the team object
    def __str__(self):
        return f"ID: {self.__id}, Date: {self.__date}, Name: {self._name}, Type: {self._type}, Fee Paid: {self._fee_paid}, Fee Amount: {self._fee_amount}"


t = Team('simba', "B", 'Y')
t2 = Team("quenss", "g", 'Y')
t3 = Team("luton", "B", 'Y')
t4 = Team("jkt", "B", 'N')
t5 = Team("atleti", "B", 'N')
t6 = Team("crown", "g", 'Y')

lst = [t, t2, t3, t4, t5, t6]
c = []

for t in lst:
    c.append(t.store_data())
print(c)
