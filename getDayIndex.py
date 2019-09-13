import datetime

lookup_table = [0, 31, 61, 92]

def getDayIndex(a):
	return (lookup_table[a.month-3] + a.day)