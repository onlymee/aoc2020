hillfile =  open('day3/input.txt','r')
hill=[]
for line in hillfile:
  hill.append(line.strip())

height = len(hill)
width = len(hill[1])
print("Map size = ({},{})".format(width,height))

slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]

prod = 1
for slope in slopes:
    dx = slope[0]
    dy = slope[1]
    x = 0
    y = 0
    trees=0
    for y in range(dy, height, dy):
      x+=dx
      if hill[y][x % width]=="#": trees+=1
    print("Slope ({},{}) => {} trees".format(dx,dy,trees))
    prod *=trees
    
print("Tree product for all slope = {}".format(prod))