# Python Library Modules
# Internet Access
# There are a number of modules for accessing the internet 
# and processing internet protocols. 
# Two of the simplest are urllib.request for retrieving data 
# from URLs and smtplib for sending mail:
 
from urllib.request import urlopen

with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
        for line in response:
            line = line.decode('utf-8')  # Decoding the binary data to text.
            if 'EST' in line or 'EDT' in line:  # look for Eastern Time
              print(line)

# Displays '<BR>Nov. 25, 09:43:32 PM EST'

    import smtplib
    server = smtplib.SMTP('localhost')
    server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
    """To: jcaesar@example.org
    From: soothsayer@example.org

    Beware the Ides of March.
    """)
    server.quit()
