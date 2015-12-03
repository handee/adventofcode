import fileinput
import numpy as np

f=open('input.txt','r');
a=f.read()
m=len(a)
print(m)
#part1
#big 2d array of zeroes to be our big map
bigmap=np.zeros((2*m,2*m),int) # twice the input length is plenty big
x=m; #start in the middle
y=m;
bigmap[x,y]+=1 #increment starting position

for d in a:
    # move the current location
    if (d=='v'):
       y-=1
    if (d=='>'):
       x+=1
    if (d=='<'):
       x-=1
    if (d=='^'):
       y+=1
   # increment cell at current location
    bigmap[x,y]+=1

houses_visited=np.count_nonzero(bigmap)
print (houses_visited)

#part2 
bigmap.fill(0) # zero that array 
x=m; #start in the middle
y=m;
rx=m; # robotsanta also starts in middle
ry=m;
bigmap[x,y]+=2 #increment starting position
santa=1;
for d in a:
    if (santa==1) :
# move the current location of santa
       if (d=='v'):
          y-=1
       if (d=='>'):
          x+=1
       if (d=='<'):
          x-=1
       if (d=='^'):
          y+=1
   # increment cell at current location
       bigmap[x,y]+=1
       santa=0
    else:
# move the current location of robot santa
       if (d=='v'):
          ry-=1
       if (d=='>'):
          rx+=1
       if (d=='<'):
          rx-=1
       if (d=='^'):
          ry+=1
   # increment cell at current location
       bigmap[rx,ry]+=1
       santa=1

houses_visited=np.count_nonzero(bigmap)
print (houses_visited)
