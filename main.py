import numpy as np
from driver import *
from utils import *

def main():
    """
    main executable
    check times, put into intervals
    """

    # TODO: get 2D numpy array from parsing data here
    # read in parsed data 
    parsed_data = np.empty((10, 10)) # placeholder -- modify 
    #parsed_data = load_data()

    
    # create dictionary (key = id, value = index for lookup in 3D np array)
    driver_data = dict()

    # make set of driver IDs
    driver_set = set(parsed_data[:, 0])

    # populate dict
    count = 0
    for d in driver_set:
        driver_data[d] = count
        count += 1


    # intialize 3D np array to hold all data for [day][driver][hour]
    working_dataset = np.empty((122, len(driver_set), 24))

    # calculate driver's working min
    for row in parsed_data:
        # get driver id 
        driver_id = row[0]

        # get driver index
        driver_index = driver_data[driver_id]

        # get start time / end time 
        accepted_at_time = row[1]
        dropped_off_time = row[2]

        # calculate driving min 
        intIdx = categorizeTimeInterval(accepted_at_time, 
                                        dropped_off_time, 
                                        driver_index, 
                                        working_dataset)

    # categorize driver's working min into time intervals
    # num drivers x 24 x 

if __name__ == "__main__":
    main()