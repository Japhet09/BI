# The Team class will be imported into the interface program
# import datetime module to get the date
import datetime

"""Team class definition."""


class Team:
    """Team class for registering and administrating handball  teams."""

    # A class attribute that will be used to increment the id attribute for each object created
    counter = 1

    def __init__(self, name, type, fee_paid, fee_amount=99, cancel=None):
        """Initialize the team object"""
        # use the class counter variable to initialize the id attribute
        self.__id = Team.counter  # private attribute
        Team.counter += 1  # increment the class variable for the next object creation
        self.__date = datetime.date.today()  # private attribute
        self.name = name
        self.type = type
        self.fee_paid = fee_paid
        self.fee_amount = fee_amount
        self.cancel = cancel

    # All the accessor methods for the class data attributes
    @property
    def id(self):
        """Return the id of the team"""
        return self.__id

    @property
    def date(self):
        """Return the date the team was created"""
        return self.__date

    @property
    def name(self):
        """Return the name of the team"""
        return self._name

    @property
    def type(self):
        """Return the type of the team"""
        return self._type

    @property
    def fee_paid(self):
        """Return the status of the fee if paid or not"""
        return self._fee_paid

    @property
    def fee_amount(self):
        """Returns the amount of the fee paid"""
        return self._fee_amount

    @property
    def cancel(self):
        """Return the date the team canclled participating"""
        return self._cancel

    # Mutator methods for the  data attributes
    # The id and date attributes have no corresponding mutator methods
    # Since they are not supposed to be changed by the user ( Read Only)
    @name.setter
    def name(self, name):
        """Set the name of the team"""
        self._name = name.title()

    @type.setter
    def type(self, type):
        """Set the type of the team"""
        # team type can only be boys or girls
        if type.lower() in ["b", "boys", "boy"]:
            self._type = "Boys"
        elif type.lower() in ["g", "girls", "girl"]:
            self._type = "Girls"
        else:
            raise ValueError("Invalid team type ")

    @fee_paid.setter
    def fee_paid(self, fee_paid):
        """Set the status of the fee if paid or not"""
        # Fee is paid True(Y) or False (N)
        if fee_paid.lower() in ["y", "yes", "true"]:
            self._fee_paid = True
        elif fee_paid.lower() in ["n", "no", "false"]:
            self._fee_paid = False
        else:
            raise ValueError("Please Enter Yes or No")

    @fee_amount.setter
    def fee_amount(self, fee_amount):
        """Set the amount of the fee paid depending on the fee status"""
        # If fee is paid, set fee_amount to default value(99)
        if self._fee_paid:
            self._fee_amount = fee_amount
        else:
            self._fee_amount = 0

    @cancel.setter
    def cancel(self, cancel):
        try:
            # team which cancelled will have a cancellation date
            self._cancel = datetime.datetime.strptime(cancel, "%Y-%m-%d").date()
        except (TypeError, ValueError):
            # cancellation date will be none for participating team
            self._cancel = cancel

    # String representation of the object
    def __str__(self):
        return (
            f"Team Info\n"
            f"ID: {self.id}\n"
            f"Date: {self.date}\n"
            f"Name: {self.name}\n"
            f"Type: {self.type}\n"
            f"Fee Paid: {self.fee_paid}\n"
            f"Fee Amount: {self.fee_amount}$\n"
            f"Cancelled on : {self.cancel}\n"
        )
