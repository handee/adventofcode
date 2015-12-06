import fileinput
import numpy as np
import cv2 
import re

#part1
#big 2d array of zeroes to be our lights
w=1000;
h=1000;
lights=np.zeros((w,h),int) 


def turnon(x1,y1,x2,y2):
   x2+=1
   y2+=1
   for x in range (x1,x2):
      for y in range (y1,y2):
          lights[x,y]+=1

def turnoff(x1,y1,x2,y2):
   x2+=1
   y2+=1
   for x in range (x1,x2):
      for y in range (y1,y2):
          lights[x,y]-=1
          if (lights[x,y]<0):
             lights[x,y]=0

def toggle(x1,y1,x2,y2):
   x2+=1
   y2+=1 
   for x in range (x1,x2):
      for y in range (y1,y2):
          lights[x,y]+=2 



counter=0
for line in fileinput.input(['input.txt']):
    match= re.findall(r'([^0-9]+)+([0-9]+),([0-9]+)[^0-9]+([0-9]+),([0-9]+)', line)
    command= match[0][0]
    x1=int(match[0][1])
    y1=int(match[0][2])
    x2=int(match[0][3])
    y2=int(match[0][4])
    if x1>=x2 or y1>=y2:
       print "santa you're an arse"
    if (command=="turn on "):
       print(x1, y1, x2, y2)
       turnon(x1,y1,x2,y2)
    if (command=="turn off "):
       print(x1, y1, x2, y2)
       turnoff(x1,y1,x2,y2)
    if (command=="toggle "):
       print(x1, y1, x2, y2)
       toggle(x1,y1,x2,y2)
    counter+=1

print np.sum(lights)
cv2.imwrite("/tmp/lights.png",lights)
