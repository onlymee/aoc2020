import numpy as np
from collections import defaultdict
#from bitstring import BitArray
import re


def parseFile(lines):
    points=set()
    for i,line in enumerate(lines):
        for j,ch in enumerate(line):
            if ch=="#": points.add((i,j,0))
    return points

vec=[]
for i in range(-1,2):
    for j in range(-1,2):
        for k in range(-1,2):
            if (i,j,k)!=(0,0,0): vec.append((i,j,k))

def findAdj(pnt):
    global vec
    (x,y,z)=pnt
    return set([(x+i,y+j,z+k) for (i,j,k) in vec])

def iterate(pnts):
    newpnts=set()
    inactivenb=set()

    for pnt in pnts:
        adj = findAdj(pnt)
        inactivenb=inactivenb.union(adj.difference(pnts))
        cnt=len(adj.intersection(pnts))
        if cnt==2 or cnt==3:
            newpnts.add(pnt)
    
    for pnt in inactivenb:
        adj = findAdj(pnt)
        cnt=len(adj.intersection(pnts))
        #print(pnt,cnt)
        if cnt == 3:
            newpnts.add(pnt)

    return newpnts

def printMap(pnts):
    (minx,miny,minz)=next(iter(pnts))
    (maxx,maxy,maxz)=next(iter(pnts))
    for (x,y,z) in pnts:
        if x>maxx:maxx=x
        if x<minx:minx=x
    miny=0
    maxy=0
    for (x,y,z) in pnts:
        if y>maxy:maxy=y
        if y<miny:miny=y
    minz=0
    maxz=0
    for (x,y,z) in pnts:
        if z>maxz:maxz=z
        if z<minz:minz=z
    
    for k in range(minz,maxz+1):
        print("\nz=",k)
        for i in range(minx,maxx+1):
            str=""
            for j in range(miny,maxy+1):
                if (i,j,k) in pnts:
                    str+="#"
                else:
                    str+="."
            print(str)




###########################################################################
filename='day17/input.txt'
input = open(filename,'r')
lines = input.read().splitlines()
input.close()

points=parseFile(lines)

pnts=points.copy()

printMap(pnts)
print("----------------")

test=iterate(iterate(pnts))
print (test)
printMap(test)

while i<7:
    pnts=iterate(pnts)
    i+=1

# Answer 1
answer1=len(pnts)

# Answer 2

answer2=-1

print(answer1,answer2)
