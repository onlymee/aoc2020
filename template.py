import numpy as np
from collections import defaultdict
#from bitstring import BitArray
import re


def parseFile(lines):
    points=set()
    for i,line in enumerate(lines):
        for j,ch in enumerate(line):
            if ch=="#": points.add((i,j,0))
    return points

###########################################################################
filename='day18/input.txt'
input = open(filename,'r')
lines = input.read().splitlines()
input.close()

points=parseFile(lines)

# Answer 1
answer1=-1

# Answer 2

answer2=-1

print(answer1,answer2)
