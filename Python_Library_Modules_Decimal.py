# Python Library Modules
# Decimal Floating Point Arithmetic
# The 'decimal' module offers a Decimal datatype for decimal 
# floating point arithmetic. Compared to the built-in float 
# implementation of binary floating point, the class is 
# especially helpful for;
# 1. financial applications and other uses which require exact decimal 
#    representation,
# 2. control over precision,
# 3. control over rounding to meet legal or regulatory requirements,
# 4. tracking of significant decimal places, or
# 5. applications where the user expects the results to match calculations 
#     done by hand.


from decimal import *

round(Decimal('0.70') * Decimal('1.05'), 2)
Decimal('0.74')

round(.70 * 1.05, 2)

# Displays '0.73'

