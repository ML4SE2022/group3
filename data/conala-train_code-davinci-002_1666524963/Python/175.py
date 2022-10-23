import datetime

current_date = datetime.datetime.now()
six_months_later = current_date + datetime.timedelta(days=180)
print(six_months_later)