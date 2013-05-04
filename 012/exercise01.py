#!/usr/bin/env python

def sumall(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

def main():
    print sumall(1,2,3,3,5,6,6,77)
    print sumall()
    print sumall(10)
    
if __name__ == "__main__":
    main()
