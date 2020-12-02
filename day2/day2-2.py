import re
passwd =  open('day2/input.txt','r')

def countc(c,s):
  count=0
  for cc in s:
    if (cc==c): count+=1
  return count

linefmt=re.compile("([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)")
valid=0
for line in passwd:
  m = re.search(linefmt,line)
  lower = int(m.group(1))-1
  upper = int(m.group(2))-1
  pwd = m.group(4)
  ccnt=countc(m.group(3),pwd[lower]+pwd[upper])
  if ccnt == 1:
    valid+=1
  #print(line[:-1]+"="+test)

print(valid)

  