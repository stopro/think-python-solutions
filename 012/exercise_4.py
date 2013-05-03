#!/usr/bin/env python

def histogram(words):
    d = {}
    for w in words:
        v = d.get(w,0)
        d[w] = v+1
    return d
    
def reverse_lookup(d,v):
    klist = []
    for k in d:
        if d[k] == v:
            klist.append(k)
    if len(klist) == 0:
        raise ValueError
    else:
        return klist

def invert_dict(d):
    reverse = {}
    for key in d:
        value = d[key]
        if value not in reverse:
            reverse[value] = [key]
        else:
            reverse[value].append(key)
    return reverse
    
print reverse_lookup(histogram('thisisfunction'), 2)
print invert_dict(histogram('thisisanotherfunction'))
