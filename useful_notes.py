dir()
# Prints the attributes of an object
obj.__dict__
# Prints the attributes of an object along with its class and parameters

help()
# helper function

bool()
# check truthy

perf_counter()
# to calculate execution time
# from time

wraps()
# preserver the signature of the original function in decorators
# see decorator note
# from functools

print(*object, sep=" ", end="/n", file=sys.stdout, flush=False)

# Dummy variable
# if we dont want certain data then represent with _
#eg: we only want city and popln from tuple. 
city, _, popln = "Bkt", "Nepal", 100_000_000
from collections import name


import sys
sys.modules

sys.__file__  # see the file path

sys.exec_info()
# returns the tuple of current exception raised if any
# use this in except block to see what except has been raised.


obj.__class__.__name__  # to see what class is the object created from