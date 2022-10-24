import datetime

date_string = '2018-01-01'
date_object = datetime.datetime.strptime(date_string, '%Y-%m-%d')

print(date_object)