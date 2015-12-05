import re
import fileinput
#part 1


def contains3vowels(string):
   vowels=string.count('a')+string.count('e')+string.count('i')+string.count('o')+string.count('u')
   if vowels>=3:
      return True 
   else:
      return False 

def isnaughty(string):
   if (string.find("xy")>=0):
       return True 
   if (string.find("pq")>=0):
       return True 
   if (string.find("ab")>=0):
       return True 
   if (string.find("cd")>=0):
       return True 
   return False 

def doubleletters(string):
   p=re.compile(r'([a-zA-Z])\1')
   a=p.search(string)
   if (a):
      return True 
   else: 
      return False 

def hasrepeatedsubstringpair(string):
   p=re.compile(r'([a-zA-Z][a-zA-z]).*\1')
   a=p.search(string)
   if (a):
      return True 
   else: 
      return False 

def haspalindrome(string):
   p=re.compile(r'([a-zA-Z]).\1')
   a=p.search(string)
   if (a):
      return True 
   else: 
      return False 

nice=0
nice2=0
counter=0
for line in fileinput.input(['input.txt']):
    counter=counter+1
    if not isnaughty(line):
      if contains3vowels(line) and doubleletters(line): 
         nice+=1 
    if hasrepeatedsubstringpair(line) and haspalindrome(line):
      nice2+=1
print ("firstpart:", nice)
print ("secondpart:", nice2)
 
