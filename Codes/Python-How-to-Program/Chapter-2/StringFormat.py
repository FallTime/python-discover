# Based on Fig 2.19
# String formatting. That is "Old Style" with % operator. very usual in C.

integerValue = 4237
floatValue = 123456.789
stringValue = "String formatting"

# simple interpolation with comma
print("Integer ", integerValue)
print("Float", floatValue)
print("String", stringValue)

# use of % operator with integer value
print("\nInteger %d" % integerValue)
print("Integer %i" % integerValue)
# there is a subtle difference between %d and %i
# that can be seen in C and C++ documentation.
# It's not worth going into depth about this as this
# formatting choice has fallen into disuse.

print("Lowercase Hexadecimal Integer %x" % integerValue)
print("Uppercase Hexadecimal Integer %X" % integerValue)

# use of % operator with float value
print("\nFloat %f" % floatValue)
print("Float %F" % floatValue)

print("Float %g" % floatValue)
print("Float %G" % floatValue)
# g or G, if a formatting component is not used, it will display
# a decimal, in other words, it displays the float without precision.
# using the correct components will be displayed in exponential formatting,
# lowercase and uppercase respectively to g and G

print("Lowercase exponential %e" % floatValue)
print("Uppercase exponential %E" % floatValue)

# use of % operator with char and String
# Single character or an Integer
print("\nChar %c" % stringValue[0])
print("Char %c" % integerValue)

# these types convert a String to an object in python
# the s use str(), When you declare a string it is already
# converted to this type of object.
print("String %s" % stringValue)

# the r use repr(), summarizing what this method does in
# a simple way, it returns the string with single quotes
print("String %r" % stringValue)

# use method repr() and simple interpolation with comma
stringRepr = repr(stringValue)
print("String", stringRepr)

# the a use ascii(), it also returns the string with single quotes,
# but this converts it to the ascii standard
print("String %a" % stringValue)

# use method ascii() and simple interpolation with comma
stringAscii = ascii(stringValue)
print("String", stringAscii)
