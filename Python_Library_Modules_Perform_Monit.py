# Python Library Modules
# Performance Measurement
# The 'timeit' module quickly demonstrates a modest performance advantage:

from timeit import Timer

Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()

# Displays '0.57535828626024577'

Timer('a,b = b,a', 'a=1; b=2').timeit()

# Displays '0.54962537085770791'
