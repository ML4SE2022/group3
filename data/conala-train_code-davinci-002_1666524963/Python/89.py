import os

def is_descendant(parent, child):
    parent = os.path.abspath(parent)
    child = os.path.abspath(child)
    return child.startswith(parent)