from math import ceil

file = open('../data/ex3.txt', 'r')
lines = file.readlines()
nlines = len(lines)
nspots = len(lines[0])
factor = int(ceil((nlines/nspots)*10))+1
newLines = []

for line in lines:
    newLines.append(line.strip('\n')*factor)

def countTrees(lines,sx,sy):
    nTrees = 0
    x = 0
    y = 0
    while ((y+1) < len(lines)):
        x += sx
        y += sy
        if(newLines[y][x] == '#'):
            nTrees += 1
    print('x,y,nTrees: ' + str((x,y,nTrees)))
    return nTrees


print('nTrees: ' + str() )
score = countTrees(newLines,1,1)
score *= countTrees(newLines,3,1)
score *= countTrees(newLines,5,1)
score *= countTrees(newLines,7,1)
score *= countTrees(newLines,1,2)
print('total score: ' + str(score))