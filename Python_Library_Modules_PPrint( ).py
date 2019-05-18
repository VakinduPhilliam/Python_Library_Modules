# Python Library Modules
# The pprint module offers more sophisticated control 
# over printing both built-in and user defined objects 
# in a way that is readable by the interpreter. 
# When the result is longer than one line, the “pretty printer” 
# adds line breaks and indentation to more clearly reveal 
# data structure:
 
import pprint

t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
    'yellow'], 'blue']]]

pprint.pprint(t, width=30)

# Displays [[[['black', 'cyan'],
# Displays 'white',
# Displays  ['green', 'red']],
# Displays  [['magenta', 'yellow'],
# Displays  'blue']]]
