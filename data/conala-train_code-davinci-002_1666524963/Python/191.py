import datetime
import pytz

utc = pytz.utc

today = datetime.date.today()

print(today)

utc_today = utc.localize(today)

print(utc_today)