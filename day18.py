import fileinput
import numpy as np
import cv2 
import re

#part1
#big 2d array of zeroes to be our lights
w=100;
h=100;
grid=np.zeros((w+2,h+2),int)  # lets have it a bit bigger so we can pad with 0
oldgrid=np.zeros((w+2,h+2),int)  # lets have it a bit bigger so we can pad with 0
grid2=np.zeros((w+2,h+2),int)  # lets have it a bit bigger so we can pad with 0
oldgrid2=np.zeros((w+2,h+2),int)  # lets have it a bit bigger so we can pad with 0
crowdthresh=3
starvethresh=2

           
  

def canlive(x,y,grid):
   global w
   global h
   neighboursum=0
   for i in range(x-1,x+2):
      for j in range(y-1,y+2):
          neighboursum+=grid[i][j]
   neighboursum-=grid[x][y] #take into account value at x-y, 
     #if it's zero it won't affect it but if it's 
     #1 we'll have as sum that's 1 too many
   print "ns={} x={} y={}".format(neighboursum,x,y)
   if neighboursum>crowdthresh:
       return 0
   elif neighboursum==crowdthresh:
       return 1
   elif neighboursum>=starvethresh and grid[x][y]==1:
       return 1
   else:
       return 0
   

counter=1
current=1
for line in fileinput.input(['input.txt']):
    line=line.rstrip() 
    current=1
    for i in line:
        if i=='#':
           grid[counter][current]=1
        else:
           grid[counter][current]=0
        current+=1
    counter+=1

   
c=0
im=np.zeros(((5*w)+2,(5*h)+2, 3),np.uint8)
im2=np.zeros(((5*w)+2,(5*h)+2, 3),np.uint8)
grid2=np.copy(grid)
for frame in range(0,100):
   im[:]=0
   im2[:]=0
   oldgrid=np.copy(grid)
   oldgrid2=np.copy(grid2)
   for xcount in range (1,w+1):
       for ycount in range (1,h+1):
          #blank out the edge rows
	   oldgrid[:,0]=0
	   oldgrid[:,h+1]=0
	   oldgrid[0,:]=0
	   oldgrid[w+1,:]=0
           grid[xcount][ycount]=canlive(xcount,ycount,oldgrid) 
          #part II blank out the edge rows and light up the corners
	   oldgrid2[:,0]=0
	   oldgrid2[:,h+1]=0
	   oldgrid2[0,:]=0
	   oldgrid2[w+1,:]=0
	   oldgrid2[1,1]=1
	   oldgrid2[w,h]=1
	   oldgrid2[1,h]=1
	   oldgrid2[w,1]=1
           grid2[xcount,ycount]=canlive(xcount,ycount,oldgrid2)
          #part II light up the corners again because they're stuck on
	   grid2[1,1]=1
	   grid2[w,h]=1
	   grid2[1,h]=1
	   grid2[w,1]=1
           #let's draw it because wth not
           if (xcount==w):
              print "on the edge, ycount = {} grid2= {}".format(ycount,grid2[xcount,ycount])
           if grid[xcount][ycount]==1:
              cv2.circle(im,(xcount*5,ycount*5),4,(0,255,0),-1) 
           if grid2[xcount][ycount]==1:
              cv2.circle(im2,(xcount*5,ycount*5),4,(0,0,255),-1) 
   fn="/tmp/frame_{:04d}.png".format(c)
   fn2="/tmp/frame2_{:04d}.png".format(c)
   cv2.imwrite(fn,im)
   cv2.imwrite(fn2,im2)
   c+=1

print np.sum(grid)
print np.sum(grid2)
