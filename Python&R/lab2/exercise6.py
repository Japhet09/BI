# Exercise 6: Test Average and Grade
def main():
    score = float(input("Score: "))
    print(f"You scored {determine_grade(score)}")


# Function that calcualte and returns the average of 5 score
def calc_average(score1, score2, score3, score4, score5):
    avg_score = (score1 + score2 + score3 + score4 + score5) / 5
    return avg_score


# Function that display the grade for the score
def determine_grade(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    elif score < 60: # used an elif instead of else to only return score below 60 and not 
        return "F"


main()
