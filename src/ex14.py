from math import pow
from copy import deepcopy as dc

f = open('../data/ex14.txt', 'r')
lines = f.readlines()
memory = dict()


def val_variations(var):
    xs = var.count('X')
    n_max = int(pow(2, xs))
    replacements = [str(bin(b)).replace('b', '').zfill(xs)[-1*xs:] for b in range(0, n_max)]
    variations = []

    for r in replacements:
        mask_r = dc(var)
        j = 0
        for i, m in enumerate(mask_r):
            if m == 'X':
                mask_r[i] = r[j]
                j += 1
        variations.append(mask_r)
    return variations


def process_line(line, mask):
    global memory
    begin = line.find('[') + 1
    end = line.find(']')
    index = line[begin:end]
    value = int(line[end+4:])
    value_bin = [c for c in str(bin(value)).replace('b', '').zfill(36)]
    mask_list = [m for m in mask]
    for i, m in enumerate(mask_list):
        if m == 'X':
            continue
        else:
            value_bin[i] = m
    val = int(''.join(value_bin), 2)
    return index, val


def process_line2(line, mask):
    global memory
    begin = line.find('[') + 1
    end = line.find(']')
    index = int(line[begin:end])
    value = int(line[end+4:])
    index_bin = [c for c in str(bin(index)).replace('b', '').zfill(36)]
    mask_list = [m for m in mask]
    for i, m in enumerate(mask_list):
        if m == '0':
            continue
        else:
            index_bin[i] = m

    var = val_variations(index_bin)
    return var, value


def process_block(block):
    global memory
    if len(block) > 0:
        mask = block[0].replace('mask = ', '').replace('\n',  '')
    for line in block[1:]:
        ix, val = process_line(line, mask)
        memory[ix] = val


def process_block2(block):
    global memory
    if len(block) > 0:
        mask = block[0].replace('mask = ', '').replace('\n',  '')

    for line in block[1:]:
        ixs, val = process_line2(line, mask)
        for ix in ixs:
            memory[int(''.join(ix), 2)] = val


def run():
    global lines
    global memory

    blocks = []
    block = []
    for line in lines:
        if 'mask' in line:
            blocks.append(block)
            block = []
        block.append(line)
    blocks.append(block)

    for block in blocks:
        process_block(block)
    score = 0
    for v in memory.values():
        score += v
    print(score)

    memory = dict()
    score = 0
    for block in blocks:
        process_block2(block)

    for k in memory.keys():
        score += memory[k]
    print(score)


if __name__ == '__main__':
    run()
