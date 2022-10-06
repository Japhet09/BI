# Class name
class Pet:
    # initialize the class 
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
        
    # methods to change the class attributes
    def set_name(self, name):
        self.__name = name
        
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type
    
    def set_age(self, age):
        self.__age = age
        
    # methods to access the class attributes
    def get_age(self):
        return self.__age
    
    def get_name(self):
        return self.__name
    
    def get_animal_type(self):
        return self.__animal_type
        
    # A string method
    def __str__(self):
        return f'Animal Info: \n Name: {self.__name} \n Type: {self.__animal_type} \n Age: {self.__age}'