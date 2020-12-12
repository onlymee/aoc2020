import numpy as np

filename='day12/test.txt'
input = open(filename,'r')
lines = input.readlines()
input.close()

dirs=[]
for line in lines:
    inst=(line[0],int(line[1:]))
    print(line, inst)
    dirs.append(inst)

posx=0
posy=0
dir=90
wpx=10
wpy=1



for (move,val) in dirs:
    if move=='L':
        for i in range(int(val/90)):
            (wpx,wpy)=(-wpy,wpx)
    elif move=='R':
        for i in range(int(val/90)):
            (wpx,wpy)=(wpy,-wpx)
    elif move=='N':
        wpy+=val
    elif move=='S':
        wpy-=val
    elif move=='E':
        wpx+=val
    elif move=='W':
        wpx-=val
    elif move=='F':
        posx+=wpx*val
        posy-=wpy*val
    print(posx,posy,dir,move,val)

print (posx,posy)

answer1=abs(posx)+abs(posy)
answer2=-1

print(answer1,answer2)
