import numpy as np

report =  sorted(np.loadtxt('input.txt',dtype=int))

found=False
for value in report:
  delta=2020-value
  for value2 in reversed(report):
    if found: break
    if (delta==value2):
        print(value*value2)
        found=True
        break

found=False
for value in report:
  for value2 in report:
    delta=2020-value-value2
    for value3 in reversed(report):
      if found: break
      if (delta==value3):
          print(value*value2*value3)
          found=True
          break
