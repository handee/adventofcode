import fileinput


shop=[]
fighters=[]

class character:
   name=""
   weapon=""
   armour=""
   D=0 #damage
   A=0 #armour 
   ringone=""
   ringtwo=""
   numrings=0
   moneyspent=0
   hp=0
   initialhp=0
   def __str__(self):
       return "{} has weapon {}, armour {}, ring one{}, ring two {}, damage {} and armour{}".format(self.name,self.weapon,self.armour,self.ringone,self.ringtwo,self.D, self.A, self.hp)
   def __init__(self, name, hp, D, A):
       self.name=name
       self.hp=hp
       self.initialhp=hp
       self.D=D
       self.A=A
   def reset(self):
       self.hp=self.initialhp
   def buystuff(self, obj):
       if obj.objecttype=="Weapon":
          self.weapon=obj.name
          self.D+=obj.D
          self.A+=obj.A
          self.moneyspent+=obj.cost
       elif obj.objecttype=="Armour":
          self.armour=obj.name
          self.D+=obj.D
          self.A+=obj.A
          self.moneyspent+=obj.cost
       elif obj.objecttype=="Ring":
          if (self.numrings<2):
             if self.ringone=="":
                 self.ringone=obj.name
                 self.D+=obj.D
                 self.A+=obj.A
                 self.moneyspent+=obj.cost
                 self.numrings+=1
             else:
                 self.ringtwo=obj.name
                 self.D+=obj.D
                 self.A+=obj.A
                 self.moneyspent+=obj.cost
                 self.numrings+=1
          else: 
              print "can't add another ring."

   def sellstuff(self, obj):
       if obj.objecttype=="Weapon":
          self.weapon="" 
       elif obj.objecttype=="Armour": 
          self.armour=""
       elif obj.objecttype=="Ring":
          if (self.ringone==obj.name):
             self.ringone=self.ringtwo
          self.ringtwo=""
          self.numrings-=1
       self.D-=obj.D
       self.A-=obj.A
       self.moneyspent-=obj.cost

class obj:
   name=""
   D=0 #damage
   A=0 #armour  
   objecttype=""
   cost=0
   def __str__(self):
       return "{} is a {}, damage {} and armour{}, costing {}".format(self.name,self.objecttype,self.D, self.A, self.cost)



for line in fileinput.input(['shop.txt']):
   x=line.rstrip().split(' ')
   r=obj()
   if len(x)>2:
      if x[0]=="Weapons:":
          type_thing="Weapon"
      elif x[0]=="Armor:":
          type_thing="Armour"
      elif x[0]=="Rings:":
          type_thing="Ring"
      else:
         r.name=x[0] # name
         r.cost=int(x[1]) 
         r.D=int(x[2]) 
         r.A=int(x[3]) 
         r.objecttype=type_thing
         shop.append(r)

def fight(chars):
   i=0
   j=1
   finished=False
   # i attacks j 
   while not finished:
      wounding=chars[i].D-chars[j].A
      if (wounding>0):
         chars[j].hp-=wounding
      else:
         chars[j].hp-=1
      if (chars[j].hp<=0):
         print "{} just beat {} having spent {}, the loser spent {}".format(chars[i].name,chars[j].name,chars[i].moneyspent,chars[j].moneyspent)
#for part 1, if the player wins, return the amount of money they've spent and 
#a big number if they didn't win
     #    if chars[i].name=="Hannah":
     #        return chars[i].moneyspent 
     #    else :
     #        return 9999999 

#for part 2, if the player doesn't win, return the amount of money they've 
# spent and zero if they did win
         if chars[j].name=="Hannah":
             return chars[j].moneyspent 
         else :
             return 0
         finished=True
      k=i
      i=j
      j=k
    

me=character("Hannah", 100, 0,0)
boss=character("Monster", 103, 9, 2)
fighters.append(me)
fighters.append(boss)
fight(fighters)

fightcosts=[]

for i in range(0,5): #weapons
#first just the weapon
   me.buystuff(shop[i])
   me.reset()
   boss.reset()
   fightcosts.append(fight(fighters))
   for j in range(5,10): #armour
#then the weapon and the armor
      me.buystuff(shop[j])
      me.reset()
      boss.reset()
      fightcosts.append(fight(fighters))
      for k in range(10,16): #rings of power
          me.buystuff(shop[k])
          me.reset()
          boss.reset()
          fightcosts.append(fight(fighters))
          for l in range(k+1,16):#can have more than one ring
             me.buystuff(shop[l])
             me.reset()
             boss.reset()
             fightcosts.append(fight(fighters))
             me.sellstuff(shop[l])
          me.sellstuff(shop[k]) 
      me.sellstuff(shop[j])
   me.sellstuff(shop[i])

#print min(fightcosts)  #part 1
print max(fightcosts)
