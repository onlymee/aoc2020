


filename='day10/test2.txt'
input = open(filename,'r')
lines = input.readlines()
input.close()


code=[]
input=[]
for line in lines:
        num=int(line.strip())
        input.append(num)
input.append(0)

input.sort()
deltas={}
diffs=""
for i,inp in enumerate(input):
    if i==0:continue  
    diff=input[i]-input[i-1]
    diffs+=str(diff)
    if diff in deltas: deltas[diff]+=1
    else: deltas[diff]=1

counts={}
answer2=1
mult=[1,1,2,4,7]
for line in diffs.split("3"):
  if len(line) in counts: counts[len(line)]+=1
  else: counts[len(line)]=1
  answer2*=mult[len(line)]
  print(line)

print(counts)
answer1=deltas[1]*deltas[3]
print(answer1,answer2)
