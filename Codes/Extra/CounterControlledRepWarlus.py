# Based on Fig. 3.10: fig03_10.py
# Class average program with counter-controlled repetition.

# initialization phase
total = 0  # sum of grades
gradeCounter = 0  # number of grades entered

# processing phase
while (gradeCounter := gradeCounter + 1) <= 10:  # loop 10 times
    grade = input("Enter grade: ")  # get one grade
    grade = int(grade)  # convert string to an integer
    total = total + grade  # add up the total

# termination phase
average = total / 10  # integer division
print("Class average is", average)  # output
