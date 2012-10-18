#!/usr/bin/python

def is_next(letter1, letter2):
    dist = ord(letter2) - ord(letter1)
    return dist == 0 or dist == 1

def is_abecedarian(word):
    index = 0
    while index < len(word) - 2:
        if not is_next(word[index], word[index + 1]):
            return False
        index = index + 1
    return True


print is_next('a','c')

print is_abecedarian('a')
print is_abecedarian('aabbcdefghijklmnooooopqrsttttttuvw')
