# Based on Fig. 2.13
# Displaying an object’s location, type and value.

# prompt user for input
# In the figure is used raw_input, but in python 3,
# raw_input was renamed to input.
integer1 = input("Enter first Integer:\n")  # prompt
print("integer1 pre-typecast: ", id(integer1), type(integer1), integer1)
integer1 = int(integer1)  # typecast to convert String in Integer.
print("integer1 pos-typecast: ", id(integer1), type(integer1), integer1)

integer2 = input("Enter Second Integer:\n")  # prompt
print("integer2 pre-typecast: ", id(integer2), type(integer2), integer2)
integer2 = int(integer2)  # typecast to convert String in Integer.
print("integer2 pos-typecast: ", id(integer2), type(integer2), integer2)

# in the figure "sum" is used as the variable name,however sum is
# a function in python, avoid unnecessary use of soft keywords
result = integer1 + integer2  # compute and assign result
print("Result: ", id(result), type(result), result)

print("Sum is:", result)  # print sum
