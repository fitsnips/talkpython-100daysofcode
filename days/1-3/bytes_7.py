''' this kicked my but, even after reading it three times I still had a little trouble pulling out
shutdown_entries = [ line for line in loglines if SHUTDOWN_EVENT in line ], thats some crazy python stuff there'''

'''Extract datetimes from log entries and calculate the time
   between the first and last shutdown events'''
from datetime import datetime
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def convert_to_datetime(line):
    '''TODO 1:
       Given a log line extract its timestamp and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)'''
    # pull out the list item that contains the timestamp
    timestamp = line.split()[1]
    # https: // docs.python.org / 3 / library / datetime.html  # strftime-strptime-behavior
    time_format = '%Y-%m-%dT%H:%M:%S'
    # convert to datetime object
    return datetime.strptime(timestamp, time_format)


def time_between_shutdowns(loglines):
    '''TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and calculate the
       timedelta between the first and last one.
       Return this datetime.timedelta object.'''

    shutdown_entries = [line for line in loglines if SHUTDOWN_EVENT in line]
    shutdown_times = [convert_to_datetime(event) for event in shutdown_entries]
    return max(shutdown_times) - min(shutdown_times)