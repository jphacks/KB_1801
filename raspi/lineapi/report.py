import sys
import datetime

class userDatetime:
	def __init__(self):
		self.day     = 0
		self.weekday = 0
		self.hour    = 0

def flagReport(dateNow, when, udatetime, flag, err):
	dayNow = dateNow.day
	weekdayNow = dateNow.weekday()
	hourNow = dateNow.hour
	if flag == 0:
	# print(dateNow)
		if when == "m":
			if dayNow == udatetime.day and hourNow == udatetime.hour:
				flag = 1
				# sys.exit("aaa")
		elif when == "w":
			if weekdayNow == udatetime.weekday and hourNow == udatetime.hour:
				flag = 1
		elif when == "d":
			if hourNow == udatetime.hour:
				flag = 1
	elif flag == 1:
		if when == "m":
			if hourNow != udatetime.hour:
				flag = 0
		elif when == "w":
			if hourNow != udatetime.hour:
				flag = 0
		elif when == "d":
			if hourNow != udatetime.hour:
				flag = 0
	else:
		err = 1
		flag = 0

	return flag, err



		# whenNow = when.format(dateNow)

	# flag = 1
	# print(int(dd))
	# print(type(dd))

# YEAR  = "{0:%Y}"
# MONTH = "{0:%m}"
# DAY   = "{0:%d}"
# WEEKDAY = "{0:%w}"
# HOUR  = "{0:%H}"
# flag = 0
# err = 0
# for i in range(1, 31):
# 	for j in range(0, 23):
# 		dateNow = datetime.datetime(2018, 10, i, j)
# 		flag, err = flagReport(dateNow, "m", flag, err)
# 		print(i, j, flag, err)