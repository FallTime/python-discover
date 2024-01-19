# Based on Fig. 2.22
# Compare integers using if structures, relational operators
# and equality operators.

print("Enter two integers to compare")

number1 = input("Please enter first integer: ")
number1 = int(number1)

number2 = input("Please enter second integer: ")
number2 = int(number2)

# the if statement in python different of some languages like C++ or Java.
# They don't use braces to denote a code block of this structure, instead they
# are used an indentation to separate code blocks
# Ultimately this doesn't change the effectiveness of the blocks,
# nesting in the code still works, and indentation makes it easier to read.

if number1 == number2:
    print("%d is equal to %d" % (number1, number2))

if number1 != number2:
    print("%d is not equal to %d" % (number1, number2))

if number1 < number2:
    print("%d is less than %d" % (number1, number2))

if number1 > number2:
    print("%d is greater than %d" % (number1, number2))

if number1 <= number2:
    print("%d is less than or equal to %d" % (number1, number2))

if number1 >= number2:
    print("%d is greater than or equal to %d" % (number1, number2))
