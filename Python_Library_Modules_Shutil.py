# Python Library Modules
# For daily file and directory management tasks, the 
# shutil module provides a higher level interface 
# that is easier to use:
 
import shutil

shutil.copyfile('data.db', 'archive.db')    #Displays 'archive.db'

shutil.move('/build/executables', 'installdir')   #Displays 'installdir'
