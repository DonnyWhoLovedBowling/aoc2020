def parse_operation(ix, line, left, expect_bracket):
    total = 0
    if left == 0:
        if line[ix] == '(':
            ix, left = parse_operation(ix+1, line, 0, True)
        else:

            left = int(line[ix])
            ix += 1

    operator = line[ix]
    ix += 1

    if line[ix] == '(':
        ix, right = parse_operation(ix+1, line, 0, True)
    else:
        right = int(line[ix])
        ix += 1

    if operator == '+':
        total = left + right
    else:
        total = left * right

    if expect_bracket:
        if line[ix] == ')':
#            print(') found, ix,line[ix] = ' + str((ix, line[ix+1])))
            return ix+1, total
        else:
            return parse_operation(ix, line, total, expect_bracket)
    else:
        return ix, total

    return ix, total


def main():
    with open('../data/ex18.txt') as f:
        lines = f.readlines()
    lines = [line.replace(' ', '').replace('\n', '') for line in lines if line.strip()]
    score = 0
    for line in lines:
        ix = 0
        left = 0
        print('new line: ' + line )
        while ix < (len(line)-1):
            ix, left = parse_operation(ix, line, left, False)
        print('subresult: ' + str(left))
        score += left
    print(score)


if __name__ == '__main__':
    main()