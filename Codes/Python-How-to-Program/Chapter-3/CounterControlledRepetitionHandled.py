# Based on Fig. 3.10: fig03_10.py
# Class average program with counter-controlled repetition.
def validmensage(rep):
    if rep == 1:
        print("invalid grade! Please enter {} more valid grade".format(rep))
    else:
        print("invalid grade! Please enter {} more valid grades".format(rep))


# initialization phase
total = 0  # sum of grades
gradeCounter = 0  # number of grades entered

# processing phase
while gradeCounter < 10:  # loop 10 times

    diff = 10 - gradeCounter  # control variable to check how many are missing
    grade = input("Enter grade: ")  # get one grade

    if grade.isdigit():  # Valid if the grade is digits only
        grade = int(grade)  # convert string to an integer

        if 0 < grade < 11:  # Valid if the grade is in the range of 1 to 10
            total = total + grade  # add up the total
            gradeCounter = gradeCounter + 1  # count 1
        else:
            validmensage(diff)  # Error message with information on how many are missing
    else:
        validmensage(diff)  # Error message with information on how many are missing

# termination phase
average = total / gradeCounter  # integer division
print("Class average is", average)  # final output
