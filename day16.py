import fileinput

num=0
ings=[]
class aunt:
   name="Sue"
   def __init__(self):
      self.props={}
      self.props["number"]=-1
      self.props["children"]=-1
      self.props["cats"]=-1
      self.props["samoyeds"]=-1
      self.props["pomeranians"]=-1
      self.props["akitas"]=-1
      self.props["vizslas"]=-1
      self.props["goldfish"]=-1
      self.props["trees"]=-1
      self.props["cars"]=-1
      self.props["perfumes"]=-1
   def __str__(self):
       return "SUE number {} ".format(self.number)
   def add_to_aunt(self,value,name):
       self.props[name]=value 
   def difference(self,othersue):
       currendiff=0;
       for key in self.props:
          if (othersue.props[key]>=0):
             # part 2 additional lines
             if (key=="cats" or key=="trees"):
                # for cats and trees, if othersue is bigger than
                # current reading it's good so we only want to record
                # smaller values. 
                if (self.props[key]>=othersue.props[key]):
                   currendiff+=abs(self.props[key]-othersue.props[key])
             elif (key=="pomeranians" or key=="goldfish"):
                # for pomeranians and goldfish, it's the opposite 
                if (self.props[key]<=othersue.props[key]):
                   currendiff+=abs(self.props[key]-othersue.props[key])
             else:
             #end of part 2 additional lines
                currendiff+=abs(othersue.props[key]-self.props[key])
       return currendiff    


sue=aunt()
sue.add_to_aunt(3,"children")
sue.add_to_aunt(7,"cats")
sue.add_to_aunt(2,"samoyeds")
sue.add_to_aunt(3,"pomeranians")
sue.add_to_aunt(0,"akitas")
sue.add_to_aunt(0, "vizslas")
sue.add_to_aunt(5,"goldfish")
sue.add_to_aunt(3, "trees")
sue.add_to_aunt(2, "cars")
sue.add_to_aunt(1, "perfumes")

aunts=[]
for line in fileinput.input(['input.txt']):
   x=line.rstrip().split(' ')
   r=aunt()
   r.number=x[1][:-1] # name
   thing1=int(x[3][:-1]) #not a dodgy smiley,
   thing2=int(x[5][:-1]) #just a means of taking off the ,
   thing3=int(x[7])
   r.add_to_aunt(thing1,x[2][:-1])
   r.add_to_aunt(thing2,x[4][:-1])
   r.add_to_aunt(thing3,x[6][:-1])
   aunts.append(r)

bestsue=-1
min_score=99999999999999999   
for auntie in aunts:
   if sue.difference(auntie)<min_score:
      min_score=sue.difference(auntie)
      bestsue=auntie.number

print min_score
print bestsue
