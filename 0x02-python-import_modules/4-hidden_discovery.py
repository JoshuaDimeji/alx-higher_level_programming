#!/usr/bin/python3
# program that prints all the names defined by the compiled module hidden_4.pyc

if __name__ == "__main__":
    from hidden_4 import *
    lists = dir()
    for i in range(len(lists)):
        if lists[i][:2] != '__':
            print("{}".format(lists[i]))
