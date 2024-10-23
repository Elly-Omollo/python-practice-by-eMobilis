# Grade Categorizer
# Write a program that takes a score (0-100) as input and categorizes it into one of the following
# grades:
# ● A (90-100)
# ● B (80-89)
# ● C (70-79)
# ● D (60-69)
# ● F (below 60)


def myGrade(score):
    if  90 <=score <= 100: 
        return "Grade A"
    elif 80 <= score < 90:
        return "Grade B"
    elif  70 <= score < 80:
        return "Grade C"
    elif 60 <= score < 70:
        return "Grade D"
    else:
        return "Grade F"

score = int(input("Enter your score \t"))
grade = myGrade(score)

if score >= 101:
    print("The score must be in a range of 0 - 100: \n \t Please try again")
else:
    print('\t'f"The score of {score} is {grade}")