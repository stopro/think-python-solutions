#!/usr/bin/python

from exercise_10 import *
import sys

def bisect(as_list, key):
    if (len(as_list) == 0):
        return None
    head = 0
    tail = len(as_list) - 1
    mid = (head + tail)/2
    while tail >= head:
        if as_list[mid] > key:
            tail = mid - 1
        elif as_list[mid] < key:
            head = mid + 1
        else:
            break
        mid = (head + tail) / 2
    if as_list[mid] == key:
        return mid
    else:
        return None
    

def main():
    args = sys.argv[1:]
    if args:
        print bisect(append_method(), args[0])
    else:
        print 'usage: exercise-11 searchkey'
    
if __name__ == "__main__":
    main()

