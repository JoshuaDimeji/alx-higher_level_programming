#!/usr/bin/python3
# program that imports the function def add(a, b):

from add_0 import add
a = 1
b = 2
if __name__ == "__main__":
    print('{:d} + {:d} = {:d}'.format(a, b, add(a, b)))
