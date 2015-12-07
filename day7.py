
import fileinput
import numpy as np

D= {}
links=[]
for line in fileinput.input(['input.txt']):
   x=line.rstrip().split(' ')
   links.append(x);
links.sort()
print (links)
ND= {}
counter=0
empty=True

while (len(links)>0):
   x=links.pop(0)
   print ( x, 'line: ' , counter)
   if ('LSHIFT' in x):
	 v1=x[0]
	 index=np.uint16(x[2])
	 output=x[4]
	 if D.has_key(v1):
            print("setting ", output,"to a key");
	    D[output]=D[v1]<<index
	 else: 
	    links.append(x)
   elif ('RSHIFT' in x):
	 v1=x[0]
	 index=np.uint16(x[2])
	 output=x[4]
	 if D.has_key(v1):
            print("setting ", output,"to a key");
	    D[output]=D[v1]>>index
	 else: 
	    links.append(x)
   elif ('AND' in x):
	 v1=x[0]
	 v2=x[2]
	 output=x[4]
	 if D.has_key(v1) and D.has_key(v2):
	     print("setting ", output,"to a key");
	     D[output]=D[v1] & D[v2]
	 elif (v1.isdigit() and D.has_key(v2)):
	     print("setting ", output,"to a key");
	     D[output]=np.uint16(v1) & D[v2]
	 elif (v2.isdigit() and D.has_key(v1)):
	     print("setting ", output,"to a key");
	     D[output]=D[v1] & np.uint16(v2)
	 else: 
	    links.append(x)
   elif ('OR' in x):
	 v1=x[0]
	 v2=x[2]
	 output=x[4]
	 if D.has_key(v1) and D.has_key(v2):
	    print("setting ", output,"to a key");
	    D[output]=D[v1] | D[v2]
	 elif (v1.isdigit() and D.has_key(v2)):
	    print("setting ", output,"to a key");
	    D[output]=np.uint16(v1) | D[v2]
	 elif (v2.isdigit() and D.has_key(v1)):
	    print("setting ", output,"to a key");
	    D[output]=D[v1] | np.uint16(v2)
	 else: 
	    links.append(x)
   elif ('NOT' in x):
	 v1=x[1]
	 output=x[3]
	 if D.has_key(v1):
	    print("setting ", output,"to a key");
	    D[output]= ~D[v1]
	 else: 
	    links.append(x)
   else:
	 v1=x[0]
	 output=x[2]
	 if (v1.isdigit()):
	    output=x[2]
	    print("setting ", output,"to a key");
	    D[output]=np.uint16(v1)
	 else:
	    if D.has_key(v1):
	       print("setting ", output,"to a key");
	       D[output]=D[v1] 
	    else: 
	       links.append(x)

   counter+=1 
   print (D)
   print (len(links))





