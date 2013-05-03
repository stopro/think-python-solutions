#!/bin/python

def remove_duplicates(alist):
    slist = sorted(alist)
    pre = slist[0]
    blist = slist[1:]
    if blist != None:
        for e in blist:
            if pre == e:
                alist.remove(e)
            else:
                pre = e

    return alist
print remove_duplicates([1,2,7,4,1,2,3,3,5,30])

