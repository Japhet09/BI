
# Testing if an input from a user is equal to
# 5, 10, or 15 and print a message accordingly.
# If not, print a suitable message.
# Print a message "Good bye!" in the end of the script.

# Variable to test
var = int(input("Enter an integer: "))

# First try evaluated as True
if var == 15:
   print("1 - Got a true expression value")
   print(var)

# Second try evaluated as True
elif var == 10:
   print("2 - Got a true expression value")
   print(var)

# Third try evaluated as True
elif var == 5:
   print("3 - Got a true expression value")
   print(var)

# All above evaluate as False  
else:
   print("4 - Got a false expression value")
   print(var)

# This will be executed after the
# if-elif-else statements
print("Good bye!")
