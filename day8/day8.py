 
def run(prog):
  prog=list(prog)
  ip=0
  acc=0
  while ip<len(prog):
      (ins,operand)=prog[ip]
      prog[ip]=("hlt",operand)  # Loop protection!
      
      if ins=="hlt": break
      if ins=="acc": acc+=int(operand)
      if ins=="jmp": 
          ip+=int(operand)
          continue
      # nop - 
      ip+=1
  return (acc,ip)

def load_prog(filename):
    input = open(filename,'r')
    lines = input.readlines()
    input.close()

    prog=[]
    for line in lines:
        line=line.strip().split(' ')
        line=(line[0],line[1])
        prog.append(line)
    return prog

def fix_prog(prog,i):
    prog2=prog.copy()
    (ins,operand)=prog2[i]
    if ins=="jmp": ins="nop"
    elif ins=="nop": ins="jmp"
    prog2[i]=(ins,operand)
    return prog2


## MAIN ########################################################

# prog=load_prog('day8/test1.txt')
# result=run(prog)
# print(result)

prog=load_prog('day8/input.txt')
answer1=run(prog)[0]

for i, l in enumerate(prog):
    (acc,ip)=run(fix_prog(prog,i))
    if ip==len(prog):
        answer2=acc
        break

print(answer1,answer2)
