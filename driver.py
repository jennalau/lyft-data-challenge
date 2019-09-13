import numpy as np

class Driver():
    def __init__(self, driver_id):
        self.driver_id = driver_id
        self.driving_time_arr = {} # make this a 2D numpy array
        
    def getDriverID(self):
        return self.driver_id

    def getWorkingTime(self):
        return self.working_time

    def addWorkingTime(self):
        # dict: key = date: value = # mins work 
        # [date, time-interval-1, time-interval-2, etc.]

