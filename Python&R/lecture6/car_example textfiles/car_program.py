import car_id
from utility_functions import clean_list as clean_list

# Three objects created from the class Car in 
# file myCarClassFile.py
c1 = car_id.Car("Skoda","Scout","2013")
c2 = car_id.Car("VW","Passat","1998")
c3 = car_id.Car("Volvo","V70","2007")

# A list is created and car-objects are 
# stored in it (temporary stored - cleared after program ends)
myCars = [c1,c2,c3]

# List of cars after file been read and 
# objects created from each line in the file 
# myCarsList = []

# =========================================================================
# WRITING DATA, EACH OBJECT CTREATED ABOVE, TO FILE IN 
# THE FORM OF STRINGS! (TEXT)
# =========================================================================
# Open a file named my_cars.txt.
outfile = open("my_cars.txt", "w")

for c in myCars:
   c_txt = c.get_make() + "," + c.get_model() + "," + c.get_year()
   outfile.write(c_txt +"\n")

outfile.close()

# =========================================================================
# OPEN A FILE FOR READING WITH DATA, about cars, STORED FROM I.E. AN EARLIER SESSION
# =========================================================================

# Open a file named my_cars.txt.
infile = open("my_cars.txt", "r")

# get content from file, returned as a list ! so the
# car_temp_list will automatically be referencing a new list
# returned from the method readlines() of the file object "infile"
car_temp_list = infile.readlines()

infile.close()

# =========================================================================
# AFTER FILE READING, A LIST EXIST WITH DATA, about cars, STORED AS STRINGS!
# =========================================================================
car_temp_list = clean_list(car_temp_list)
print(car_temp_list)

myCars.clear()

for each_position in car_temp_list : 
    tmp_list = each_position.rsplit(',')
    tmp_car_obj = car_id.Car(tmp_list[0],tmp_list[1],tmp_list[2])
    # Simple way of adding new objects to 
    # the end of the list by using method append()
    myCars.append(tmp_car_obj)


# printing each object's data
for x in myCars:
   print(x)


# ======================================================================
# CODE BELOW IS TO SHOW THAT NEW DATA IS BEING ADDED TO THE FILE
# AND ALSO WHAT HAPPENS WITH THE VALUE OF THE CLASS VARIABLE NAMED
# COUNTER IN THE CAR-CLASS
# ======================================================================

myCars.append(car_id.Car("Ford","GT","1985"))

# Open a file named my_cars.txt.
outfile = open("my_cars.txt", "w")

for c in myCars:
   c_txt = c.get_make() + "," + c.get_model() + "," + c.get_year()
   outfile.write(c_txt +"\n")

outfile.close()
