# Exercise 5: Maximum of Two values
def main():
    # Convert user input to integer values
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    print(f"The greater value is {my_max(num1, num2)}")

# Function accepts two float parameters and returns the maximum value

def my_max(num1, num2):
    # If num1 is smaller than num2, then return num2
    if num1 < num2:
        return num2
    # if the conditon above is False, that means num1 is greater than num2
    else:
        return num1

main()