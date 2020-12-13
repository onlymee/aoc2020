import numpy as np

filename='day13/input.txt'
input = open(filename,'r')
lines = input.readlines()
input.close()

for i,line in enumerate(lines):
    print(line)

#buses=[7,13,59,31,19]
buses=[29,41,37,653,13,17,23,823,19]
t0=1008169
t=t0
found=False
while not found:
    for b in buses:
        if t % b == 0:
            found=True
            print((t-t0)*b)
            break
    t=t+1

answer1=-1
answer2=-1

print(answer1,answer2)
