import datetime

date_string = '01/01/17 12:10:03.234567'
date_dt = datetime.datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')

print(date_dt)