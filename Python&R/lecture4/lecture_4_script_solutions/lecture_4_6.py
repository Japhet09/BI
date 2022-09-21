
'''Make a while loop that will only stop printing
if the user solves a simple math question'''

math_solve = int(input("What is the square root of 9?: "))

while math_solve != 3:
    print("Wrong! Try again!")
    math_solve = int(input("What is the square root of 9?: "))

print("Great! You made it!")
