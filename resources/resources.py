import os


def readfile(filename):
    path = os.path.abspath(__file__)

    with open(path.replace('resources.py', filename)) as f:
        return f.read()
