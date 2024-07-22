# Based on Fig. 3.15: fig03_15.py
# Analysis of examination results.

# initialize variables
passes = 0  # number of passes
failures = 0  # number of failures
studentCounter = 1  # counter

# First input with notation
result = int(input("[1-pass,2-fail]\nEnter result:"))

# process 10 students; counter-controlled loop
while studentCounter <= 10:
    # Conditional test to increment variables
    if result == 1:
        passes += 1
    else:
        failures += 1
    # Increment counter
    studentCounter += 1
    # Repeated input without notation
    result = int(input("Enter result:"))

# termination phase
print("{} Students pass".format(passes))
print("{} Students fail".format(failures))
# Conditional test for last output
if passes > 8:
    print("Raise tuition")
