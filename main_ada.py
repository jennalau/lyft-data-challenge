import numpy as np
import datetime as dt

def parseDay(day_string):
    return day_string.split("-")

def parseTime(time_string):
    return time_string.split(":")

def parseDateData(date_string):
    date_string = date_string.split(" ")
    day = parseDay(date_string[0])
    time = parseTime(date_string[1])
    dateInfo = dt.date(int(day[0]), int(day[1]), int(day[2]))
    timeInfo = dt.time(int(time[0]), int(time[1]), int(time[2]))
    return dateInfo, timeInfo

def getDayIndex(a):
	lookup_table = [0, 31, 61, 92]
	return (lookup_table[a.month-3] + a.day)

def getData():
	loadData = np.load('loaded_data_CORRECT_bigger.csv.npy')
	driver_hash = dict()
	counter = 0;
	for driver_id in loadData[:,0]:
		if (driver_id not in driver_hash):
			driver_hash[driver_id] = counter
			counter += 1

	extras = loadData[0]

	for row in loadData:
		date1, time1 = parseDateData(row[1])
		date2, time2 = parseDateData(row[2])
		if(date1 == date2):
			row[1] = time1
			row[2] = time2
			row[3] = date1
		else:
			row2 = row
			row[1] = time1
			row[2] = dt.time(23,59,59)
			row[3] = date1
			row2[1] = dt.time(0,0,0)
			row2[2] = time2
			row2[3] = date2
			extras = np.vstack((extras, row2))

	extras = extras[1:, :]
	parseData = np.vstack((loadData, extras))
	
	data = np.zeros((122, len(driver_hash), 24), dtype=int)

	for row in parseData:
		driver_index = driver_hash[row[0]]
		day_index = getDayIndex(row[3])
		start = dt.datetime.combine(row[3], row[1])
		end = dt.datetime.combine(row[3], row[2])
		while(start.hour != end.hour):
			data[day_index, driver_index, start.hour] = (dt.datetime.combine(row[3], dt.time(start.hour,59,59)) - start).seconds/60
			start = dt.datetime.combine(row[3], dt.time(start.hour+1,0,0))
		data[day_index, driver_index, start.hour] = (end - start).seconds/60
	return data