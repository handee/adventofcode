import fileinput
import numpy as np
import itertools

d={} # dictionary to keep track of individual locations
dist=[]

locations=0
for line in fileinput.input(['input.txt']):
   #set up a dictionary (name-matrix index)
   #and find out how many destinations we're dealing with
   x=line.rstrip().split(' ')
   if not d.has_key(x[0]) :
       d[x[0]]=locations
       locations+=1
   if not d.has_key(x[2]) :
       d[x[2]]=locations
       locations+=1
   dist.append(x)

#array to hold distances between individual locations
#a=np.zeros([locations,locations],int)
#for line in fileinput.input(['input.txt']):
#   x=line.rstrip().split(' ')
#   a[d[x[0]]][d[x[2]]]=int(x[4])
#although maybe that's a pants idea?


r={}
p= itertools.permutations(list(d.keys()))
#print(list(p))
lengths={}
shortest=9999999999999
longest=0
for route in p:
   length=0
   strroute=route[0]
   for j in range(1,len(route)):
      for k in range(0,len(dist)):
          if (route[j] in dist[k]):
              if (route[j-1] in dist[k]):
                 strroute+=route[j]
                 length+=int(dist[k][4])
   if (length<shortest):
       shortest=length
       shortestroute=strroute
   if (length>longest):
       longest=length
       longestroute=strroute
   lengths[strroute]=length
print ("shortest: ", shortestroute, shortest)
print ("longest: ", longestroute, longest) 
