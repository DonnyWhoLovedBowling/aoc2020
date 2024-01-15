file = open('../data/ex2.txt', 'r')
lines = file.readlines()

pws = 0
for line in lines:
    splt = line.split(':')
    mn = int(splt[0].split('-')[0])
    mx = int(splt[0].split(' ')[0].split('-')[1])
    letter = splt[0].split(' ')[1]
    pw = splt[1].strip()
    occ = pw.count(letter)
    if mn <= occ <= mx:
        pws += 1
print(pws)
