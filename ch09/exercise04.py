#!/usr/bin/python

def uses_only(word, keys):
    for w in word:
        if not w in keys:
            return False
    return True

print uses_only('onlyyouloveyounotme','onlyyouloveme')
