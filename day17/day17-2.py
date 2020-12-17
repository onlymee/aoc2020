import numpy as np
from collections import defaultdict
#from bitstring import BitArray
import re


def parseFile(lines):
    points=set()
    for i,line in enumerate(lines):
        for j,ch in enumerate(line):
            if ch=="#": points.add((i,j,0,0))
    return points

vec=[]
for i in range(-1,2):
    for j in range(-1,2):
        for k in range(-1,2):
          for l in range(-1,2):
            if (i,j,k,l)!=(0,0,0,0): vec.append((i,j,k,l))

def findAdj(pnt):
    global vec
    (x,y,z,w)=pnt
    return set([(x+i,y+j,z+k,w+l) for (i,j,k,l) in vec])

def iterate(pnts):
    alive=set()
    dead=set()
    inactivenb=set()

    for pnt in pnts:
        adj = findAdj(pnt)
        inactivenb=inactivenb.union(adj.difference(pnts))
        cnt=len(adj.intersection(pnts))
        if cnt!=2 and cnt!=3:
            dead.add(pnt)
    
    for pnt in inactivenb:
        adj = findAdj(pnt)
        cnt=len(adj.intersection(pnts))
        #print(pnt,cnt)
        if cnt == 3:
            alive.add(pnt)

    pnts.difference_update(dead)
    return pnts.union(alive)

def printMap(pnts):
    (minx,miny,minz,minw)=next(iter(pnts))
    (maxx,maxy,maxz,maxw)=next(iter(pnts))
    activelayer=set()
    for (x,y,z,w) in pnts:
        if x>maxx:maxx=x
        if x<minx:minx=x
        if y>maxy:maxy=y
        if y<miny:miny=y
        if z>maxz:maxz=z
        if z<minz:minz=z
        if w>maxw:maxw=w
        if w<miny:miny=w
        activelayer.add((z,w))
    
    for l in range(minw,maxw+1):
        for k in range(minz,maxz+1):
            if (k,l) not in activelayer: continue
            print("\nz=",k, "w=",l)
            for i in range(minx,maxx+1):
                str=""
                for j in range(miny,maxy+1):
                    if (i,j,k,l) in pnts:
                        str+="#"
                    else:
                        str+="."
                print(str)

###########################################################################
filename='day17/input.txt'
input = open(filename,'r')
lines = input.read().splitlines()
input.close()

pnts=parseFile(lines)

printMap(pnts)

for i in range(6):
    pnts=iterate(pnts)

# Answer 1
answer2=len(pnts)


print(answer2)
