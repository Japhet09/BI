# Car class
class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year
    
    def __str__(self):
        return 'Car status\n' + 'MAKE: ' + self.__make + '\n' + 'MODEL: ' + self.__model + '\n' + 'YEAR: ' + self.__year
