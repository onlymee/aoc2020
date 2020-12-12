import numpy as np

filename='day12/input.txt'
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


for (move,val) in dirs:
    if move=='L':
        dir=(dir-val+360) % 360
    elif move=='R':
        dir=(dir+val) % 360
    elif move=='N':
        posy+=val
    elif move=='S':
        posy-=val
    elif move=='E':
        posx+=val
    elif move=='W':
        posx-=val
    elif move=='F':
        if dir==0:
            posy+=val
        elif dir==180:
            posy-=val
        elif dir==90:
            posx+=val
        elif dir==270:
            posx-=val
    print(posx,posy,dir,move,val)

print (posx,posy)

answer1=abs(posx)+abs(posy)
answer2=-1

print(answer1,answer2)
