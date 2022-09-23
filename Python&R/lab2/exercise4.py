# Exercise 4: Sum of Numbers

# initialize a variable to store the the sum of numbers
sum_nums = 0

# Initialize an infinite loop, break it when user input a negative number
while True:
    num = float(input("Number : "))
    # add the number to the sum if its positive
    if num >= 0:
        sum_nums += num
    else:  # if its negative, display the sum and break out of the loop
        print(f"The sum of numbers is {sum_nums}")
        break
