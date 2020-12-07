
import re
def canContain(bags,target_bag):
  result=[]
  for (k,bag) in bags.items():
    if target_bag in bag: result.append(k)
  return result

input = open('day7/input.txt','r')
lines = input.readlines()
input.close()

bags={}
linefmt=re.compile("^([a-z]+ [a-z]+) bags contain (.*)$")
elementfmt=re.compile("([0-9]+) ([a-z]+ [a-z]+) bag(s?)(,|\.)")
for line in lines:
  a=linefmt.match(line)
  container=a.group(1)
  if (a.group(2)=="no other bags."): bags[container]={}
  b=elementfmt.findall(a.group(2))
  for bag in b:
    if container not in bags: bags[container]={}
    bags[container][bag[1]]=bag[0]


#Answer 2
found={}
tally={}
lookup={'shiny gold':1}
while (len(lookup) > 0):
  bag=lookup.popitem()
  for (k,v) in bags[bag[0]].items():
    q=int(v)*bag[1]
    if k in lookup: lookup[k]+=q
    else: lookup[k]=q
    if k in tally: tally[k]+=q
    else: tally[k]=q

answer2=0
for (k,v) in tally.items(): answer2+=v

#Answer 1
found={}
lookup=['shiny gold']
while (len(lookup) > 0):
  bag=lookup.pop()
  m=canContain(bags,bag)
  lookup.extend(m)  
  for b in m: 
    if b in found: found[b]+=1
    else: found[b]=1
    del bags[b]

answer1=len(found)
print(answer1, answer2)
