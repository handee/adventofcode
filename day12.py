import fileinput
import json 
import re 

#
# part1
for line in fileinput.input(['input.txt']):
      nos=re.findall(r'-*[0-9]+',line)
total=0
for i in nos:
   total+=int(i)
print total

#part2 bollx i'm going to have to parse it after all
noredtotal=0
def unpack(i):
   global noredtotal
   if type(i) is dict:
       if "red" in i.values():
          print "red!!"
       else: 
          for key in i:
             unpack(i[key])
   elif type(i) is list:
       for element in i:
           unpack(element)
   elif type(i) is int: 
      noredtotal+=i


decoded = json.loads(line)
noredtotal=0
unpack(decoded)
print noredtotal
