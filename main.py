import numpy as np
import datetime as dt
from driver import *


def parseDate(date_string):
    date_string = date_string.split(" ")
    day = date_string[0].split("-")
    time = date_string[1].split(":")

    dateInfo = dt.datetime(day[0], day[1], day[2], time[0], time[1], time[2])
    return dateInfo

def calculateWorkingMin(row):
    """
    calculate driving time (in minutes)
    
    """
    dropped_off_time = parseDate(row[2])
    accepted_time = parseDate(row[1])
    time_diff = dropped_off_time - accepted_time

    working_min = time_diff.total_seconds() / 60
    return working_min


def main():
    """
    main executable
    check times, put into intervals
    """

    # TODO: get 2D numpy array from parsing data here
    parsed_data = np.empty((10, 10)) # placeholder -- modify 
    print(parsed_data)

    # make set of driver IDs
    driver_set = set(parsed_data[:, 0])

    driver_obj = []
    for driver_id in driver_set:
        d = Driver(driver_id, 0)
        driver_obj.append(d)

    # key=id; value=Driver() object
    driver_working_data = dict(zip(driver_set, driver_obj))

    # calculate driver's working min
    for row in parsed_data:
        driver_id = row[0]
        driver_working_data = calculateWorkingMin(row)

        driver_working_data[driver_id] = 0

        

    # categorize driver's working min into time intervals
    # num drivers x 24 x 

if __name__ == "__main__":
    main()