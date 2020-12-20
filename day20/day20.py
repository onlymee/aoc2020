import numpy as np
from collections import defaultdict
#from bitstring import BitArray
import re


def rotate(l, n):
    #n=n%4
    #if n==0: return l
    #if n<4: 
    return l[-n:] + l[:-n]
    #return l[-(n-4)::-1] + l[:-(n-4):-1]

def rotateMapOnly(l,n):
    n=n%4
    if n==0: return l
    if n==3:
        newmap=[]
        for c in range(len(l[0])-1,-1,-1):
            newmap.append(''.join([l[r][c] for r in range(len(l))]))
        return newmap
    if n==2:
        newmap=[]
        for r in range(len(l)-1,-1,-1):
            newmap.append(l[r][::-1])
        return newmap
    if n==1:
        newmap=[]
        for c in range(len(l[0])):
            newmap.append(''.join([l[r][c] for r in range(len(l)-1,-1,-1)]))
        return newmap

def flipMap(l):
    newmap=[]
    for line in l:
        newmap.append(line[::-1])
    return newmap

def rotateMap(l,n):
    n=n%8
    if n==0: l
    if n<4:
        return rotateMapOnly(l,n)
    return rotateMapOnly(flipMap(l),n)

tile=-1
def parseFile(lines):
    tiles={}
    for i,line in enumerate(lines):
        if line=="": continue
        if line[:4]=="Tile": 
            tile=int(line[5:-1])
            continue
        line=line.replace(".","0").replace("#","1")
        if tile in tiles:
            tiles[tile]['map'].append(line)
        else:
            tiles[tile]={}
            tiles[tile]['map']=[line]

    return tiles

def tileMapEdges(tile):
        edges=[]
        t=tile[0]
        r=''.join([s[-1] for s in tile])
        b=list(tile[-1])
        b.reverse()
        b=''.join(b)
        l=[s[0] for s in tile]
        l.reverse()
        l=''.join(l)

        return ([int(t,2), int(r,2), int(b,2), int(l,2) ],[int(t[::-1],2), int(r[::-1],2), int(b[::-1],2), int(l[::-1],2) ])


def rotateTile(tile,n):
    tile['edges']=rotate(tile['edges'],n)
    tile['fedges']=rotate(tile['fedges'],n)
    return tile

def makeTileIndex(tiles):
    tileIndex=defaultdict(list)
    for t,tile in tiles.items():
        for i in range(8):
            (e,ec)=tileMapEdges(rotateMap(tile['map'],i))
            tileIndex[(-1,ec[0])].append((t,i,e))
            tileIndex[(ec[3],-1)].append((t,i,e))
            tileIndex[(ec[3],ec[0])].append((t,i,e))
    return tileIndex

def printTile(tile,rot=0):
    m=rotateMap(tile['map'],rot)
    print('\n'.join(m))

def removeEdges(mp):
    result=[]
    for l in mp[1:-1]:
        result.append(l[1:-1])
    return result

def getSeaMap(tiles,soln,rsep='',csep='',wedges=False):
    tiles[-1]={}
    if wedges:
        tiles[-1]['map']=["?"*10 for i in range(10)]
    else:
        tiles[-1]['map']=["?"*8 for i in range(8)]

    result=[]
    for r,tilerow in enumerate(soln):
        ts=[]
        for c,(tile,rot) in enumerate(tilerow):
            if wedges:
                thistile=rotateMap(tiles[tile]['map'],rot)
            else:
                thistile=rotateMap(removeEdges(tiles[tile]['map']),rot)
            ts.append(thistile)
        for l in range(len(ts[0])):
            longline = [tile[l] for tile in ts]
            result.append(csep.join(longline))
        if rsep!='': result.append(rsep)
    return result


def printSoln(tiles,soln,rsep='',csep=''):
    for line in getSeaMap(tiles,soln):
        print (line)

seamonster=[int("00000000000000000010",2),
            int("10000110000110000111",2),
            int("01001001001001001000",2)]

def findMonsters(seamap):
    intmap=[]
    for l in seamap:
        intmap.append(int(l,2))
    h=len(seamap)
    w=len(seamap[0])
    found=[]
    for i in range(h-2):
        for j in range(w):
            if (intmap[i]>>j & seamonster[0]==seamonster[0]) and (intmap[i+1]>>j & seamonster[1]==seamonster[1]) and (intmap[i+2]>>j & seamonster[2]==seamonster[2]):
                intmap[i  ] = intmap[i  ] - (intmap[i  ] & seamonster[0]<<j)
                intmap[i+1] = intmap[i+1] - (intmap[i+1] & seamonster[1]<<j)
                intmap[i+2] = intmap[i+2] - (intmap[i+2] & seamonster[2]<<j)
                found.append((i,j))
                print("FOund:",i,j)
    for (i,j) in found:
        intmap[i]   = intmap[i  ] - (intmap[i  ] & seamonster[0]<<j)
        intmap[i+1] = intmap[i+1] - (intmap[i+1] & seamonster[1]<<j)
        intmap[i+2] = intmap[i+2] - (intmap[i+2] & seamonster[2]<<j)
    waves=0
    for i in intmap:
        waves+=bin(i).count('1')
    return(len(found)!=0,waves)

        



def assembleTiles(tileIndex,N,soln,cons,diag,rowSoFar,used):
    newused=list(used)
    if diag==2*N-1: return (True,soln)
    if len(cons)==0:
        newcons=[-1]
        k=0
        for (t,r,[e1,e2,e3,e4]) in rowSoFar:
            newcons.append(e3)
            newcons.append(e2)
            i,j=-1,-1
            if diag<N:
                i=diag-k
                j=k
            else:
                i=N-k-1
                j=k+diag-N+1

            soln[i][j]=(t,r)
            k+=1
        newcons.append(-1)
        if diag+1>=N: newcons=newcons[2:-2]
        newcons=[(newcons[i],newcons[i+1])  for i in range(0,len(newcons),2)]
        return assembleTiles(tileIndex,N,soln,newcons,diag+1,[],used)
    poss=[(t,i,e) for (t,i,e) in tileIndex[cons[0]] if t not in used]
    #print("Poss:",poss, rowSoFar)
    for (t,i,e) in poss:
        rowSoFar.append((t,i,e))
        used.append(t)
        (res,soln) = assembleTiles(tileIndex,N,soln,cons[1:],diag,rowSoFar,used)
        if res: return (res,soln)
        rowSoFar=rowSoFar[:-1]
        used=used[:-1]
    return (False,soln)

# def findPoss(tiles,edges,excluding):
#     matches=[]
#     for t,tile in tiles.items():
#         if t in excluding: continue
#         e=tile['edges']
#         for i in range(4):
#             if i>0: e=rotate(e,1)
#             if e[:len(edges)]==edges:
#                 matches.append((t,i))
#     return matches


###########################################################################
filename='day20/input.txt'
input = open(filename,'r')
lines = input.read().splitlines()
input.close()

tiles=parseFile(lines)

#print(tiles)
#print(len(tiles))


ti=makeTileIndex(tiles)


if len(tiles)==144: 
    N=12
elif len(tiles)==9: 
    N=3
else:
    print("bad input")
    exit()



soln=[[(-1,0) for i in range(N)] for j in range(N)]

printSoln(tiles,soln)

found=False
cnt=0



for i in tiles.keys():
    if i==-1: continue
    for rot in range(8):##
        soln[0][0]=(i,rot)
        used=[i]
        (edges,edgecompliment)=tileMapEdges(rotateMap(tiles[i]['map'],rot))
        cons=[ (-1,edges[2]), (edges[1],-1) ]
        (found,soln)=assembleTiles(ti,N,soln,cons, 1, [], [i])
        cnt+=1
        if found: break
    if found: break

if found:
    printSoln(tiles,soln)
    print(soln[0][0][0],soln[N-1][0][0],soln[0][N-1][0],soln[N-1][N-1][0])
    print(soln[0][0][0]*soln[N-1][0][0]*soln[0][N-1][0]*soln[N-1][N-1][0])

    seamap=getSeaMap(tiles,soln)
    for i in range(8):       
        (found,waves)=findMonsters(rotateMap(seamap,i))
        if found: print("Got'em:",i,waves)


else:
    print ("Failed")

filename='day20/test-seamap.txt'
input = open(filename,'r')
lines = input.read().splitlines()
input.close()

testseamap=[]
for line in lines:
    testseamap.append(line.replace(".","0").replace("#","1"))

seamap=testseamap
for i in range(8):       
    (found,waves)=findMonsters(rotateMap(seamap,i))
    if found: print("Got'em:",i,waves)


# Answer 1
answer1=-1

# Answer 2

answer2=-1

#print(answer1,answer2)
