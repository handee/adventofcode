import fileinput
import re 
from copy import deepcopy


D= {}
for line in fileinput.input(['input.txt']):
   x=line.rstrip().split(' ')
   if len(x)>1:
        if x[0] in D.keys():
            D[x[0]].append(x[2]) 
        else:
            D[x[0]]=[x[2]]
   else:
        molecule=x[0]


#let us do it backwards. start with greedy - subs shorter strings into 
# molecule.
def try_greedy():
   global D # dictionary of transformations
   newmolecules={}
   newermolecules={}
   newmolecules[molecule]=0 # initialise our newmolecules with the current mol
   done=False
   totalsubs=0
   while not done:
      totalsubs+=1
      for molkey in newmolecules: 
          biggest=0
          sub=""
          translation=""
          loc=-1
          for key in D:
             translist=D[key]
             for trans in translist:
	         x=[matches.start() for matches in re.finditer(trans,molkey)]
                 if len(x)>0: #if we have found  a match
                     if (len(trans)>biggest):
                         biggest=len(trans)
                         sub=key
                         translation=trans
                         loc=x
	  print "loc = {}".format(loc)
          if (loc>=0):
              for i in loc: 
                 print "subbing {} for {} at {}".format(sub,translation, i)
                 newmolecule=molkey[0:i]+sub+molkey[i+biggest:]
                 print len(newmolecule)
                 if (newmolecule=="e"):
                     done=True
                     print "*******{}********".format(totalsubs)
                 newermolecules[newmolecule]=totalsubs
      newmolecules.clear()
      newmolecules=deepcopy(newermolecules)
      newermolecules.clear()
      print "we now have {} new molecules and are on iteration {}".format(len(newmolecules), totalsubs)

       

try_greedy()



