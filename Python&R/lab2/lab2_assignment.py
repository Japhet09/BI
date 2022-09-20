'''
In this exercise, I have answered each question using functions, 
the purpose is just to separate echa question from the other questions.
the main function holds all the other functions '''

def main():
    pass

# Exercise 1: DVD CLUB POINTS
# A program that displays the user earnings based on the number of dvd purchased
def dvd_club_points():
    #Asking the user for number of videos  purchased and converting it into int 
    videos_purchased =int( input("How many videos did you purchase this month?: "))

    # initialize a variable to store the user's earnigs
    earnings = None
    
    # then update their earnings based on the videos_purchased and display a message
    # about of how much they earned
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
    #Ask for user weight and height, then convert them into float
    weight = float(input("Enter weight in kg: "))
    height = float(input("Enter height in meter: "))
    
    # Calculate the user bmi_index
    bmi_index = weight / (height ** 2)
    
    #Then display their bmi with a message depending on their bmi_index
    if bmi_index < 18.5:
        print(f"You are Underweight with a  bmi index of {bmi_index}")
    elif 18.5 <= bmi_index <= 24.99:
        print(f"Your weight is normal with a bmi index of {bmi_index}")
    elif 25.0 <= bmi_index <= 29.99:
        print(f"You are overweight with a bmi index of {bmi_index}")
    elif bmi_index >= 30:
        print(f"You have obesity with a bmi index of {bmi_index}") 
        
    
        
# Exercise 3: Property Tax
# Calculate the property tax based on the assessment value
def propert_tax():
    # The percentage to get the assessment value from the actual value
    percent_of_actual = 0.60
    
    # Ask user for the actual property  value and convert it to float
    actual_value = float(input("Actual Property Value: "))
    
    # Calculate the assessment value from the actual property value
    assessment_value = actual_value * percent_of_actual
    
    # to get the tax per dollar divide $0.72 (72¢) by $100
    tax_per_dollar = 0.72 / 100
    
    #Calculate the property tax
    property_tax = assessment_value * tax_per_dollar
    
    
    pass
    
    
    
    
    
    
if __name__ == "__main__":
    main()