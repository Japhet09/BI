class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    @property
    def make(self):
        return self.__make

    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year

    @make.setter
    def make(self, make):
        self.__make = make

    @model.setter
    def model(self, model):
        self.__model = model

    @year.setter
    def year(self, year):
        self.__year = year

    def __str__(self):
        return f"Car Status:\n MAKE: {self.__make} \n MODEL: {self.__model} \n YEAR: {self.__year}"


my_car = Car("Toyota", "RAV4", "2015")
print(my_car)
