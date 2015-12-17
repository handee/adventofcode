import fileinput
import itertools 
import numpy as np

c=[]
for line in fileinput.input(['input.txt']):
    c.append(int(line.rstrip()))

c.sort()
max_size=c[-1]
min_size=c[0]

print min_size
print max_size
print c
