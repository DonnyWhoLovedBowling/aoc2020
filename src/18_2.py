def has_num_addition(line):
    while line.find('+') != -1:
        ix = line.find('+')
        if line[ix-1].isnumeric() and line[ix+1].isnumeric():
            return True
        line = line[ix+1:]
    return False


def parse_num(ix, line):
    num = ''
    stop_ix = len(line)
    while line[ix].isnumeric():
        num += line[ix]
        ix += 1
        if ix >= stop_ix:
            break
    return int(num), ix


def replace_brackets(line):
    ix = line.rfind('(')
    start_ix = ix
    total = 1
    while line[ix] != ')':
        ix += 1
        if line[ix].isnumeric():
            num, ix = parse_num(ix, line)
            total *= num

    if (ix+1) < len(line):
        ret = line[0:start_ix]+str(total)+line[ix+1:]
    else:
        ret = line[0:start_ix]+str(total)

    return ret


# Assume all other operations are completed
def do_multiplications(line):
    ix = 0
    total = 1
    while ix < len(line):
        if line[ix].isnumeric():
            num, ix = parse_num(ix, line)
            total *= num
        else:
            ix += 1
    return total


def replace_additions(line):
    ix = 0
    stop_ix = len(line)-1
    while ix < stop_ix:
        stop_ix = len(line) - 1
        start_ix = ix
        num_l = -1
        num_r = -1
        if ix >= stop_ix:
            break
        if line[ix].isnumeric():
            num_l, ix = parse_num(ix, line)
            if ix >= stop_ix:
                break

            if line[ix] == '+':
                ix += 1
                if line[ix].isnumeric():
                    num_r, ix = parse_num(ix, line)

            if num_l != -1 and num_r != -1:
                num = num_l+num_r
                line = line[0:start_ix] + str(num) + line[ix:]
        else:
            ix += 1

    return line


def main():
    with open('../data/ex18.txt') as f:
        lines = f.readlines()
    lines = [line.replace(' ', '').replace('\n', '') for line in lines if line.strip()]
    new_lines = list()
    score = 0
    for line in lines:
        print(line)
        cont = True
        while has_num_addition(line):
            line = replace_additions(line)
        print('additions replaced: ' + line)
        while line.find('(') != -1:
            line = replace_brackets(line)
            print('brackets replaced: ' + line)
            while has_num_addition(line):
                line = replace_additions(line)
                print('additions replaced: ' + line)

        sub_result = do_multiplications(line)
        score += sub_result
        print(sub_result)

    print(score)


if __name__ == '__main__':
    main()
