import datetime

def convert_date_to_day_of_week(date_string):
    """
    Convert a date string to the day of the week.
    """
    date_object = datetime.datetime.strptime(date_string, '%Y-%m-%d')
    return date_object.strftime('%A')

convert_date_to_day_of_week('2018-01-01')