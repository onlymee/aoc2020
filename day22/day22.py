import numpy as np
from collections import defaultdict,deque
#from bitstring import BitArray
import re


def parseFile(lines):
    points=set()
    player=0
    player1=deque()
    player2=deque()
    for i,line in enumerate(lines):
        if line=="": 
            continue
        if "Player" in line:
            player+=1
            continue
        if player==1:
            player1.append(int(line))
        else:
            player2.append(int(line))
    return (player1,player2)

###########################################################################
filename='day22/input.txt'
input = open(filename,'r')
lines = input.read().splitlines()
input.close()

(player1,player2)=parseFile(lines)
print(player1)

while player1 and player2:
    print("Player 1's deck:",list(player1))
    print("Player 2's deck:",list(player2))
    p1=player1.popleft()
    p2=player2.popleft()
    if p1>p2:
        player1.append(p1)
        player1.append(p2)
    if p2>p1:
        player2.append(p2)
        player2.append(p1)

score1,score2=0,0
i=1
while player1 or player2:
    if player1: score1+=player1.pop()*i
    if player2: score2+=player2.pop()*i
    i+=1

# Answer 1
answer1=(score1,score2)

# Answer 2

answer2=-1

print(answer1,answer2)
