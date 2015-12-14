import fileinput

num=0
reindeerinfo=[]
#hacky hacky hack yes i should have used a "reindeer" class
#maybe i'll refactor it later.

for line in fileinput.input(['input.txt']):
   r=[]
   x=line.rstrip().split(' ')
   r.append(x[0]) # name
   r.append(int(x[3])) # speed
   r.append(int(x[6])) # flight time 
   r.append(int(x[13])) # rest time 
   r.append(0) # totaltravelled 
   r.append(True) # currentlytravelling 
   r.append(0) # stopped travelling 
   r.append(0) # started travelling 
   r.append(0) # in the lead points 
   reindeerinfo.append(r)


totalsecs=2503
for t in range(0,totalsecs):
   counter=0
   leadingreindeerdist=0
   for r in reindeerinfo:
      if r[5]:
         if (t-r[7])>=r[2]: #if you've been flying for too long
            r[5]=False
            r[6]=t
         else:
            r[4]+=r[1] #update currently travelling with the seconds travelled
      else:
         if (t-r[6])>=r[3]: #if you've rested long enough
            r[5]=True
            r[7]=t
            r[4]+=r[1] #update currently travelling with the seconds travelled
      if (r[4]>leadingreindeerdist):
         leadingreindeerdist=r[4]
      reindeerinfo[counter]=r
      counter+=1
   counter=0
   for r in reindeerinfo:
      if r[4]==leadingreindeerdist: #this is the leading reindeer! have a point
         reindeerinfo[counter][8]+=1 
      counter+=1

leadingreindeerdist=0
maxpoints=0
counter=0 
for r in reindeerinfo:
   if (r[8]>maxpoints):
     maxpoints=r[8]
     pointyreindeer=counter
   if (r[4]>leadingreindeerdist):
     leadingreindeerdist=r[4]
     farthestreindeer=counter
   counter+=1

print(reindeerinfo[farthestreindeer][0], "went farthest, going ",leadingreindeerdist)
print(reindeerinfo[pointyreindeer][0], "got the most points, which is ",maxpoints)
       
