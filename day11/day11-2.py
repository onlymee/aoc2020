import numpy as np

def iterate(mp):
    adj=[]
    newMp=[]
    occ=0
    chg=0
    for i,row in enumerate(mp):
        newRow=""
        for j,seat in enumerate(row):
          cnt=0
          if seat=='.':
              newRow+=seat
              continue
          newSeat=seat
          if i>0 and mp[i-1][j]=='#': cnt+=1
          if i<len(mp)-1 and mp[i+1][j]=='#': cnt+=1
          if j>0 and mp[i][j-1]=='#': cnt+=1
          if j<len(row)-1 and mp[i][j+1]=='#': cnt+=1
          if i>0 and j>0 and mp[i-1][j-1]=='#': cnt+=1
          if i<len(mp)-1 and j<len(row)-1 and mp[i+1][j+1]=='#': cnt+=1
          if i>0 and j<len(row)-1 and mp[i-1][j+1]=='#': cnt+=1
          if i<len(mp)-1 and j>0 and mp[i+1][j-1]=='#': cnt+=1
          if cnt==0: newSeat='#'
          if cnt>=4: newSeat='L'
          if newSeat!=seat: chg+=1
          if newSeat=='#': occ+=1
          newRow+=newSeat
        newMp.append(newRow)
    return (occ,chg,newMp)

def iterate2(mp):
    adj=[]
    newMp=[]
    occ=0
    chg=0
    for i,row in enumerate(mp):
        newRow=""
        for j,seat in enumerate(row):
          if seat=='.':
              newRow+=seat
              continue
          newSeat=seat
          cnt=scan(mp,i,j)
          if cnt==0: newSeat='#'
          if cnt>=5: newSeat='L'
          if newSeat!=seat: chg+=1
          if newSeat=='#': occ+=1
          newRow+=newSeat
        newMp.append(newRow)
    return (occ,chg,newMp)


def onMap(r,c,h,w):
    return (r>=0 and c>=0 and r<h and c<w)

def scan(mp,r,c):
    seats=""
    h=len(mp)
    w=len(mp[0])
    vec=[(-1,0),(0,-1),(1,0),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
    pos=[(r,c) for i in range(8)]
    while len(vec)>0:
        newPos=[]
        newVec=[]
        for i in range(len(vec)):
            (dr,dc)=vec[i]
            (pr,pc)=pos[i]
            pr+=dr
            pc+=dc
            if onMap(pr,pc,h,w):
                if mp[pr][pc] in "#L":
                    seats+=mp[pr][pc]
                else:
                    newPos.append((pr,pc))
                    newVec.append((dr,dc))
        vec=newVec
        pos=newPos
    return seats.count('#')


def checkEqual(mp1,mp2):
    if len(mp1)!=len(mp2): return False
    for i in range(len(mp1)):
        if mp1[i]!=mp2[i]: return False
    return True

def printMap(mp):
    for line in mp:
        print(line)


def getAnswer1(mp):
    newMp=[]
    occ=-1
    i=0
    while True:
        (occ,chg,newMp)=iterate(mp)
#        print("Iterate: ",i, occ)
        if chg==0: break
        mp=newMp
        newMp=[]
        i+=1
    return occ

def getAnswer2(mp):
    newMp=[]
    occ=-1
    i=0
    while True:
        (occ,chg,newMp)=iterate2(mp)
#        print("Iterate: ",i, occ)
        if chg==0: break
        mp=newMp
        newMp=[]
        i+=1
    return occ

filename='day11/input.txt'
input = open(filename,'r')
lines = input.readlines()
input.close()

mp=[]
for line in lines:
    mp.append(line.strip())

#printMap(mp)
answer1=getAnswer1(mp)
answer2=getAnswer2(mp)

print(answer1,answer2)
