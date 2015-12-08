import fileinput
import re 

counter=0
counter2=0
for line in fileinput.input(['input.txt']):
   x=line.rstrip()
   b=eval(x)
   c=re.escape(x)
   print(c)
   counter=counter+(len(x)-len(b))
   counter2=counter2+(len(c)-len(x)+2) #plus two for the quotes

print counter
print counter2
