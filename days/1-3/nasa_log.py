from datetime import datetime
import os
from collections import Counter

def read_logfile():
    logfile = os.path.join('.', 'sample_data','sample.log')
    with open(logfile,'r') as log_input:
        log_lines = log_input.readlines()
    return log_lines

def get_search_string():
    search_string = input('String you would like to search for? ')
    return search_string

def find_matches(log_lines, search_string):
    matches = [line for line in log_lines if search_string in line]
    search_patern_entry_times = [convert_to_datetime(event) for event in matches]

    return search_patern_entry_times

def diplay_final_data(matches):
    for match in matches:
        print(match)



def convert_to_datetime(entry):
    timeformat = '[%d/%b/%Y:%H:%M:%S'
    event_splite = entry.split()[3]

    return datetime.strptime(event_splite,timeformat)

def drop_seconds(entries):
    drop_format = '%Y-%d-%m %H:%M'


    return processed_matches


def count_per_minute(matches):
    '''TODO
    take the entries that match our search pattern and count the the instance per a minute

    :return:
    '''

    return Counter(matches)


    pass

if __name__ == '__main__':
    logentries = read_logfile()
    user_search_entry = get_search_string()
    matched_entries = find_matches(logentries,user_search_entry)
    processed_matches = drop_seconds(matched_entries)
    entry_count = count_per_minute(processed_matches)
    diplay_final_data(entry_count)


