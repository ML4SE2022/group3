import datetime

def sort_dates(dates):
    return sorted(dates, key=lambda x: datetime.datetime.strptime(x, '%m/%d/%Y'))