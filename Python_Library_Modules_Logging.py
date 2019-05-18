# Python Library Modules
# Logging
# The logging module offers a full featured and flexible 
# logging system. 
# At its simplest, log messages are sent to a file or to 
# sys.stderr:
 
import logging

logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')
