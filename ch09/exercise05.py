#!/usr/bin/python

def uses_all(word, keys):
    for key in keys:
        if not key in word:
            return False
    return True

keys = 'abcde'

def words_use_all(keys):
    result = []
    fin = open('words.txt')
    for w in fin:
        w = w.strip()
        if uses_all(w, keys):
            result.append(w)
    fin.close()
    return result
print words_use_all(keys)
