from regex import  fullmatch
from itertools import chain
# mport (sys, os)
#
# sys.setrecursionlimit(10000)

rule_dict = dict()
all_rules = list()
messages = list()


def extend_rule(rule: list, pt2=False, depth=0):
    if isinstance(rule, str):
        return rule
    # if isinstance(rule, int):
    #     return extend_rule(rule)
    if depth > 50:
        return ''
    new_rule = []
    for sub_rule in rule:
        new_sub_rule = ''
        for sub_sub_rul in sub_rule:
            # if sub_sub_rul == 8 and pt2:
            #     new_sub_rule += f"({extend_rule(rule_dict[42], pt2)}){{1,2}}"
            # elif sub_sub_rul == 31 and sub_rule == [42, 42, 31] and pt2 and depth < 100:
            #     new_sub_rule += f"({extend_rule(rule_dict[sub_sub_rul], True, depth+1)})"
            # else:
            new_sub_rule += extend_rule(rule_dict[sub_sub_rul], pt2, depth+1)
        new_rule.append(new_sub_rule)

    return f"({'|'.join(new_rule)})"


def main():
    with open('../data/ex19.txt') as f:
        lines = f.readlines()
    global rule_dict, messages, all_rules

    lines = [line.replace('\n', '').strip() for line in lines]
    for line in lines:
        if line == '':
            continue
        if ':' not in line:
            messages.append(line)
            continue
        split_line = line.split(':')

        if 'a' in line:
            rule_dict[int(split_line[0])] = 'a'
            continue
        if 'b' in line:
            rule_dict[int(split_line[0])] = 'b'
            continue

        options = [element for element in split_line[1].split('|') if element != '']
        num_list = [element for element in options[0].split(' ') if element != '']
        options1 = list(map(int, num_list))

        if len(options) > 1:
            num_list = [element for element in options[1].split(' ') if element != '']
            options2 = list(map(int, num_list))
            rule_dict[int(split_line[0])] = [options1, options2]
        else:
            rule_dict[int(split_line[0])] = [options1]

    print(rule_dict[0])
    print(rule_dict[1])
    regex_rule = extend_rule(rule_dict[0])
    print(regex_rule)
    score = 0
    for m in messages:
        if fullmatch(regex_rule, m):
            score += 1
    print('score = ' + str(score))
    rule_dict[8] = [[42], [42, 8]]
    rule_dict[11] = [[42, 31], [42, 11, 31]]
    # 8: 42 | 42 42 | 42 42 | 42 42 | 42 8
    # 11: 42 31 | 42 42 31 | 42 42 31 | 42 42 31 | 42 11 31 31 31 31
    regex_rule = extend_rule(rule_dict[0], True)
    print(regex_rule)
    score = 0
    for m in messages:
        if fullmatch(regex_rule, m):
            score += 1
    print('score = ' + str(score))


if __name__ == '__main__':
    main()
