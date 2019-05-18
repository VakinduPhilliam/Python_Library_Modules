# Python Library Modules
# Tools for Working with Lists
# The 'heapq' module provides functions for implementing 
# heaps based on regular lists. 
# The lowest valued entry is always kept at position zero. 
# This is useful for applications which repeatedly access 
# the smallest element but do not want to run a full list 
# sort:
 
from heapq import heapify, heappop, heappush
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)                      # rearrange the list into heap order
heappush(data, -5)                 # add a new entry
[heappop(data) for i in range(3)]  # fetch the three smallest entries

# Displays [-5, 0, 1]
