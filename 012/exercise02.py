#!/usr/bin/env python

import random

def sort_by_length(words):
    t = []
    for word in words:
        t.append((len(word),random.random(), word))

    t.sort(reverse = True)

    res = []
    for length, rand, word in t:
        res.append(word)
    return res


def main():
    words = ['The', 'second', 'loop', 'traverses', 'the', 'list', 'of', 'tuples', 'and', 'builds', 'a', 'list', 'of', 'words', 'in', 'descending', 'order', 'of', 'length']
    print sort_by_length(words)
    
if __name__ == "__main__":
    main()
