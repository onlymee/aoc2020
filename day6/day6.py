input = open('day6/input.txt','r')
lines = input.readlines()
input.close()
lines.append("")

qcount={}
rowcount=0
answer1=0
answer2=0
for line in lines:
  line=line.strip()
  if (line==""):
    answer1+=len(qcount)
    for (k,v) in qcount.items():
        if v==rowcount: answer2+=1 
    qcount={}
    rowcount=0
  else:
    rowcount+=1
    for c in line: 
        if (c in qcount.keys()): qcount[c]+=1
        else: qcount[c]=1
    
print(answer1,answer2)
