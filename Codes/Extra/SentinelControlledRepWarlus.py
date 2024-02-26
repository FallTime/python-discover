# Based on Fig. 3.13: fig03_13.py
# Class average program with sentinel-controlled repetition.
# I'll use the warlus operator to simplify input process

# initialization phase
total = 0  # sum of grades
gradeCounter = 0  # number of grades entered

# processing phase
while (grade := int(input("Enter grade, -1 to end: "))) != -1:
    total = total + grade
    gradeCounter = gradeCounter + 1

# termination phase
if gradeCounter != 0:
    average = float(total) / gradeCounter
    print("Class average is", average)
else:
    print("No grades were entered")
