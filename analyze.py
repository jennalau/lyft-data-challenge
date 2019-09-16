from utils import *
import pandas as pd
import seaborn as sns

def calcTotalDrivingMin(data):
    """
    calculate mean # of driving min for all drivers for all days
    data shape = (122, 46, 24)
    """
    total = []
    for i in range(0,24):
        total.append([0,0,0])

    for driver in data:
        for hrs in driver: # 1x24 np array of int64
            hrs = hrs.tolist()
            for hr in hrs: 
                if hr > 0:
                    hrsIdx = hrs.index(hr)
                    # number of mins
                    total[hrsIdx][0] += hr
                    # number of drivers
                    total[hrsIdx][1] += 1

    total = np.asarray(total)
    
    # calculate means minutes worked
    for t in total:
        t[2] = t[0] / t[1]

    return total


def calcResidual(data, driver_hash, avg_time):
    num_drivers = len(driver_hash)
    residuals = []
    for i in range(num_drivers):
        residuals.append([0] * 24)
    
    driver_working_min = []
    for i in range(num_drivers):
        driver_working_min.append(0)

    for day in data:
        for driver in range(len(day)):
            driver_time = day[driver]
            r = driver - avg_time
            residuals[driver] += r

            # calculate number of mins. worked
            total_min = np.sum(driver)
            driver_working_min[driver] += total_min
    
    residuals = np.asarray(residuals)  
    driver_working_min = np.asarray(driver_working_min)  
    return residuals, driver_working_min


def driverEfficiency(residuals, driver_working_min):
    driver_rankings = []

    for r in range(len(residuals)):
        # print(residuals[r])
        sum_r = np.sum(residuals[r])
        score = sum_r / driver_working_min[r]
        driver_rankings.append(score)
    
    return np.asarray(driver_rankings)


def analyze(data, driver_hash):
    # calculate total # of driving minutes for all drivers across the entire dataset timespan for 
    # each 1-hour interval & the # of drivers working in each interval
    totalTime = calcTotalDrivingMin(data) # 24 x 3
    print("NUM DRIVERS = ", len(driver_hash)) # 46

    # calculate residuals for each driver
    avg_times = totalTime[:, -1:]
    residuals, driver_working_min = calcResidual(data, driver_hash, np.squeeze(avg_times, axis=-1))
    print("residuals: ", residuals.shape)
    print("driver working minutes: ", driver_working_min)

    driver_rankings = driverEfficiency(residuals, driver_working_min)
