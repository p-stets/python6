'''
Написать программу, которая выводит саму себя
'''

import sys

filename = sys.argv[0]

f = open(filename, 'r')

for i in f:
    print(i, end='')

f.close()
