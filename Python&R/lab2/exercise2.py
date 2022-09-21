# Exercise 2: BMI
# A program that calculates the BMI  for a user

# Ask for user weight and height, then convert them into float
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meter: "))

# Calculate the user bmi_index and round to 2 decimal places
bmi_index = round((weight / (height**2)), 2)

# Then display their bmi with a message depending on their bmi_index
if bmi_index < 18.5:
    print(f"You are Underweight with a  bmi index of {bmi_index}")
elif 18.5 <= bmi_index <= 24.99:
    print(f"Your weight is normal with a bmi index of {bmi_index}")
elif 25.0 <= bmi_index <= 29.99:
    print(f"You are overweight with a bmi index of {bmi_index}")
elif bmi_index >= 30:
    print(f"You have obesity with a bmi index of {bmi_index}")
