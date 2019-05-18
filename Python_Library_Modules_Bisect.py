# Python Library Modules
# Tools for Working with Lists
# Bisect
# In addition to alternative list implementations, the 
# library also offers other tools such as the 'bisect' 
# module with functions for manipulating sorted lists:
 
import bisect

scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
scores

# Displays [(100, 'perl'), (200, 'tcl'), (300, 'ruby'), (400, 'lua'), (500, 'python')]
