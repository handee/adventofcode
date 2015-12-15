import fileinput

num=0
ings=[]
class ingredient:
   name=""
   capacity=0
   durability=0
   flavour=0
   texture=0
   calories=0
   def __str__(self):
       return "{} has capacity {}, durability {}, flavour {}, texture {}, and calories {}".format(self.name,self.capacity,self.durability,self.flavour,self.texture,self.calories)


for line in fileinput.input(['input.txt']):
   x=line.rstrip().split(' ')
   r=ingredient()
   r.name=x[0][:-1] # name
   r.capacity=int(x[2][:-1]) #not a dodgy smiley,
   r.durability=int(x[4][:-1]) #just a means of taking
   r.flavour=int(x[6][:-1]) #the last character off 
   r.texture=int(x[8][:-1]) #a string losing the ,
   r.calories=int(x[10])
   ings.append(r)

score=0
max_score=0   
desc=""
for i in range(0,100):
    for j in range (0,100-i):
       for k in range (0,100-i-j):
            l=100-i-j-k
            cap=ings[0].capacity*i+ings[1].capacity*j+ings[2].capacity*k+ings[3].capacity*l
            dur=ings[0].durability*i+ings[1].durability*j+ings[2].durability*k+ings[3].durability*l
            fla=ings[0].flavour*i+ings[1].flavour*j+ings[2].flavour*k+ings[3].flavour*l
            tex=ings[0].texture*i+ings[1].texture*j+ings[2].texture*k+ings[3].texture*l
            cals=ings[0].calories*i+ings[1].calories*j+ings[2].calories*k+ings[3].calories*l
 # part 2 just add the cals into the <=0 calculation
            if (cap<=0 or dur<=0 or fla<=0 or tex<=0 or cals !=500):
                score=0
            else: 
                score=fla*cap*tex*dur
            if (score>max_score):
                max_score=score
                desc="{} {} {} {} {} {} {} {}".format(ings[0].name,i,ings[1].name,j,ings[2].name,k,ings[3].name,l)


print max_score
print desc
