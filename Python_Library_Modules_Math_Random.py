# Python Library Modules
# Mathematics
# The random module provides tools for making random 
# selections:
 
import random

random.choice(['apple', 'pear', 'banana'])  # Displays 'apple'

random.sample(range(100), 10)   # sampling without replacement

# Displays [30, 83, 16, 4, 8, 81, 41, 50, 18, 33]

random.random()    # random float
                   # Displays '0.17970987693706186'

random.randrange(6)    # random integer chosen from range(6)

# Displays '4'
