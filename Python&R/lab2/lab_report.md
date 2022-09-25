# Lab 2 Report

A short summary of my thoughts process while working through the lab assignment.

## Exercise 1: DVD Club Points

In this exercise, I initialized two variables, one to get the user input, and another to store their earnings based on
the number of dvd bought. I then convert the user input into an integer.
Using conditional statements, I check the number of dvd boguht and then update the earnings respectively. I then use
f-string to print a message on the total points awarded to the user.

## Exercise 2: BMI

Since the weight and height can have decimal points, I convert them into float values. Using the formula, I calculate the index and round it to 2 decimal places using the round function. Same as above, I check the bmi if below or above certain values and display a message depending on its value.

## Exercise 3: Property Tax

First, I initiate a constant variable representing the percentage of the actual property that is used to get the assessment value. I also use a main function to call the property tax function and get the actual value from the user. Since the tax rate was per $100, I had challenges on how to use it to calculate the assessment value but Iwas able to figure it out in the end.

## Exercise 4: Sum of Numbers

In this exercise, I had options of either initializing the user input variable first and using it to control the loop, or initializing an infinite loop that I can break manually by checking the user input if its value is negative.

## Exercise 5:Maximum of Two Numbers

This exercise was more or less the same as the previous exercises. I created a main function to wrap the two variables and the function. I then conditionals in the my_max function to compare the two parameneter variables and return the largest value of the two.

## Exercise 6: Test Averages and Grade

The _determine_grade_ function assumes that the user fills in a positive number between 0 and 100. However, if they enter a negative number, the function will still display a message that they got an F. Otherwise, the function will the function works as expected

In general, the the exercise was pretty straightforward for me because I spent some time in the summer learning programming basics. In this lab, I make the assumption that the user enters a float or integer value where required. Only then will the programs that require user input be able to run properly
