# Question 3.4:
# A palindrome is a number or a text phrase that reads the same backwards or forwards. For
# example, each of the following five-digit integers is a palindrome: 12321, 55555, 45554 and 11611.
# Write a program that reads in a five-digit integer and determines whether it is a palindrome.
# (Hint: Use the division and modulus operators to separate the number into its individual digits.)

def is_palindrome(stream):
    first_digit = stream // 10000
    second_digit = (stream // 1000) % 10
    fourth_digit = (stream % 100 - stream % 10) // 10
    end_digit = stream % 10

    if first_digit == end_digit and second_digit == fourth_digit:
        print("Is a palindrome\n")
        return

    print("Is not a palindrome\n")


while True:
    sequence = input("(model : 11111, 12345, 00000, etc.)\nEnter a five-digit integer (-1 to end): ")
    try:
        if sequence == '-1':
            break
        if len(sequence) == 5:
            sequence = int(sequence)
            is_palindrome(sequence)
        else:
            print("Invalid input. Please enter a five-digit number.\n")

    except ValueError:
        print("Invalid input. Please enter a numeric value.\n")
