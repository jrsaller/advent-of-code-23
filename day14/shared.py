import os
import sys

def read_file(filename):
    filename = os.path.join(sys.path[0], filename)
    with open(filename, "r") as f:
        return [x.strip() for x in f.readlines()]
