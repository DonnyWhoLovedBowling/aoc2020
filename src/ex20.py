from __future__ import annotations

import math
from copy import deepcopy as dc
from regex import finditer
from line_profiler_pycharm import profile


@profile
def rotate(all_lines):
    return [''.join(reversed([row[n] for row in all_lines if row != ''])) for n in
            range(len(all_lines))]


@profile
def flip(all_lines):
    return ["".join(reversed(line)) for line in all_lines]


class Tile:
    def __init__(self, block: list):
        self.id = int(block[0][5:9])
        self.all_lines = [b for b in block[1:] if b != '']
        self.value_lines = [l[1:-1] for l in self.all_lines[1:-1]]
        self.borders = []
        self.calc_borders()
        self.fixed = False
        self.rng = range(0, len(self.value_lines), 1)

    @profile
    def __hash__(self):
        return hash(self.id)

    @profile
    def __repr__(self):
        return self.id

    @profile
    def __eq__(self, other):
        return self.id == other.id

    @profile
    def merge(self, other: Tile, horizontal=True, vertical=True):
        for _ in range(4):
            for __ in range(2):
                if self.borders[0] == other.borders[1] and vertical:

                    other.fixed = True
                    self.value_lines = other.value_lines + self.value_lines  # other zit boven self
                    self.borders[0] = other.borders[0]
                    self.borders[2] = other.borders[2]
                    self.borders[3] = other.borders[3]
                    self.rng = range(0, len(other.value_lines), 1)
                    print('going up')
                    return True
                elif self.borders[1] == other.borders[0] and vertical:
                    other.fixed = True
                    self.value_lines += other.value_lines  # self zit boven other
                    self.borders[1] = other.borders[1]
                    self.borders[2] = other.borders[2]
                    self.borders[3] = other.borders[3]
                    self.rng = range(-1, -(len(other.value_lines) + 1), -1)
                    print('going down')

                    return True
                elif self.borders[2] == other.borders[3] and horizontal:
                    other.fixed = True
                    for i in self.rng:
                        self.value_lines[i] = other.value_lines[i] + self.value_lines[i]

                    if list(self.rng)[0] == 0:
                        self.borders[0] = other.borders[0]
                    else:
                        self.borders[1] = other.borders[1]

                    self.borders[2] = other.borders[2]
                    return True
                elif self.borders[3] == other.borders[2] and horizontal:
                    other.fixed = True
                    for i in self.rng:
                        self.value_lines[i] += other.value_lines[i]
                    if list(self.rng)[0] == 0:
                        self.borders[0] = other.borders[0]
                    else:
                        self.borders[1] = other.borders[1]
                    self.borders[3] = other.borders[3]
                    return True
                if not other.fixed:
                    other.flip()
                else:
                    break
            if not other.fixed:
                other.rotate()
            else:
                break

        return False

    @profile
    def rotate(self):

        self.all_lines = rotate(self.all_lines)
        self.calc_borders()

    @profile
    def flip(self):
        self.all_lines = flip(self.all_lines)
        self.calc_borders()

    @profile
    def calc_borders(self):
        up = self.all_lines[0]
        down = self.all_lines[9]
        left = ''.join([row[0] for row in self.all_lines if row != ''])
        right = ''.join([row[-1] for row in self.all_lines if row != ''])
        self.borders = [up, down, left, right]
        self.value_lines = [l[1:-1] for l in self.all_lines[1:-1]]

    @profile
    def print(self):
        for line in self.value_lines:
            print(line)
        print()


dir_map = {0: 'u', 1: 'd', 2: 'l', 3: 'r'}
master_tile = []
tiles = {Tile(t.split('\n')) for t in open('../data/ex20.txt', 'r').read().split('\n\n')}
tile_map = {t.id: t for t in tiles}
@profile
def run():
    global master_tile, tiles
    matched_tiles = set()
    n_tiles = len(tiles)
    t_start = next(iter(tiles))
    t_start.print()
    matched_tiles.add(t_start)
    while len(tiles) != len(matched_tiles):
        for _ in range(len(tiles)):
            h = 0
            for t in tiles.difference(matched_tiles):
                if t_start.merge(t, horizontal=True, vertical=False):
                    matched_tiles.add(t)
                    h += 1
                if h == math.sqrt(n_tiles):
                    break
            if h == math.sqrt(n_tiles):
                break

        found = False
        for t in tiles.difference(matched_tiles):
            if t_start.merge(t, horizontal=False, vertical=True):
                found = True
                matched_tiles.add(t)
                break
        if not found and len(tiles) != len(matched_tiles):
            print("couldn't find vertical expansion!", len(matched_tiles))

    total = 1
    upper_left = [t[0:8] for t in t_start.value_lines[0:8]]
    upper_right = [t[-8:] for t in t_start.value_lines[0:8]]
    lower_left = [t[0:8] for t in t_start.value_lines[-8:]]
    lower_right = [t[-8:] for t in t_start.value_lines[-8:]]
    corners = [upper_left, upper_right, lower_right, lower_left]
    for t in matched_tiles:
        matched = False
        value_lines = dc(t.value_lines)
        for _ in range(4):
            value_lines = rotate(value_lines)
            for __ in range(2):
                value_lines = flip(value_lines)
                if value_lines in corners:
                    total *= t.id
                    matched = True
                    break
                if matched:
                    break
            if matched:
                break
    print(f"ans pt1 = {total}")

    pattern_str = """
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """
    pattern_str = pattern_str.replace(' ', '.')
    pattern_lst = pattern_str.split('\n')[1:]
    total = sum([line.count('#') for line in t_start.value_lines])

    for _ in range(4):
        t_start.value_lines = rotate(t_start.value_lines)
        for __ in range(2):
            t_start.value_lines = flip(t_start.value_lines)
            for i in range(0, len(t_start.value_lines)-len(pattern_lst)):
                matches = []
                for j in range(0, len(pattern_lst)):
                    line = t_start.value_lines[i + j]
                    pattern = pattern_lst[j]
                    starts = {m.start(0) for m in finditer(f"(?={pattern})", line)}
                    matches.append(starts)
                total -= len(set.intersection(*matches))*15

    print(f"ans pt2 = {total}")


if __name__ == '__main__':
    run()
