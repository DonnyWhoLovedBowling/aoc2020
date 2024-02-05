from copy import deepcopy as dc


def add_tuples(t1, t2):
    return tuple(map(lambda i, j: i + j, t1, t2))


def get_neighbours(tile):
    x = tile[0]
    y = tile[1]
    ans = [(x+1, y), (x-1, y)]
    if y % 2 == 0:
        ans += [(x-1, y+1), (x, y+1), (x-1, y-1), (x, y-1)]
    else:
        ans += [(x+1, y+1), (x, y+1), (x+1, y-1), (x, y-1)]
    return ans


def run(in_lines):
    tiles = set()
    removed = 0
    commands = set()
    for line in in_lines:
        current = (0, 0)
        while line:
            if line[0] in 'sn':
                command = line[0:2]
                line = line[2:]
            else:
                command = line[0]
                line = line[1:]
            if command == 'ne':
                if current[1] % 2 == 0:
                    add = (0, 1)
                else:
                    add = (1, 1)
            elif command == 'se':
                if current[1] % 2 == 0:
                    add = (0, -1)
                else:
                    add = (1, -1)
            elif command == 'nw':
                if current[1] % 2 == 0:
                    add = (-1, 1)
                else:
                    add = (0, 1)
            elif command == 'sw':
                if current[1] % 2 == 0:
                    add = (-1, -1)
                else:
                    add = (0, -1)
            elif command == 'e':
                add = (1, 0)
            elif command == 'w':
                add = (-1, 0)
            else:
                print("ERROR")
                exit(-1)
            current = add_tuples(current, add)
            commands.add(command)
        if current in tiles:
            tiles.remove(current)
            removed += 1
        else:
            tiles.add(current)
    print(f"ans = {len(tiles)}")

    for i in range(100):
        whites = dict()
        remove_tiles = set()
        add_tiles = set()
        for t in tiles:
            black_neighbours = 0
            ns = get_neighbours(t)
            for n in ns:
                if n in tiles:
                    black_neighbours += 1
                else:
                    if n in whites:
                        whites[n] += 1
                    else:
                        whites[n] = 1
            if black_neighbours == 0 or black_neighbours > 2:
                remove_tiles.add(t)
        for t, v in whites.items():
            if v == 2:
                add_tiles.add(t)
        tiles = tiles.difference()
        tiles.difference_update(remove_tiles)
        tiles.update(add_tiles)
        print(i, len(tiles))


if __name__ == '__main__':
    lines = [line.replace('\n', '') for line in open('../data/ex24.txt', 'r').readlines()]
    run(lines)
