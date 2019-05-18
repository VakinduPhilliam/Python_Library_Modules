# Python Library Modules
# Software Quality Control
# One approach for developing high quality software is to 
# write tests for each function as it is developed and to 
# run those tests frequently during the development 
# process.
# The 'doctest' module provides a tool for scanning a module 
# and validating tests embedded in a program’s docstrings. 

def average(values):
    """Computes the arithmetic mean of a list of numbers.

    print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest

doctest.testmod()   # automatically validate the embedded tests
