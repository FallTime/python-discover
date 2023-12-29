# Based on the articles https://realpython.com/python-string-formatting/
# and https://realpython.com/python-f-strings/
# String formatting. That is literal string interpolation, also called fString.
# It is present in Python versions 3.6+.

stringValue = "String formatting"
name = "Arthur"
age = 10

# simple interpolation whit F-String. Simply put, use an f
# before a string. The format is f" " or f' '.
# put the variable name inside curly braces to reference it.
print(f"Example of {stringValue}")

# simple interpolation whit F-String. You can embed almost
# any Python expression in an f-string.
print(f"The sum of 1 + 2 is {1 + 2}")
print(f"The sum of {1} + {2} is {1 + 2}")

# Example with a complex expression. This example uses some list concepts.
print(f"{[2**n for n in range(1, 10)]}")

# Another simples interpolation.
print(f"My name is {name}")
print(f"Hello, {name}. How old are you?")
print(f"I'm {age} years old and this is {stringValue}")

# I tried to reproduce the same case used in the "new" style formatting,
# but it limits the application of the F-String, mainly because
# in the last case I did not use numeric formatting

number = 123456789
balance = 5124.887553
text = "Center Text"

# formatting operator after :
print(f"{number:,}")  # comma separators for thousands place values

# formatting for float value limit the decimal places that will be displayed
print(f"{balance:.2f}")

# formatting for text layout
print(f"{text:=^20}")

# use of flags
print(f"{text!s}")
print(f"{text!r}")
