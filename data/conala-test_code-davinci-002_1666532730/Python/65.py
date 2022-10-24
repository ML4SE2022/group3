import datetime

def convert_epoch_to_datetime(epoch_time):
    return datetime.datetime.fromtimestamp(epoch_time/1000)

print(convert_epoch_to_datetime(1588291200000))