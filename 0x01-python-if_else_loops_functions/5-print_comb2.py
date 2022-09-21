#!/usr/bin/python3
# A program that prints numbers from 0 to 99
for i in range(100):
    print("{:0>2}".format(i), end=", " if i < 99 else "\n")
