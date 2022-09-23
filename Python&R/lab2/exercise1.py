# Exercise 1: DVD CLUB POINTS
# A program that displays the user earnings based on the number of dvd purchased

# Asking the user for number of videos  purchased and converting it into int
videos_purchased = int(input("How many videos did you purchase this month?: "))

# Initialize a variable to store the user's earnigs
earnings = None

# then update their earnings based on the videos_purchased and display a message
# about of how much they earned

if videos_purchased == 0:
    earnings = 0
    print(f"Points awarded: {earnings}")
elif videos_purchased == 1:
    earnings = 5
    print(f"Points awarded: {earnings}")
elif videos_purchased == 2:
    earnings = 15
    print(f"Points awarded: {earnings}")
elif videos_purchased == 3:
    earnings = 30
    print(f"Points awarded: {earnings}")
elif videos_purchased >= 4:
    earnings = 60
    print(f"Points awarded: {earnings}")
