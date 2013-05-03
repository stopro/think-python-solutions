#!/usr/bin/pythonsnnnnn

import time

def append_method():
    result = []
    fin = open('words.txt')
    before = time.time()
    for line in fin:
        result.append(line.strip())
    after = time.time()
#    print 'append time costs:', after - before
    fin.close()
    return result 

def idiom_method():
    result = []
    fin = open('words.txt')
    before = time.time()
    for line in fin:
        result = result + [line]
    after = time.time()
    print '+[x] time costs:', after - before
    fin.close()
    return result 
    
#append_method()
#idiom_method()
