from datetime import date, timedelta
from dateutil.rrule import rrule, MONTHLY, FR

def get_second_friday(year, month):
    return list(rrule(freq=MONTHLY, byweekday=FR(2), dtstart=date(year, month, 1)))[1]

def get_daterange(year, month):
    second_friday = get_second_friday(year, month)
    return second_friday - timedelta(days=7), second_friday + timedelta(days=7)

print(get_daterange(2020, 1))
# (datetime.date(2019, 12, 27), datetime.date(2020, 1, 10))