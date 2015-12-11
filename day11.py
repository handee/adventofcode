import re
import fileinput
#part 1


def incrementstring(string):
    charpos=len(string)-1 
    slist=list(string)
    done=False
    while not done:
       if (slist[charpos]=='z'):
          #if the char's a z, make it an a and look at the prev char
          slist[charpos]='a'   
          charpos-=1
       else:
          ascival=ord(slist[charpos])
          slist[charpos]=chr(ascival+1)
          done=True
    a =''.join(slist)
    return a 
          

def confusing(string):
   if 'i' in string:
      return True
   elif 'o' in string:
      return True 
   elif 'l' in string:
      return True 
   else:
      return False 

def pairofdoubleletters(string):
   p=re.compile(r'([a-z])\1.*([a-z])\2')
   a=p.search(string)
   if (a):
      return True 
   else: 
      return False 

def increasingsequence(string):
    slist=list(string)
    for charpos in range(0,len(string)-3):
       ascival=ord(slist[charpos])
       if (ord(slist[charpos+1])==ascival+1):
          if (ord(slist[charpos+2])==ascival+2):
              return True 
    return False 
       
          


out="cqjxxyzz"
newpassword=False
while (newpassword==False):
   out = incrementstring(out)
   if (not confusing(out)) and (pairofdoubleletters(out)) and (increasingsequence(out)):
      newpassword=True

print out 
