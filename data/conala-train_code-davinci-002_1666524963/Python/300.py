import datetime

def time_converter(time):
    time = datetime.datetime.strptime(time, '%H:%M')
    return time.strftime('%I:%M %p')

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 PM'
    assert time_converter('09:00') == '09:00 AM'
    assert time_converter('23:15') == '11:15 PM'
    print("Coding complete? Click 'Check' to earn cool rewards!")