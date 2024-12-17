# Question 2.5:
# Write a program that reads in the radius of a circle and prints the circle’s diameter,
# circumference and area. Use the constant value 3.14159 for π.
# Do these calculations in output statements.

PI = 3.1415
radius = float(input("Enter Radius:\n$"))

print(f"diameter is {radius * 2:.2f}")
print(f"circumference is {2 * PI * radius:.2f}")
print(f"area is {radius * radius * PI:.2f}")

'''
diameter = radius * 2
circumference = 2 * PI * radius
area = radius * radius * PI
'''
