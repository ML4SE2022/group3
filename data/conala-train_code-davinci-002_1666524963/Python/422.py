import os

if os.path.isfile('/etc/passwd'):
    print('File exists')
else:
    print('File does not exist')