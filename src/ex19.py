from copy import deepcopy as dc


def main():
    with open('../data/ex19.txt') as f:
        lines = f.readlines()
    rule_dict = dict()
    all_rules = list()
    messages = list()

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

    all_rules.append(rule_dict[0][0])
    new_all_rules = list()
    print(all_rules)
    cont = True
    while cont:
        if len(all_rules) % 10000 == 0:
            print('iterating with ' + str(len(all_rules)) + ' rules: ')
        cont = False
        for i, rule in enumerate(all_rules):
            if cont:
                break
            new_rule = dc(rule)
            for j, rule_nr in enumerate(rule):
                if cont:
                    break
                if isinstance(rule_nr, str):
                    continue
                rule_replacement = rule_dict[rule_nr]
                if isinstance(rule_replacement, list):
                    del all_rules[i]
                    cont = True
                    replacement = rule_dict[rule_nr]

                    for rule_option in replacement:
                        new_new_rule = dc(new_rule)
                        del new_new_rule[j]
                        for k, rule_option_nr in enumerate(rule_option):
                            new_new_rule.insert(j+k,rule_option_nr)
                        all_rules.append(new_new_rule)
                elif isinstance(rule_replacement, str):
                    new_rule[j] = rule_replacement
                    all_rules[i] = new_rule
                elif isinstance(rule_replacement, int):
                    new_rule[j] = rule_replacement
                    all_rules[i] = new_rule
                else:
                    print(' error: ' + rule_replacement)

    all_rules_txt = list()
    for rule in all_rules:
        txt_rule = ''.join(rule)
        print(txt_rule)
        all_rules_txt.append(txt_rule)

    score = 0
    for message in messages:
        for rule in all_rules_txt:
            if message.strip() == rule.strip():
                print(message + " to rule " + rule)
                score += 1
                break
    print(str(len(all_rules_txt)) + ' rules')
    print(str(len(messages)) + ' messages')

    print('score = ' + str(score))

if __name__ == '__main__':
    main()
