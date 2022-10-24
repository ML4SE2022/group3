import datetime

today = datetime.date.today()
six_months = datetime.timedelta(days=180)
six_months_from_now = today + six_months
print(six_months_from_now)