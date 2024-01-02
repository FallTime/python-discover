# Based on article https://realpython.com/python-string-formatting/
# String formatting. For use a Template Strings is necessary import a class template
# built-in string module.

from string import Template

stringValue = "String formatting"
name = "Arthur"
age = 10

# create a template for the string " Hello name! ".
text = Template("Hello $name!")  # we use $ to mark what can be replaced.
print(text.substitute(name="Bob"))
# the substitute method works with indexing by name. $name takes the value of name.

# It is not necessary to create sentences like Template class.
# create a simple strings with insert points marked by $ and use substitute
# method on print
example1 = "Hello, $name. How old are you?"
example2 = "I'm $age years old."

print(Template(example1).substitute(name=name))
print(Template(example2).substitute(age=age))

# the template format is useful for user input strings, thanks to its simplicity.
# You can use in any case, but the others formats is best for greater control.
