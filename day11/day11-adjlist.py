import numpy as np

def onMap(point,dims):
    return (point[0]>=0 and point[1]>=0 and point[0]<dims[0] and point[1]<dims[1])

def findAdj(mp,seat):
    adjacent=[]
    vec=[(-1,0),(0,-1),(1,0),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
    for v in vec:
        point=(seat[0]+v[0],seat[1]+v[1])
        if point in mp:
            adjacent.append(point)
    return adjacent

def findAdjLos(mp,dims,seat):
    adjacent=[]
    vec=[(-1,0),(0,-1),(1,0),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
    rays={i:seat for i in vec}
    while len(rays)>0:
        pnts=list(rays.keys())
        for s in pnts:
            rays[s]=(rays[s][0]+s[0],rays[s][1]+s[1])
            if not onMap(rays[s],dims):
                del rays[s]
                continue
            if rays[s] in mp:
                adjacent.append(rays[s])
                del rays[s]
    return adjacent

def iterate(occMap,adjMap,maxNb):
    newOccMap={}
    occ=0
    chg=0
    for seat in occMap:
        nb=0
        for neighbour in adjMap[seat]:
            if occMap[neighbour]=='#': nb+=1
        if nb>=maxNb:
            newOccMap[seat]='L'
        elif nb==0:
            newOccMap[seat]='#'
        else:
            newOccMap[seat]=occMap[seat]
        if newOccMap[seat]=='#': occ+=1
        if newOccMap[seat]!=occMap[seat]: chg+=1
    return (occ,chg,newOccMap)


def printMap(occMap,h,w):
    for i in range(h):
        row=""
        for j in range(w):
            if (i,j) in occMap: 
                row+=occMap[(i,j)]
            else:
                row+='.'
        print(row)

def getOccMap(mp):
    seats={}
    for i,row in enumerate(mp):
        for j,seat in enumerate(row):
            if mp[i][j] in "#L": seats[(i,j)]=mp[i][j]
    return seats


def getAnswer(occMap,adjMap,maxNb):
    occ=-1
    i=0
    while True:
        (occ,chg,occMap)=iterate(occMap,adjMap,maxNb)
        if chg==0: break
        i+=1
    return occ

filename='day11/input.txt'
input = open(filename,'r')
lines = input.read().splitlines()
input.close()

dims=(len(lines), len(lines[0]))

occMap=getOccMap(lines)
adjMap1={seat: findAdj   (occMap.keys(),seat) for seat in occMap}
adjMap2={seat: findAdjLos(occMap.keys(),dims,seat) for seat in occMap}

answer1=getAnswer(occMap,adjMap1,4)
answer2=getAnswer(occMap,adjMap2,5)

print(answer1,answer2)
