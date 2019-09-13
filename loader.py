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
	print(data_ride_delete[3])

if __name__ == '__main__':
	load_data()