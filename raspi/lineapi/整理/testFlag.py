import sys
import datetime
from report import userDatetime, flagReport

# class userDatetime:
# 	def __init__(self):
# 		self.day     = 0
# 		self.weekday = 0
# 		self.hour    = 0

ndt = userDatetime()
ndt.day = 1
ndt.weekday = 0
ndt.hour = 9

flag = 0
err = 0
for i in range(1, 32):
	for j in range(0, 24):
		dateNow = datetime.datetime(2018, 10, i, j)
		flag, err = flagReport(dateNow, "d", ndt, flag, err)
		if flag == 1:
			print(i, j, flag, err)