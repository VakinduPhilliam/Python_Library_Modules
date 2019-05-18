# Python Library Modules
# Tools for Working with Lists
# The 'collections' module provides a deque() object 
# that is like a list with faster appends and pops 
# from the left side but slower lookups in the middle. 
# These objects are well suited for implementing 
# queues and breadth first tree searches:

from collections import deque

unsearched = deque([starting_node])

def breadth_first_search(unsearched):
    node = unsearched.popleft()

    for m in gen_moves(node):
        if is_goal(m):
            return m
        unsearched.append(m)
