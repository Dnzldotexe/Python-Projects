# Pseudocode for this activity
"""
Start
Take User Inputs
Compute User Inputs Using The Given Formula
    Solve For Quizzes Mean
    Solve For The Grade
Use If-Else Statement For The Solved Grade
Print The Grade Block
End
"""


# ask user for input
quiz_1 = float(input("Enter Grade for Quiz 1: "))
quiz_2 = float(input("Enter Grade for Quiz 2: "))
quiz_3 = float(input("Enter Grade for Quiz 3: "))
seatwork = float(input("Enter Grade for Seatwork: "))
assignment = float(input("Enter Grade for Assignment: "))
project = float(input("Enter Grade for Project: "))
exams = float(input("Enter Grade for Major Exams: "))


# computes the input using the given formula
quizzes = float((quiz_1 + quiz_2 + quiz_2) / 3)
grade = float((quizzes + seatwork + assignment + project + exams) / 5)


# generates a desired grade output along with the watermark
if grade >= 95: 
    print("\n")
    print("\n")
    print("Percentage Grade: ", "%.2f" % grade, "%")
    print("Numerical Equivalent: 4.0")
    print("Letter Equivalent: A")
    print("Description: Excellent")
    print("\n")
    print("Creator's Name: Danziel Cempron")
    print("Creator's Section: SS221")
    print("\n")
elif grade >= 90: 
    print("\n")
    print("\n")
    print("Percentage Grade: ", "%.2f" % grade, "%")
    print("Numerical Equivalent: 3.5")
    print("Letter Equivalent: B+")
    print("Description: Superior")
    print("\n")
    print("Creator's Name: Danziel Cempron")
    print("Creator's Section: SS221")
    print("\n")
elif grade >= 86: 
    print("\n")
    print("\n")
    print("Percentage Grade: ", "%.2f" % grade, "%")
    print("Numerical Equivalent: 3.0")
    print("Letter Equivalent: B")
    print("Description: Very Good")
    print("\n")
    print("Creator's Name: Danziel Cempron")
    print("Creator's Section: SS221")
    print("\n")
elif grade >= 82: 
    print("\n")
    print("\n")
    print("Percentage Grade: ", "%.2f" % grade, "%")
    print("Numerical Equivalent: 2.5")
    print("Letter Equivalent: C+")
    print("Description: Good")
    print("\n")
    print("Creator's Name: Danziel Cempron")
    print("Creator's Section: SS221")
    print("\n")
elif grade >= 78: 
    print("\n")
    print("\n")
    print("Percentage Grade: ", "%.2f" % grade, "%")
    print("Numerical Equivalent: 2.0")
    print("Letter Equivalent: C")
    print("Description: Satisfactory")
    print("\n")
    print("Creator's Name: Danziel Cempron")
    print("Creator's Section: SS221")
    print("\n")
elif grade >= 74: 
    print("\n")
    print("\n")
    print("Percentage Grade: ", "%.2f" % grade, "%")
    print("Numerical Equivalent: 1.5")
    print("Letter Equivalent: D+")
    print("Description: Fair")
    print("\n")
    print("Creator's Name: Danziel Cempron")
    print("Creator's Section: SS221")
    print("\n")
elif grade >= 70: 
    print("\n")
    print("\n")
    print("Percentage Grade: ", "%.2f" % grade, "%")
    print("Numerical Equivalent: 1.0")
    print("Letter Equivalent: D")
    print("Description: Passed")
    print("\n")
    print("Creator's Name: Danziel Cempron")
    print("Creator's Section: SS221")
    print("\n")
elif grade >= 0: 
    print("\n")
    print("\n")
    print("Percentage Grade: ", "%.2f" % grade, "%")
    print("Numerical Equivalent: 0.0")
    print("Letter Equivalent: F")
    print("Description: Failed")
    print("\n")
    print("Creator's Name: Danziel Cempron")
    print("Creator's Section: SS221")
    print("\n")
else:
    print("\n")
    print("\n")
    print("You are Insane!")
    print("\n")
    print("Creator's Name: Danziel Cempron")
    print("Creator's Section: SS221")
    print("\n")