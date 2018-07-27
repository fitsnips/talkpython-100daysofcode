from datetime import datetime, timedelta
from time import sleep

timer_minutes = int(input('How many minutes whould you like to set your timer for: '))


start_time = datetime.today()
target_time = start_time + timedelta(minutes=timer_minutes)
time_format = '%Y-%d-%m %H:%M'

print('Timer started at {} '.format(start_time.strftime(time_format)), end=' ')

while True:
    if datetime.today() > target_time:
        print('Times up!')
        break
    else:
        sleep(60)
        print('*', end=' ')

print()
print('Timer ended at {}'.format(datetime.today().strftime(time_format)))
