import os
import random

def random_file(path):
    files = os.listdir(path)
    index = random.randrange(0, len(files))
    return files[index]

print(random_file('/home/user/dir'))