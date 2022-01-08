# Write a function which will be able to show date and time

def local():
	"""It will return current local time""" 
	import time
	x = ""
	for i in time.localtime()[3:5]:
		x = x + str(i) + ":"
	return x[:-1]

def dateandtime():
	"""It will return current date and time"""
	import datetime
	return f"Date is {datetime.date.today()} and time is {local()}"


if __name__ == "__main__":
	print(dateandtime())