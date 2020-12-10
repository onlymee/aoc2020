import numpy as np
filename='day10/input.txt'
input = open(filename,'r')
lines = input.readlines()
input.close()

jolts = [int(i) for i in lines]
jolts.sort()
jolts.insert(0,0)
jolts.append(jolts[-1]+3)

diffs=''.join(map(str,np.diff(jolts)))

answer1=diffs.count('1')*diffs.count('3')

combos=[1,1,2,4,7]
runsof1combos = [combos[i.count('1')] for i in diffs.split('3')]

answer2=np.product(runsof1combos)
print(answer1,answer2)
