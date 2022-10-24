def checkKey(dict, key):

    if key in dict.keys():
        print("Present, ", end =" ")
        print("value =", dict[key])
    else:
        print("Not present")

# Driver Code
dict = {'a': 100, 'b':200, 'c':300}

key = 'b'
checkKey(dict, key)

key = 'w'
checkKey(dict, key)