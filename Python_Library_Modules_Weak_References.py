# Python Library Modules
# Weak References
# The 'weakref' module provides tools for tracking objects 
# without creating a reference. When the object is no 
# longer needed, it is automatically removed from a weakref 
# table and a callback is triggered for weakref objects. 
# Typical applications include caching objects that are 
# expensive to create:

import weakref, gc

class A:
        def __init__(self, value):
            self.value = value
        def __repr__(self):
            return str(self.value)

a = A(10)                   # create a reference
d = weakref.WeakValueDictionary()
d['primary'] = a            # does not create a reference
d['primary']                # fetch the object if it is still alive

# Displays '10'

del a                       # remove the one reference
gc.collect()                # run garbage collection right away

# Displays '0'

>>> d['primary']                # entry was automatically removed
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    d['primary']                # entry was automatically removed
