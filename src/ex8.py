file = open('../data/ex8.txt', 'r')
lines = file.readlines()


def run(swap_iter):
    i = 0
    history = set()
    score = 0
    j = 0

    while True:
        if i in history or i > len(lines):
            return False,score
        history.add(i)
        cmd = lines[i].split(' ')[0]
        par = int(lines[i].split(' ')[1])
        if cmd == 'nop' or cmd == 'jmp':
            if j == swap_iter:
                if cmd == 'nop':
                    cmd = 'jmp'
                else:
                    cmd = 'nop'
            j += 1

        if cmd == 'nop':
            j += 1
            i += 1
        elif cmd == 'jmp':
            i += par
            j += 1
        elif cmd == 'acc':
            i += 1
            score += par
        else:
            print('error! cmd = ' + cmd )
        if i > len(lines) - 1:
            return True,score


itr = 0
stop = False
score = 0
while not stop:
    stop, score = run(itr)
    itr += 1
print(score)

