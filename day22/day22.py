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

def score(player):
    score=0
    i=1
    while player:
        score+=player.pop()*i
        i+=1
    return score

def combat(player1,player2,game=1):
    while player1 and player2:
        p1=player1.popleft()
        p2=player2.popleft()
        if p1>p2:
            player1.append(p1)
            player1.append(p2)
        if p2>p1:
            player2.append(p2)
            player2.append(p1)

    if player1: winner=1
    else: winner=2
    return player1,player2,winner

def recursive_combat(player1,player2,game=1):
    plays=set()
    round=0
    while player1 and player2:
        round+=1
        deck=tuple(list(player1)+[-1]+list(player2))
        if deck in plays: return player1,player2,1
        plays.add(deck)

        p1=player1.popleft()
        p2=player2.popleft()
        if p1<=len(player1) and p2<=len(player2):
            (sp1,sp2,swinner)=recursive_combat(deque(list(player1)[:p1]),deque(list(player2)[:p2]),game+1)
            if swinner==1:
                player1.append(p1)
                player1.append(p2)
            else:
                player2.append(p2)
                player2.append(p1)
        else:
            if p1>p2:
                player1.append(p1)
                player1.append(p2)
            if p2>p1:
                player2.append(p2)
                player2.append(p1)

    if player1: winner=1
    else: winner=2
    return player1,player2,winner


filename='day22/input.txt'
input = open(filename,'r')
lines = input.read().splitlines()
input.close()

# Answer 1
(player1,player2)=parseFile(lines)
player1,player2,winner=combat(player1,player2)
if winner==1:
    answer1=score(player1)
else:
    answer1=score(player2)

# Answer 2
(player1,player2)=parseFile(lines)
player1,player2,winner=recursive_combat(player1,player2)
if winner==1:
    answer2=score(player1)
else:
    answer2=score(player2)



print(answer1,answer2)
