import numpy as np
from collections import defaultdict
#from bitstring import BitArray
import re


def parseFile(lines):
    foods=[]
    ings=set()
    als=set()

    for i,line in enumerate(lines):
        food={}
        ing,al=line,""
        if "contains" in line:
            ing,al = line.split(" (contains ")
            al=al[:-1]
        inglist=ing.split(" ")
        allist=al.split(", ")
        food=(set(inglist),set(allist))
        for i in inglist:
            ings.add(i)
        for i in allist:
            als.add(i)
        foods.append(food)
    return (foods,ings,als)

###########################################################################
filename='day21/input.txt'
input = open(filename,'r')
lines = input.read().splitlines()
input.close()

(foods, ingredients, allergens)=parseFile(lines)

alcand=defaultdict(list)
for a in allergens:
    alcand[a]=ingredients.copy()

for (ing,als) in foods:
    for a in als:
        alcand[a].intersection_update(ing)

print(alcand)

#eliminate
knownallergens={}
canelim=[a for a in alcand if len(alcand[a])==1]
while canelim:
    for i in canelim:
        if i in knownallergens: 
            print("Cannot happen!")
            exit()
        else:
            ing=list(alcand[i])[0]
            del alcand[i]
            knownallergens[i]=ing
            for a in alcand:
                alcand[a].difference_update([ing])
    canelim=[a for a in alcand if len(alcand[a])==1]

print("Known:",knownallergens)


reming=ingredients.copy()
for a in alcand:
    reming.difference_update(alcand[a]) 

for i in knownallergens:
    reming.difference_update([knownallergens[i]]) 



print(reming)

# Answer 1
answer1=0
for (i,a) in foods:
    found=i.intersection(reming)
    answer1+=len(found)




# Answer 2
sal=[i for i in knownallergens.keys()]
sal.sort()

bading=[]
for i in sal:
    bading.append(knownallergens[i])
answer2=','.join(bading)

print(answer1,answer2)
