#!/usr/bin/python3i
# function that checks for lowercase characters

def islower(c):
    """Function checks for lowercase characters."""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
