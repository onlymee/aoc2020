import numpy as np
from collections import defaultdict
#from bitstring import BitArray
import re

def fieldValid(r,v):
    return (v>=r[0] and v<=r[1]) or (v>=r[2] and v<=r[3])

def valid(rules,t):
    for v in t:
        found=False
        for k,r in rules.items():
            if fieldValid(r,v): 
                found=True
                break
        if found==False:
            return False
    return True

def errcount(rules,t):
    errcount=0
    for v in t:
        found=False
        for k,r in rules.items():
            if fieldValid(r,v): 
                found=True
                break
        if found==False:
            errcount+=v
    return errcount

def validFor(rules,t):
    validList=[]
    for v in t:
        valid=[]
        for k,r in rules.items():
            if fieldValid(r,v): 
                valid.append(k)
        validList.append(valid)
    return validList

def parseFile(lines):
    mode="rules"
    tickets=[]
    rules={}
    for line in lines:
        if mode=="rules":
            if line=="": 
                mode="ticket"
                continue
            (field, rng)=line.split(": ")
            rngs = "-".join(rng.split(" or ")).split("-")
            rules[field]=[int(i) for i in rngs]
        if mode=="ticket":
            if line=="your ticket:":
                continue
            tickets.append([int(i) for i in line.split(",")])
            mode="others"
        if mode=="others":
            if line=="": 
                continue
            if line=="nearby tickets:":
                continue
            tickets.append([int(i) for i in line.split(",")])
    return (rules,tickets)


###########################################################################
filename='day16/input.txt'
input = open(filename,'r')
lines = input.read().splitlines()
input.close()

(rules,tickets)=parseFile(lines)

# Answer 1
answer1=sum([errcount(rules,t) for t in tickets[1:]])

# Answer 2
vtickets=[t for t in tickets if valid(rules,t)]
possibleFields = [validFor(rules,t) for t in vtickets]
fields=[]
for i in range(len(tickets[1])):
    options = set(rules.keys())
    for tp in possibleFields::while
        options.intersection_update(tp[i])
    fields.append(options)

while (max([len(f) for f in fields])>1):
    fixed = set([list(f)[0] for f in fields if len(f)==1])
    for f in fields:
        if len(f)==1: continue
        f.difference_update(fixed)

fields=[list(f)[0] for f in fields]
posn = [i for i,f in enumerate(fields) if "departure" in f]

answer2=np.prod([tickets[0][i] for i in posn])

print(answer1,answer2)
