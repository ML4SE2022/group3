import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if not os.path.isdir(path):
        return "Not a valid directory"
    if not suffix:
        return "Suffix cannot be empty"
    if not path:
        return "Path cannot be empty"
    if not os.path.exists(path):
        return "Path does not exist"
    if not os.path.exists(suffix):
        return "Suffix does not exist"
    if not os.path.exists(path):
        return "Path does not exist"
    if not os.path.exists(suffix):
        return "Suffix does not exist"
    if not os.path.exists(path):
        return "Path does not exist"
    if not os.path.exists(suffix):
        return "Suffix does not exist"
    if not os.path.exists(path):
        return "Path does not exist"
    if not os.path.exists(suffix):
        return "Suffix does not exist"
    if not os.path.exists(path):
        return "Path does not exist"
    if not os.path.exists(suffix):
        return "Suffix does not exist"
    if not os.path.exists(path):
        return "Path does not exist"
    if not os.path.exists(suffix):
        return "Suffix does not exist"
    if not os.path.exists(path):
        return "Path does not exist"
    if not os.path.exists(suffix):
        return "Suffix does not exist