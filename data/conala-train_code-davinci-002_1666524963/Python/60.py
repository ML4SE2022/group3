def check_value_exist(list, value):
    if value in list:
        return True
    else:
        return False

list = [1,2,3,4,5]
value = 3

print(check_value_exist(list, value))