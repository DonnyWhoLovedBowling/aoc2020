file = open('../data/ex2.txt', 'r')
lines = file.readlines()


pws  = 0
for line in lines:
    splt = line.split(':')
    ix1 = int(splt[0].split('-')[0])-1
    ix2 = int(splt[0].split(' ')[0].split('-')[1])-1
    letter = splt[0].split(' ')[1]
    pw = splt[1].strip()
    ln = len(pw)
    firstContains = (ln > ix1 and pw[ix1] == letter)
    secondContains = (ln > ix2 and pw[ix2] == letter)
    if(firstContains != secondContains):
        pws += 1

        
print(pws)
             

