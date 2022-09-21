#!/usr/bin/python3
# function that prints a string in uppercase followed by a new line.

def uppercase(str):
    """Function checks for lowercase characters."""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")
