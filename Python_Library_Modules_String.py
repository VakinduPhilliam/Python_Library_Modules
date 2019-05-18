# Python Library Modules
# The string module includes a versatile Template class 
# with a simplified syntax suitable for editing by end-users. 
# This allows users to customize their applications without 
# having to alter the application.

from string import Template
t = Template('${village}folk send $$10 to $cause.')
t.substitute(village='Nottingham', cause='the ditch fund')

# Display 'Nottinghamfolk send $10 to the ditch fund.'
