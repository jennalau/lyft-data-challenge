from loader import *
from utils import *
import pandas as pd
import seaborn as sns

def analyze(working_dataset):

    # slice working_dataset to grab all dates
    set_of_dates = set(working_dataset[0:,:,])

    # dict where key=date, value=np array of mins per time interval
    total_driving = dict.fromkeys(set_of_dates, np.zeros(shape=(1,24)))
    
    # calculate average # of mins per 1-hour interval

    # iterate through each element in 3D np array
    for data in working_dataset:
        date = data[0]
        
        # iterate through each driver-time interval data element
        for driver_data in data:
            # calculate average number of driving min per interval
            hrs = driver_data[1:]
            total_driving[date] = np.add(total_driving[date], hrs)


    # calculate average number of driving mins per date
    avg_driving = dict.fromkeys(set_of_dates, 0)
    
    for date, hours in total_driving:
        avg_driving[item] = pd.DataFrame()

    # print scatterplot per date
    ax = sns.scatterplot(x="Time Interval", y="Minutes Driven", hue="time", data=avg_driving[])


    # [day][driver][hour]



if __name__ == '__main__':
    analyze()