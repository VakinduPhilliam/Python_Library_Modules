# Python Library Modules
# Output Formatting
# The reprlib module provides a version of repr() customized 
# for abbreviated displays of large or deeply nested 
# containers:
 
import reprlib

reprlib.repr(set('supercalifragilisticexpialidocious'))

# Displays "{'a', 'c', 'd', 'e', 'f', 'g', ...}"