# Question 3.5:
# Input an integer containing 0s and 1s (i.e., a “binary” integer) and print its decimal equivalent.
# Appendix C, Number Systems, discusses the binary number system. (Hint: Use the modulus and division
# operators to pick off the “binary” number’s digits one at a time from right to left. Just as in the
# decimal number system, where the rightmost digit has the positional value 1 and the next digit leftward
# has the positional value 10, then 100, then 1000, etc., in the binary number system, the rightmost digit
# has a positional value 1, the next digit leftward has the positional value 2, then 4, then 8, etc.
# Thus, the decimal number 234 can be interpreted as 2 * 100 + 3 * 10 + 4 * 1. The decimal equivalent of binary
# 1101 is 1 * 8 + 1 * 4 + 0 * 2 + 1 * 1.)

def to_binary(stream):
    pos_value = 1
    decimal = 0
    while stream > 0:
        digit = stream % 10
        decimal += digit * pos_value
        stream //= 10
        pos_value *= 2

    return decimal


while True:
    binary = input("Enter a binary sequence (-1 to end): ")
    if binary == '-1':
        break
    try:
        if all(digit in '01' for digit in binary):
            binary = int(binary)
            decimal_value = to_binary(binary)
            print(f"The decimal equivalent of binary {binary} is {decimal_value}\n")
        else:
            print("Invalid input. Please enter a binary number containing only 0s and 1s.\n")
    except ValueError:
        print("Invalid input. Please enter a valid integer.\n")
