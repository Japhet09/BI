# Person class


class Person:
    # Initialize the class attributes
    def __init__(self, name, address, age, phone):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone

    # Create the accessor methods
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone(self):
        return self.__phone

    # Create mututor methods
    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_phone(self, phone):
        self.__phone = phone
        
    # A string method to display the object
    def __str__(self):
        return f'Personal Info: \n Name: {self.__name} \n Address: {self.__address} \n Age: {self.__age} \n Phone: {self.__phone}'

# class instances
my_info = Person('Japhet Alfred', 'Gävle, Sweden', 31, '0709337991')
nelson = Person('Nelson Amani', 'Uppsala, Sweden', 21, '070471490')
john = Person('John Doe', 'Gamla stan, Uppsala', 24, '0702819342')