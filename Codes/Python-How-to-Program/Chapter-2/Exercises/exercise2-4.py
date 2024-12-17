# Question 2.4:
# Write a program that requests the user to enter two numbers and prints the sum,
# product, difference and quotient of the two numbers.

value1 = int(input("Enter First Number:\n$"))
value2 = int(input("Enter Second Number:\n$"))

sum = value1 + value2
product = value1 * value2
difference = value1 - value2
quotient = value1 / value2

print(f"Sum is {sum}")
print(f"Product is {product}")
print(f"Difference is {difference}")
print(f"Quotient is {quotient}")
