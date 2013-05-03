#!/bin/python

import random

# assume that the list has some elements inside

def has_duplicates(alist):
    blist = sorted(alist)
    pre = blist[0]
    blist = blist[1:]
    if blist != None:
        for nxt in blist:
            if pre == nxt:
                return True
            else:
                pre = nxt
    
    return False

def gen_students_birthday():
    birthdays = []
    for i in range(0,23):
        birthdays.append(random.randint(1,31))
    return birthdays

dup = 0
undup = 0
for i in range(0,10000):
    if has_duplicates(gen_students_birthday()):
        dup += 1
    else:
        undup += 1

print 'duplicated times is ', dup
