import re
passwd =  open('day2/input.txt','r')

def countc(c,s):
  found=0
  for cc in s:
    if (cc==c): found+=1
  return found

linefmt=re.compile("([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)")
valid=0
for line in passwd:
  m = re.search(linefmt,line)
  lower = int(m.group(1))
  upper = int(m.group(2))
  ccnt = countc(m.group(3),m.group(4))
  test="Fail"
  if ccnt >= lower and ccnt<=upper:
    test="Pass"
    valid+=1
#    print(line[:-1]+"="+test)

print(valid)

  