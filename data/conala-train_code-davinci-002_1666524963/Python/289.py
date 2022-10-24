import os

def list_files(dir):
    r = []
    subdirs = [x[0] for x in os.walk(dir)]
    for subdir in subdirs:
        files = os.walk(subdir).next()[2]
        if (len(files) > 0):
            for file in files:
                r.append(subdir + "/" + file)
    return r