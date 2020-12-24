import numpy as np
from collections import defaultdict
#from bitstring import BitArray
import re

def rotate(l, n):
    return l[-n:] + l[:-n]

def rotate(l, n):
    return l[-n:] + l[:-n]

def move(cups):
    N=len(cups)
    
    pickup=cups[1:4]
    cups=cups[0:1]+cups[4:]
    dest=N if cups[0]==1 else cups[0]-1
    while not dest in cups:
        dest=N if dest==1 else dest-1
    ins=cups.index(dest)
    cups=cups[0:ins+1]+pickup+cups[ins+1:]
    return rotate(cups,-1)


###########################################################################
input=(2,1,5,6,9,4,7,8,3)
# input=(3,8,9,1,2,5,4,6,7)  #Test data

i=0
cups=input
while i<100:
    # print(i,cups)
    cups=move(cups)
    i+=1

answer1=''.join([str(i) for i in rotate(cups,-cups.index(1))[1:]])


# Answer 2
class Node:
    def __init__(self, value):
        self.value = value
        self.next=None

cups=list(input)+list(range(10,1000001))
N=len(cups)
nodes={i:Node(i) for i in range(1,1000001)}
for i in range(len(cups)):
    nodes[cups[i]].next=nodes[cups[(i+1)%N]]

i=0
current=nodes[cups[0]]
while i<10000000:
    pickup=current.next
    current.next=current.next.next.next.next
    destvalue=current.value-1 if current.value!=1 else N
    while destvalue in [pickup.value, pickup.next.value, pickup.next.next.value]:
        destvalue= destvalue - 1 if destvalue!=1 else N
    dest=nodes[destvalue]
    pickup.next.next.next=dest.next
    dest.next=pickup
    current=current.next
    i+=1

answer2=nodes[1].next.value*nodes[1].next.next.value

print(answer1,answer2)
