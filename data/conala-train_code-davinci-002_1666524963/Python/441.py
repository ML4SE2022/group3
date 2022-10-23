import datetime

date_string = "2020-01-01"

date_object = datetime.datetime.strptime(date_string, "%Y-%m-%d")

print(date_object)

print(date_object.strftime("%d-%m-%Y"))