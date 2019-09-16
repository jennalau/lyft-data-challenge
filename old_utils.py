import datetime as dt
from getDayIndex import *

# list of tuples with datetime objects
time_ranges = list(
    (dt.time(0,0,0),  dt.time(0,59,59)), 
    (dt.time(1,0,0),  dt.time(1,59,59)), 
    (dt.time(2,0,0),  dt.time(2,59,59)), 
    (dt.time(3,0,0),  dt.time(3,59,59)), 
    (dt.time(4,0,0),  dt.time(4,59,59)), 
    (dt.time(5,0,0),  dt.time(5,59,59)), 
    (dt.time(6,0,0),  dt.time(6,59,59)), 
    (dt.time(7,0,0),  dt.time(7,59,59)), 
    (dt.time(8,0,0),  dt.time(8,59,59)), 
    (dt.time(9,0,0),  dt.time(9,59,59)), 
    (dt.time(10,0,0), dt.time(10,59,59)), 
    (dt.time(11,0,0), dt.time(11,59,59)), 
    (dt.time(12,0,0), dt.time(12,59,59)), 
    (dt.time(13,0,0), dt.time(13,59,59)), 
    (dt.time(14,0,0), dt.time(14,59,59)), 
    (dt.time(15,0,0), dt.time(15,59,59)),
    (dt.time(16,0,0), dt.time(16,59,59)), 
    (dt.time(17,0,0), dt.time(17,59,59)), 
    (dt.time(18,0,0), dt.time(18,59,59)), 
    (dt.time(19,0,0), dt.time(19,59,59)), 
    (dt.time(20,0,0), dt.time(20,59,59)), 
    (dt.time(21,0,0), dt.time(21,59,59)),
    (dt.time(22,0,0), dt.time(22,59,59)), 
    (dt.time(23,0,0), dt.time(23,59,59)),
)

def parseDay(day_string):
    return day_string.split("-")

def parseTime(time_string):
    return time_string.split(":")

def parseDateData(date_string):
    """
    Read + parse date/time form CSV file

    Argument: str date (from .csv file)
    Returns: datetime object 
    """
    date_string = date_string.split(" ")
    day = parseDay(date_string[0])
    time = parseTime(date_string[1])

    dateInfo = dt.datetime(day[0], day[1], day[2], time[0], time[1], time[2])
    return dateInfo

def calculateWorkingMin(start, end):
    """
    Calculate driving time (in minutes)
    """
    time_diff = start - end
    working_min = time_diff.total_seconds() / 60
    return working_min


def categorizeTimeInterval(start_time, end_time, driver_idx, working_dataset, parsed_data):
    """
    start, end, time: datetime object
    Returns: index of what time interval (for 2d np array)
    """
    
    # check what time interval it is in
    for time in time_ranges:
        if start_time >= time[0]:
            # start/end time exactly within a time interval
            if end_time <= time[1]:
                # calculate index
                dayIdx = getDayIndex(start_time)
                timeIdx = time_ranges.index(time)

                # add to interval
                working_dataset[dayIdx][driver_idx][timeIdx] = calculateWorkingMin(start_time, end_time)
                break

            else:
                # end time overflows 
                while(end_time.time() > time[1]):
                    # get proper indices
                    dayIdx = getDayIndex(start_time)
                    currTimeIdx = time_ranges.index(time)

                    # calculate working mins (for current interval)
                    working_dataset[dayIdx][driver_idx][timeIdx] = calculateWorkingMin(start_time, time[1])

                    # update start_time (FIX THIS... WHAT ABOUT DATE + TIME)
                    start_time = time[1]

                    # move to next time interval
                    time = time_ranges.index(currTimeIdx + 1)