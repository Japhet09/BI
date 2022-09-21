
''' Check if a number is positive,
negative or zero and 
display an appropriate message'''

'''Extra content: account for incorrect
variable class being given by user with
the use of error handling (try-except)'''

num = input("Input a integer: ")

try:
    num = int(num) # Error occurs here
                   # when wrong variable
                   # type/class
    if num > 0:
        print("Positive number")
    elif num == 0:
        print("Zero")
    else:
        print("Negative number")
except ValueError:
    print("Please supply an integer!")
