import numpy as np

def iterate(mp):
    adj=[]
    newMp=[]
    emptySeats=0
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
          if newSeat=='#': emptySeats+=1
          newRow+=newSeat
        newMp.append(newRow)
    return (emptySeats,newMp)

def checkEqual(mp1,mp2):
    if len(mp1)!=len(mp2): return False
    for i in range(len(mp1)):
        if mp1[i]!=mp2[i]: return False
    return True

def printMap(mp):
    for line in mp:
        print(line)

filename='day11/input.txt'
input = open(filename,'r')
lines = input.readlines()
input.close()


mp=[]
for line in lines:
    mp.append(line.strip())

printMap(mp)

newMp=[]
emptySeats=-1
i=0
while True:
    print("Iterate: ",i)
    (emptySeats,newMp)=iterate(mp)
    print("---")
    printMap(mp)
    print("---")
    printMap(newMp)
    print("---")
    print (emptySeats)
    print()
    print()
    i+=1


    if checkEqual(mp,newMp): break
    mp=newMp
    newMp=[]


answer1=emptySeats
answer2=-1

print(answer1,answer2)
