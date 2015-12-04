import hashlib

#part 1
mykey="iwrupvqb"

i=0
while 1:
   current=mykey+str(i)
   s=hashlib.md5(current).hexdigest()
   if (s[0]=='0') and (s[1]=='0') and (s[2]=='0') and (s[3]=='0') and (s[4]=='0'):  
      print i
#part1 
      print "has 5 leading zeroes"
      if (s[5]=='0'): 
         print i
#part2 
         print "has 6 leading zeroes"
         break

   i+=1
