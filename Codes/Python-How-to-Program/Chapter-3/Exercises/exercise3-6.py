# Question #.6:
# The factorial of a nonnegative integer n is written n! (pronounced “n factorial”) and is defined as follows:
# n! = n . (n - 1) . (n - 2) . … . 1 (for values of n greater than or equal to 1) and n! = 1 (for n = 0).
# For example, 5! = 5 · 4 · 3 · 2 · 1, which is 120.
# Factorials increase in size very rapidly. What is the largest factorial that your program can calculate before leading
# to an overflow error?

# a) Write a program that reads a nonnegative integer and computes and prints its factorial.
def factorial(integer):
    result = 1
    if integer == 0:
        return 1
    while integer != 1:
        result *= integer
        integer -= 1
    return result


print("5 factorial is", factorial(5))

# b) Write a program that estimates the value of the mathematical constant e by using the formula
# [Note: Your program can stop after summing 10 terms.]
# Formula: e = 1 / 0! ( or 1 ) +  1 / 1! + 1 / 2! + 1 / 3! + ...
# In the question the formula given is incorrect. The constant e approaches 2,718281828
def estimate_e():
    e = 0
    for i in range(10):
        e += 1 / factorial(i)
    return e


print(f"{estimate_e():.5f}")

# c) Write a program that computes the value of e^x by using the formula
# [Note: Your program can stop after summing 10 terms.]
# e^x = 1 + x / 0! ( or x )  + x / 1! + x^2 / 2! + x^3 / 3! + ...
# In the question the formula given is incorrect.
def estimate_ex(x):
    ex = 1 + x
    actual_x = x
    for i in range(1, 11):
        ex += actual_x / factorial(i)
        actual_x *= x
    return ex


print(f"{estimate_ex(2):.5f}")
