# Based on article https://realpython.com/python-string-formatting/
# String formatting. That is "New Style" with format() method for
# a String object.

stringValue = "String formatting"
name = "Arthur"
age = 10

# simple positional formatting. Similar to the "old style" % operator
print("Example of {}".format(stringValue))

# simple replacement with numeric index. The first position is 0.
print("The sum of 1 + 2 is {0}".format(1+2))

# replacement with numeric index. In this case, more than
# one argument is passed. They don't appear in order of index
print("The sum of {1} + {2} is {0}".format(1+2, 1, 2))

# Replacing the naming of an argument with a keyword. In that case
# the 'name' keyword receives the value of the 'name' variable
# and replace between the brackets containing the keyword 'name'
print("My name is {name}".format(name=name))

# Another simple positional formatting.
print("Hello, {}. How old are you?".format(name))

# simple positional formatting with more than one argument
print("I'm {} years old and this is {}".format(age, stringValue))
