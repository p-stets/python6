'''
Написать программу, которая выводит саму себя задом наперед
'''

import sys

filename = sys.argv[0]

f = open(filename, 'r')

file = []

for i in f:
    file.append(i)

for i in range(len(file) - 1, -1, -1):
    print(file[i], end='')

f.close()
