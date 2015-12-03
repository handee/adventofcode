import fileinput

paper=0
ribbon=0
for line in fileinput.input(['input.txt']):
    w,h,l=line.split('x')
    w=int(w)
    h=int(h)
    l=int(l)
#part1
    currentpaper=2*l*w+2*w*h+2*h*l 
    side1=w*h
    side2=h*l
    side3=l*w
    sides=[side1,side2,side3]
    smallest=min(sides)
    paper=paper+currentpaper+smallest
#part2
    volume=w*h*l
    perimetersides=[w+w+h+h,h+h+l+l,w+w+l+l]
    smallestperim=min(perimetersides)
    ribbon=ribbon+volume+smallestperim

print paper
print ribbon 

