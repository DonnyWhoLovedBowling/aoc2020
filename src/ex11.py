from copy import deepcopy as dc


def split(txt):
    return [c for c in txt]


file = open('../data/ex11.txt', 'r')
lines = file.readlines()
lines = [split(line.replace('\n','')) for line in lines]


def get_nh(x, y):
    nh = 0
    global lines
    x_len = len(lines[0])
    y_len = len(lines)
    stop = False
    for i in range(-1, 2):
        if stop:
            break
        for j in range(-1, 2):
            if stop:
                break
            if 0 <= x+i <= x_len-1 and 0 <= y+j <= y_len-1 and not (j == 0 and i == 0):
                if lines[y+j][x+i] == '#':
                    nh += 1
                    if nh > 3:
                        stop = True
    return nh


def get_nh2(x, y):
    nh = 0
    global lines
    x_len = len(lines[0])
    y_len = len(lines)
    stop = False
    directions = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            directions.append([i, j])

    for d in directions:
        itr = 0
        while True:
            itr += 1
            tx = x + itr * d[0]
            ty = y + itr * d[1]
            if not (0 <= tx < x_len and 0 <= ty < y_len):
                break
            v = lines[ty][tx]
            if v == 'L':
                break
            if v == '#':
                nh += 1
                break
    return nh


    return nh

def new_val(x, y):
    global lines
    v = lines[y][x]
    if v == '.':
        return v
    nh = get_nh(x, y)
    # print((x, y))
    # print(ns)

    if v == 'L' and nh == 0:
        return '#'
    if v == '#' and nh > 3:
        return 'L'
    return v


def new_val2(x, y):
    global lines
    v = lines[y][x]
    if v == '.':
        return v
    nh = get_nh2(x, y)
    # print((x, y))
    # print(ns)

    if v == 'L' and nh == 0:
        return '#'
    if v == '#' and nh > 4:
        return 'L'
    return v


new_lines = dc(lines)
print('lines')
it = 0
while True:
    for i in range(0, len(lines)):
        for j in range(0, len(lines[i])):
            new_lines[i][j] = new_val2(j, i)
    if new_lines == lines:
        break
    print('don\'t break: ' + str(it))
    it += 1
    lines = dc(new_lines)

print('new lines:')
score = 0
n_l = 0
n_p = 0
for line in new_lines:
    for c in line:
        if c == '#':
            score += 1
        if c == 'L':
            n_l += 1
        if c == '.':
            n_p += 1

    print(line)
print('score: ' + str(score))




