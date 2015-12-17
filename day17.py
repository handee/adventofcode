import fileinput
import itertools 
import numpy as np
eggnog=150
c=[]
for line in fileinput.input(['input.txt']):
    c.append(int(line.rstrip()))

c.sort()
max_size=c[-1]
min_size=c[0]
print "we have {} containers".format(len(c))
print "the smallest is {} and the largest is {}".format(min_size, max_size)

largestnumberofcontainers=0
smallestnumberofcontainers=0
volume=0
print "let's bound the problem a bit (before we bruteforce it)"
print "by excluding those which deffo add up to more than {} ".format(eggnog)
for i in range(0,len(c)):
    volume+=c[i]
    if volume>eggnog: 
       largestnumberofcontainers=i
       break
volume=0
i=len(c)-1
while i > 0 :
    volume+=c[i]
    if volume>eggnog: 
       smallestnumberofcontainers=i 
       break
    i=i-1
smallestnumberofcontainers=len(c)-smallestnumberofcontainers
print "so we need between {} and {} containers...".format(smallestnumberofcontainers,largestnumberofcontainers)

total_appropriate_container_combos=0
for i in range(smallestnumberofcontainers,largestnumberofcontainers):
    y=itertools.combinations(c,i)
    for j in list(y):
        if sum(j)==eggnog:
            print j
            print sum(j)
            total_appropriate_container_combos+=1

print "so we have {}".format(total_appropriate_container_combos)
