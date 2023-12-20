# Based on Fig. 2.7
# Simple addition program.

# prompt user for input
# In the figure is used raw_input, but in python 3,
# raw_input was renamed to input.
integer1 = input("Enter first Integer:\n")  # prompt
integer1 = int(integer1)  # typecast to convert String in Integer.

integer2 = input("Enter Second Integer:\n")  # prompt
integer2 = int(integer2)  # typecast to convert String in Integer.

# in the figure "sum" is used as the variable name,however sum is
# a function in python, avoid unnecessary use of soft keywords
result = integer1 + integer2  # compute and assign result

print("Sum is:", result)  # print sum
