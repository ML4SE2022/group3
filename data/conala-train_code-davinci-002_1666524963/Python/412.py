import os
import time

def get_file_creation_modification_times(file_path):
    """
    Returns the file creation and modification times.
    """
    # get file creation time
    file_creation_time = os.path.getctime(file_path)
    # get file modification time
    file_modification_time = os.path.getmtime(file_path)
    # convert times to readable format
    file_creation_time = time.ctime(file_creation_time)
    file_modification_time = time.ctime(file_modification_time)
    # return times
    return file_creation_time, file_modification_time

# get file creation & modification times
file_creation_time, file_modification_time = get_file_creation_modification_times(file_path)

# print file creation & modification times
print("File creation time:", file_creation_time)
print("File modification time:", file_modification_time)