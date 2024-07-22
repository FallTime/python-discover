# Based on Fig. 3.5.
# if/elif/else multiple-selection structure.

# simple structure of if/elsif/else statement
grade = int(input("Enter grade:"))

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")


# In this case we have some amount of unique results based on
# the conditional tests done. It's not one more of a positive
# and negative pattern

