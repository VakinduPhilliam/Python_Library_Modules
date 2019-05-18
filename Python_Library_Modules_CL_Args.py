# Python Library Modules
# Command Line Arguments
# Common utility scripts often need to process command line arguments. 
# These arguments are stored in the sys module’s argv attribute as a list. 
# For instance the following output results from running python 
# demo.py one two three at the command line:

import sys
print(sys.argv)    #Display ['demo.py', 'one', 'two', 'three']
 
# The getopt module processes sys.argv using the conventions of the 
# Unix getopt() function. More powerful and flexible command line 
# processing is provided by the argparse module.
 
