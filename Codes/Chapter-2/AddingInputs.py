# Based on Fig. 2.8
# Adding values from input (incorrectly) without converting to integers.

# input returns values of type String.
# Python uses dynamic typing, this means that the variable
# will be initialized depending on the assigned value.
# In this case value1 and value2 receive a String variable,
# so they will be Strings.
value1 = input("Enter first Integer:\n")

value2 = input("Enter first Integer:\n")

# the misunderstanding in print is just concatenation instead of summation.
# It is not possible to add Strings using the + symbol
print(value1 + value2)
