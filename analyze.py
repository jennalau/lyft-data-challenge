from utils import *
import pandas as pd
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt

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

            # calculate number of minutes worked
            total_min = np.sum(driver)
            driver_working_min[driver] += total_min
    
    residuals = np.asarray(residuals)  
    driver_working_min = np.asarray(driver_working_min)  
    return residuals, driver_working_min


def driverEfficiency(residuals, driver_working_min, driver_hash):
    driver_rankings = dict()

    for r in range(len(residuals)):
        sum_r = np.sum(residuals[r])

        score = 0
        if driver_working_min[r] > 0:
            score = sum_r / driver_working_min[r]
            # note: we ignored the drivers who were onboarded, but did not work at all 

        driver_rankings[getDriverID(driver_hash, r)] = score

    return driver_rankings


def analyze(data, driver_hash):
    # calculate total # of driving minutes for all drivers across the entire dataset timespan for 
    # each 1-hour interval & the # of drivers working in each interval
    totalTime = calcTotalDrivingMin(data) # 24 x 3

    # calculate residuals for each driver
    avg_times = totalTime[:, -1:]
    residuals, driver_working_min = calcResidual(data, driver_hash, np.squeeze(avg_times, axis=-1))

    driver_rankings = driverEfficiency(residuals, driver_working_min, driver_hash)

    # generate visuals
    visRidePopularity(totalTime[:,0:1])

    compPrimeTime(residuals, driver_working_min, totalTime)


def visRidePopularity(mins):
    time_intervals = [x for x in range(24)]

    print(time_intervals)
    mins = np.squeeze(mins, axis=-1)

    d = {'Time': time_intervals, 'Average # of Minutes Driven': mins}
    data = pd.DataFrame(data = d)

    ax = sns.scatterplot(x=data['Time'], y=data['Average # of Minutes Driven'], data=data)
    fig = ax.get_figure()
    fig.savefig('ride_popularity.png')


def compPrimeTime(residuals, driver_working_min, totalTime):

    print('residuals: ', residuals.shape) # 46 x 24

    resulting_diff = []

    for i in range(24):
        diff = residuals[:,i:i+1]
        resulting_diff.append(np.mean(diff))

    print(resulting_diff)
    means = totalTime[:,0:1]
    means = np.squeeze(means, axis=-1)
    resulting_diff = np.asarray(resulting_diff)

    print("means", means.shape)
    print('resulting_diff: ', resulting_diff.shape)



    # resulting_diff = np.squeeze(resulting_diff, axis=-1)


    d = {'Prime Time': means, 'Residual': resulting_diff}
    data = pd.DataFrame(data = d)

    ax = sns.scatterplot(x=data['Prime Time'], y=data['Residual'], data=data)
    fig = ax.get_figure()
    fig.savefig('prime_time.png')


    all_scores = list(zip(resulting_diff, means))

    return all_scores
