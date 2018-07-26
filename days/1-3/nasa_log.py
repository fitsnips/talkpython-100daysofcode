from datetime import datetime
import os


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


def count_per_minute(matches):
    '''TODO
    take the entries that match our search pattern and count the the instance per a minute

    :return:
    '''

    #alltimestamps = matches
    #count = []

    #for time in matches:
    #    for secondtime in alltimestamps:
    #        if time.minute == secondtime.minute:
    #            count[time.minute] += 1


    pass

if __name__ == '__main__':
    logentries = read_logfile()
    user_search_entry = get_search_string()
    matched_entries = find_matches(logentries,user_search_entry)
    count_per_minute(matched_entries)
    diplay_final_data(matched_entries)


