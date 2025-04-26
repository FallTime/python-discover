import math
import inspect

# trying to discover the methods with functions
print(dir(math))
print(vars(math))

# This module helps with that, but in this case it doesn't return something.
# since most methods in math lib are written in C.
print(inspect.getmembers(math, inspect.isfunction))

# The callable function returns the methods that can be called by the program
func = [name for name in dir(math) if callable(getattr(math, name))]
print(func)

# __loader__ is callable and this is a proof of that
print(callable(math.__loader__))

# In his dir don't have a __call__
print(dir(math.__loader__))

# But is possible call him. He return yourself
print(math.__loader__())

