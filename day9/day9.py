def canMake(num,code):
    for i in code:
        if (num-i) in code:
            return True
    return False


filename='day9/input.txt'
input = open(filename,'r')
lines = input.readlines()
input.close()

code=[]
input=[]
for line in lines:
        num=int(line.strip())
        input.append(num)
        if len(code)<25:
            code.append(num)
            continue
        code=code[-25:]
        if not canMake(num,code):
            answer1=num
            break
        code.append(num)

n=len(input)
for i in range(n):
  for j in range(i+1,n):
      if sum(input[i:j])==answer1:
          answer2 = max(input[i:j])+min(input[i:j])

print(answer1,answer2)
