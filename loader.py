import csv
import numpy as np

ride_ids_ = 'data/ride_ids.csv'
ride_timestamps_ = 'data/ride_timestamps.csv'

def load_data():
	data_driver = np.genfromtxt(ride_ids_, dtype=str, delimiter=',', skip_header=1)
	data_driver = data_driver[:, :2]
	data_ride_temp = np.genfromtxt(ride_timestamps_, dtype=str, delimiter=',', skip_header=1)
	data_ride_temp = data_ride_temp[1:, :]
	data_ride_accept = data_ride_temp[::5]
	data_ride_temp = data_ride_temp[3:, :]
	data_ride_dropped = data_ride_temp[::5]
	data_ride_accept = np.delete(data_ride_accept, 1, axis=1)
	data_ride_dropped = np.delete(data_ride_dropped, [0,1], axis=1)
	dim = data_ride_accept.shape[0]
	data_ride = np.hstack((data_ride_accept, data_ride_dropped))
	data = combine_data(data_driver, data_ride)
	data = np.delete(data, [1,2], axis=1)
	return data

def combine_data(driver, ride):
	counter = 0
	new_data = np.empty((200000, 5), dtype='object')
	#for j in range(ride.shape[0]):
	for j in range(5000):
		for i in range(driver.shape[0]):
			if (driver[i, 1] == ride[j, 0]):
				new_data[counter] = np.hstack((driver[i], ride[j]))
				counter += 1
	new_data = new_data[:counter-1, :]
	print(new_data[14])
	return new_data

a = load_data()
np.save("loaded_data(3).csv", a)