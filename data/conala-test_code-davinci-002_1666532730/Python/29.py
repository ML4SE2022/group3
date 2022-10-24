import datetime

def order_by_date(list_of_dicts):
    return sorted(list_of_dicts, key=lambda x: datetime.datetime.strptime(x['date'], '%Y-%m-%d'))