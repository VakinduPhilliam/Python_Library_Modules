# Python Library Modules
# Operating System Interface
# The os module provides dozens of functions for 
# interacting with the operating system:
# Be sure to use the 'import os' style instead of 'from os import *'. 
# This will keep os.open() from shadowing the built-in open() 
# function which operates much differently.
# The built-in dir() and help() functions are useful as 
# interactive aids for working with large modules like os:

 
import os

os.getcwd()      # Return the current working directory
                 # Displays 'C:\\Python37'

os.chdir('/server/accesslogs')   # Change current working directory

os.system('mkdir today')   # Run the command mkdir in the system shell
                           # Displays '0'
