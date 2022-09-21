#!/usr/bin/python3
# function that prints the last digit of a number

def print_last_digit(number):
    tmp = int(repr(number)[-1])
    print("{}".format(tmp), end="")
    return tmp
