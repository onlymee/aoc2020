import numpy as np
from collections import defaultdict

input=[0,14,1,3,7,9]
game=input

spoken=defaultdict(list)
for i,n in enumerate(game):
    spoken[n]=i+1

lastspoken=game[-1]
lastturn=len(game)

answer1,answer2=-1,-1

while lastturn<30000000:
    if lastturn==2020: answer1=lastspoken
    if lastspoken in spoken:
        nxt=lastturn-spoken[lastspoken]
    else:
        nxt=0
    spoken[lastspoken]=lastturn
    lastspoken=nxt
    lastturn=lastturn+1
     
answer2=lastspoken

print(answer1,answer2)
