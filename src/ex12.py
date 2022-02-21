def rot(old_d, rot_dir):
    if rot_dir == 'L':
        return [old_d[1] * -1, old_d[0]]
    else:
        return [old_d[1], old_d[0] * -1]


file = open('../data/ex12.txt', 'r')
lines = file.readlines()

x = 0
y = 0
d = [1, 0]

for line in lines:
    command = line[0]
    n = int(line[1:])
    if command == 'N':
        y += n
    elif command == 'S':
        y -= n
    elif command == 'E':
        x += n
    elif command == 'W':
        x -= n
    elif command == 'L' or command == 'R':
        N = int(n / 90)
        for i in range(0, N):
            d = rot(d, command)
    elif command == 'F':
        x += n * d[0]
        y += n * d[1]

print((x, y))

x = 0
y = 0
d = [10, 1]

for line in lines:
    command = line[0]
    n = int(line[1:])
    if command == 'N':
        d[1] += n
    elif command == 'S':
        d[1] -= n
    elif command == 'E':
        d[0] += n
    elif command == 'W':
        d[0] -= n
    elif command == 'L' or command == 'R':
        N = int(n / 90)
        for i in range(0, N):
            d = rot(d, command)
    elif command == 'F':
        x += n * d[0]
        y += n * d[1]

print((x,y))
print(abs(x)+abs(y))