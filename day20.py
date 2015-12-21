import numpy as np
#part1
finish=34000000 #biggest it's gonna be, probably
npresents=np.full((finish),10,int)
print max(npresents)
for i in range(2,finish/10):
   npresents[i::i]+=10*i
for i in range(2,finish/10):
   if npresents[i]>finish:
      print i
      print npresents[i]
      break

#part2
finish=34000000 #gosh it might need to be bigger than that 
npresents2=np.full((finish),11,int)
print max(npresents2)
for i in range(2,finish/11):
   npresents2[i:50*i:i]+=11*i
for i in range(2,finish/11):
   if npresents2[i]>finish:
      print i
      print npresents2[i]
      break


