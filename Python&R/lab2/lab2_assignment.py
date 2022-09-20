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