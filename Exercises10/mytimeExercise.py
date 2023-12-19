'''
Created by: Michael Floyd
Exercise: Format Date and Time
Date: 13Dec2023
'''

from datetime import datetime as dt
# Get the current time, returns a value like 2022-10-09 17:46:45.151666
today = dt.now()
print(today)
# Get Unix time, returns a value like 1665566809.057217
unix_epoch_time = dt.timestamp(today)
print(unix_epoch_time)

weekday = dt.now().strftime("%A") 
print(weekday)

month = dt.now().strftime("%B")
print(month)

# Formatted
s = dt.now().strftime("%Y %d %B")
print('\nCurrent Date is:', s)

s = dt.now().strftime("%I:%M:%S %p")
print('\nCurrent Time is:', s)


