import os

def get_files(path, extension):
    """
    Returns a list of files in a directory with a given extension.
    """
    files = []
    for file in os.listdir(path):
        if file.endswith(extension):
            files.append(file)
    return files