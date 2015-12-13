import fileinput
import itertools 
import numpy as np
from collections import Counter

rough_input=[]
names={}
num=0

## calculate total happiness change
def THC(seating, costs): #seating is a list of numbers indicating
         # the order of seats around the table, costs is a matrix
   thc=costs[seating[0]][seating[len(seating)-1]] #wrap around
   thc+=costs[seating[len(seating)-1]][seating[0]] #wrap around
   for seat in range(0,len(seating)-1):
      thc+=costs[seating[seat]][seating[seat+1]]
      thc+=costs[seating[seat+1]][seating[seat]]
   return thc

for line in fileinput.input(['input.txt']):
   x=line.rstrip().split(' ')
   x[10]=x[10][:-1] #strip last char from the last name ('.')
   if (x[2]=="lose"): #make losing happiness == a negative no.
      number=-int(x[3])
   else:
      number=int(x[3])
   rough_input.append([x[0],number,x[10]])
   if not names.has_key(x[0]):
      names[x[0]]=num
      num+=1


#for part 2 i just make the zeroes matrix one bigger
costs=np.zeros((num+1,num+1),int)

#for part 2 i add my name because, why not? 
names["Hannah"]=num

for entry in rough_input:
   costs[names[entry[0]],names[entry[2]]]=entry[1]
#for part 2 i just make the number of people one bigger
p= itertools.permutations(range(0,num+1))
maxhappy=-1000
for i in list(p):
   happy=THC(i,costs)
   if happy>maxhappy:
      maxhappy=happy
      best=i
print("best solution, yeahright")
print maxhappy 
print best 
print names
print costs
