# Python Library Modules
# Dates and Times
# The datetime module supplies classes for manipulating 
# dates and times in both simple and complex ways. 
# dates are easily constructed and formatted

from datetime import date
now = date.today()
now
datetime.date(2003, 12, 2)

now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")

# Displays '12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'

# dates support calendar arithmetic

birthday = date(1964, 7, 31)
age = now - birthday
age.days

# Displasys '14368'
