from collections import defaultdict

###########################################################################
filename='day24/input.txt'
input = open(filename,'r')
lines = input.read().splitlines()
input.close()

def getAdj(pnt):
    (r,c)=pnt
    return [(r,  c+1),
            (r,  c-1),
            (r-1,c  ),
            (r-1,c+1),
            (r+1,c-1),
            (r+1,c )]


#tiles=defaultdict(bool)
black=set()
for j,line in enumerate(lines):
    posc=0
    posr=0
    i=0
    #print(line)
    while i<len(line):
        if line[i] in "ns":
            if line[i:i+2]=="nw":
                posr-=1
            if line[i:i+2]=="ne":
                posc+=1
                posr-=1
            if line[i:i+2]=="sw":
                posc-=1
                posr+=1
            if line[i:i+2]=="se":
                posr+=1
            i+=2
        else:
            if line[i]=="w":
                posc=posc-1
            if line[i]=="e":
                posc=posc+1
            i+=1
    pnt=(posc,posr)
    if pnt in black:
        black.remove(pnt)
    else:
        black.add(pnt)

# Answer 1
answer1=len(black)

# Answer 2
j=0
while j<100:
    j+=1
    live=set()
    points=list(black)
    for pnt in black:
        points.extend(getAdj(pnt))
    points=set(points)
    for pnt in points:
        adj=getAdj(pnt)
        bcount=len(black.intersection(adj))
        if bcount==2 or (bcount==1 and pnt in black):
            live.add(pnt)
    black=live
       

answer2=len(black)

print(answer1,answer2)
