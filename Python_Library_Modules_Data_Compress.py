# Python Library Modules
# Data Compression
# Common data archiving and compression formats are directly 
# supported by modules including: zlib, gzip, bz2, lzma, 
# zipfile and tarfile.
 
import zlib

s = b'witch which has which witches wrist watch'
len(s)                 # Displays '41'

t = zlib.compress(s)
len(t)                # Displays '37'

zlib.decompress(t)

# Displays b'witch which has which witches wrist watch'

zlib.crc32(s)         # Displays '226805979'
