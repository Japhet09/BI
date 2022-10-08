# Import the Pet class from the pet script file

from pet import Pet


def main():

    # Ask user the number of pets to be created
    total = int(input("Number of pets to create: "))
    
    # a list of all pets created
    pets_list = create_pet(total)
    
    #display the pets (all or certain type)
    
    display_pets(pets_list)
    
     


# A function that takes in the  number of pets to be created
# as an argument and returns a list of objects representing pets


def create_pet(num):
    # initialize a list to store each pet created
    pets = []
    
    # create a pet object for each iteration and add it to the list 
    for i in range(num):
        name = input("Name of the pet: ")
        type = input("Type of the pet: ")
        age = input("Age of the pet: ")
        pets.append(Pet(name, type, age))
        
    cat = Pet('kittie', 'cat', 4)
    dog = Pet('doggie', 'dog', 2)
    bird = Pet('bird', 'bird', 2)
    cute = Pet('cute', 'cat', 6)
    simba = Pet('simba', 'dog', 1)

    pets.append(cat)  
    pets.append(dog)
    pets.append(bird)
    pets.append(cute)
    pets.append(simba)

    return pets

# A function that takes a list of pets and displays all of them or a specific type 
# depending on the user preferences.

def display_pets(pets):
    # Give the user option to display all pets or only a certain type of pets
    display_all = input("Display all pets (Yes/No): ").lower()
    
    if display_all == "yes":
        for i in pets:
            print(i)
    else:
        pet_type = input("Type of pet to display: ").lower()
        for i in pets:
            if i.get_animal_type() == pet_type:
                print(i)
    

if __name__ == "__main__":
    main()
    
    