from datetime import datetime
from datetime import timedelta
from time import sleep


def timeloop(delta):
    start_time = datetime.today()
    delta_time = timedelta(minutes=delta)
    target_time = start_time + delta_time


    print('Time started: ', end='')
    while datetime.today() < target_time:
        #print("Current minute {} ".format(datetime.today()))
        #print("Target minute {}".format(target_time))
        print("*",end='')
        sleep(60)


    print()
    print(" time is up!")
    return False



if __name__ == '__main__':

    delta_input = 0

    while int(delta_input) < 60:
        delta_input = int(input("How many minutes would you like your timer to be set for: "))
        delta_input = timeloop(delta_input)

