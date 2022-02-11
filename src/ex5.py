def lineToID(line):
    min = 0
    max = 127
    n = 128
    for c in line[0:7]:
        n = n/2
        if(c == 'F'):
            max -= n
        elif(c == 'B'):
            min += n
        else:
            break
    if min != max:
        print(line[0:7] + ' min,max: ' + str((min, max)))
        raise Exception('min unequal to max')
    row = max
    min = 0
    max = 7
    n = 8
    for c in line[7:10]:
        n = n/2
        if c == 'L':
            max -= n
        elif c == 'R':
            min += n
        else:
            break
    if min != max:
        print(line[7:10] + ' min,max: ' + str((min, max)))
        raise Exception('min unequal to max')
    col = max
    return row*8+col


file = open('../data/ex5.txt', 'r')
lines = file.readlines()

ticketSet = set()
for line in lines:
    ticketSet.add(lineToID(line))

for i in range(0,127*8+7):
    if(i in ticketSet):
        continue
    if(i-1 not in ticketSet):
        continue
    if(i+1 not in ticketSet):
        continue
    print('your ticket is: ' + str(i))
print('number of tickets left:' + str(len(ticketSet)))
print('highest ticket' + str(max(ticketSet)))

