# Import the Pet class from the pet script file

from pet import Pet


def main():

    # Ask user the number of pets to be created
    total = int(input("Number of pets to create: "))
    
    # a list of all pets created
    pets = create_pet(total)
    
    # Give the user option to display all pets or only a certain type of pets
    display = input("Display all pets (Yes/No): ").lower()


# create a function that takes in the total number of pets to be
# created as an argument and returns objects representing pets


def create_pet(num):
    # initialize a list to store each pet created
    pets = []
    
    # create a pet object for each iteration
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
for i in range(2):
    name = input("Name of the pet: ")
    type = input("Type of the pet: ")
    age = input("Age of the pet: ")
    name =  (Pet(name, type, age))
    animals.append(name)    
    
for i in animals:
    if i.get_animal_type() == 'cat':
        print(i)

'''