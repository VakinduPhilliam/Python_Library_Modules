# Python Library Modules
# String Pattern Matching
# The 're' module provides regular expression (regex) tools for  
# advanced string processing. 
# For complex matching and manipulation, regular expressions offer 
# succinct, optimized solutions:
 
import re

re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')

# The above displays ['foot', 'fell', 'fastest']

re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')   

# The above displays 'cat in the hat'
