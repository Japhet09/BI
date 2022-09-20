def main():
    pass

# Exercise 1: DVD CLUB POINTS
#Asking the user for number of videos  purchased and converting it into int 
videos_purchased =int( input("How many videos did you purchase this month?: "))

# initialize the variable to store the user's earnigs
earnings = None
if videos_purchased == 0:
    earnings = 0
    print(f"Point awarded: {earnings}")
elif videos_purchased == 1:
    earnings = 5
    print(f"Point awarded: {earnings}")
elif videos_purchased == 2:
    earnings = 15
    print(f"Point awarded: {earnings}")
elif videos_purchased == 3:
    earnings = 30
    print(f"Point awarded: {earnings}")
elif videos_purchased >= 4:
    earnings = 60
    print(f"Point awarded: {earnings}")
    
# Exercise 2: BMI
# A program that calculates the BMI  for a user
def bmi():
    weight = float(input("Enter weight in kg: "))
    height = float(input("Enter height in meter: "))
    
    bmi_index = weight / (height ** 2)
    if bmi_index < 18.5:
        print(f"You are Underweight with a  bmi index of {bmi_index}")
    elif 18.5 <= bmi_index <= 24.99:
        print(f"Your weight is normal with a bmi index of {bmi_index}")
    elif 25.0 <= bmi_index <= 29.99:
        print(f"You are overweight with a bmi index of {bmi_index}")
    elif bmi_index >= 30:
        print(f"You have obesity with a bmi index of {bmi_index}") 
        