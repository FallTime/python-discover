# Based on Fig. 2.18
# Creating strings and using quote characters in strings.

# " " and ' ' define a string in python
print("This is a string with \"double quotes.\"")  # use escape sequence
print('This is another string with "double quotes."')  # use ' ' for string.
# we can use special character " in this case
print('This is a string with \'single quotes.\'')  # use escape sequence

# Python also supports triple-quoted strings
# Triple-quoted strings allows use special characters
# without the need use escape sequences
print("This is another string with 'single quotes.'")
print("""This string has "double quotes" and 'single quotes'.
 You can even do multiple lines.""")
print('''This string also has "double" and 'single' quotes.''')
