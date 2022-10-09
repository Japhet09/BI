# Lab 3 Report

A summary of my thought process while working on the lab 3 assignment.

## Exercise 1: Personal Information Class
In this exercise, I created a person class by initializing `__init__` method that creates the class data attributes.
This is followed by accessor methods to retrieve the data attributes and mutator methods to assign values or change the data attributes. I then created a `__str__` method that represents the class as a string to be able to print the instances of the class.
Finally, I created three instance variables using the class constructor.
This exercise was easy since it was similar to the car class we created in the lecture.

## Exercise 2: Pet Class
Similar to the person class, creating a pet class was also straightforward. I initialized the pet class with the `__init__` method followed by the mutator and accessor methods and then the `__str__` method. I created a separate script and imported the pet class which I then used to create the objects.
The second part of the exercise was a little bit challenging especially on how to store the objects in a list. I initially was not able to display what is in the list until I added the `__str__` method in the pet class.
Also, It was challenging to figure out how to display only a certain type of pet. I finally found that I can compare the user input to the accessor method in the pet class (in this case the `get_animal_type` method)

Overall, classes construction was straightforward for both exercises and the challenging part was storing the objects in a list and displaying them depending on the user input.