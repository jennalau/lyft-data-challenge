class Driver():
    def __init__(self, driver_id, working_time):
        self.driver_id = driver_id
        self.working_time = working_time 
    
    def getDriverID(self):
        return self.driver_id

    def getWorkingTime(self):
        return self.working_time

    def addWorkingTime(self):
        # dict: key = date: value = # mins work 

