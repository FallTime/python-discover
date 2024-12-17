# Question 2.7:
# Write a program that reads in two integers, determines and prints whether the first is a
# multiple of the second.

value1 = int(input("Enter First Integer:\n$"))
value2 = int(input("Enter Second Integer:\n$"))

if value1 % value2 == 0:
    print('First Integer is a multiple of the Second')
else:
    print('First Integer is not a multiple of the Second')
