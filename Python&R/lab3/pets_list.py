# Import the Pet class from the pet script file

from pet import Pet

'''
def main():

    # Ask user the number of pets to be created
    total = int(input("Number of pets to create: "))
    animals = create_pet(total)


# create a function that takes in the total number of pets to be
# created as an argument and returns objects representing pets


def create_pet(num):
    # initialize a variable to store each pet created
    pets = []
    #  using range function, loop through the number of pets
    # creating a pet object for each iteration
    for i in range(num):
        name = input("Name of the pet: ")
        type = input("Type of the pet: ")
        age = input("Age of the pet: ")
        pets.append(Pet(name, type, age))

    return pets


if __name__ == "__main__":
    main()
    
    '''
animals = [] 
for i in range(1):
    name = input("Name of the pet: ")
    type = input("Type of the pet: ")
    age = input("Age of the pet: ")
    name =  (Pet(name, type, age))
    animals.append(name)    
    
for i in animals:
    if i.get_animal_type() == 'cat':
        print(i)

