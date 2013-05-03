#!/bin/python

def is_sorted(alist):
    pre = alist[0]
    blist = alist[1:]
    for nxt in blist:
        if pre <= nxt:
            pre = nxt
            continue
        else:
            return False
    return True

def main():
    print is_sorted([1,2,2])
    print is_sorted(['b','a'])

if __name__ == "__main__":
    main()
