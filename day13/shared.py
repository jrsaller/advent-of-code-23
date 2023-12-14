import os
import sys

# split a text file based on an empty line
def read_file_split(filename):
    filename = os.path.join(sys.path[0], filename)
    with open(filename, "r") as f:
        return [x.strip() for x in f.read().split("\n\n")]

def read_file(filename):
    filename = os.path.join(sys.path[0], filename)
    with open(filename, "r") as f:
        return [x.strip() for x in f.readlines()]
