#!/bin/python

def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)

print is_anagram('abroad','broadd')
print is_anagram('tear','reat')


