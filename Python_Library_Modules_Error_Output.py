# Python Library Modules
# Error Output Redirection and Program Termination
# The sys module also has attributes for stdin, stdout, and stderr. 
# The latter is useful for emitting warnings and error messages 
# to make them visible even when stdout has been redirected:
 
sys.stderr.write('Warning, log file not found starting a new one\n')

# Displays 'Warning, log file not found starting a new one' 
# The most direct way to terminate a script is to use sys.exit().
