file = open('../data/ex6.txt', 'r')
lines = file.readlines()

totalString = ''
totalScore = 0
for line in lines:
    totalString += line.strip('\n')
    if(line == '\n' or line == lines[-1]):
        totalScore += len(set(totalString))
        totalString = ''
print('total score is: ' + str(totalScore))

totalSet = set()
totalScore = 0
newline = True
for line in lines:
    print('reading line: ' + line)
    if newline:
        totalSet = set(line.strip('\n'))
        newline = False
    elif line == '\n':
        print(totalSet)
        print(len(totalSet))
        print('')
        totalScore += len(totalSet)
        totalSet = set()
        newline = True
    else:
        print('before intersect: ' + str(totalSet))
        totalSet = totalSet.intersection(set(line.strip('\n')))
        print('after intersect: ' + str(totalSet))

print('second total score is: ' + str(totalScore))