# Exercise 6: Test Average and Grade
def main():
    # Ask the user to enter the scores and display the grade of that score.
    score1 = float(input("Score: "))
    print(f"Grade {determine_grade(score1)}")

    score2 = float(input("Score: "))
    print(f"Grade {determine_grade(score2)}")

    score3 = float(input("Score: "))
    print(f"Grade {determine_grade(score3)}")

    score4 = float(input("Score: "))
    print(f"Grade  {determine_grade(score4)}")

    score5 = float(input("Score: "))
    print(f"Grade {determine_grade(score5)}")

    average_score = calc_average(score1, score2, score3, score4, score5)
    print(f"Average score: {average_score}")
    print(f"Grade {determine_grade(average_score)}")


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
    elif (
        score < 60
    ):  # used an elif instead of else to only return score below 60 and not
        return "F"


main()
