def string_to_list(range_string):
    stripped = range_string.strip()
    splt = stripped.split('-')
    begin = int(splt[0])
    end = int(splt[1])
    return list(range(begin, end+1))


def parse_ranges(line):
    first_split = line.split(':')
    ranges = first_split[1].split('or')
    s = set()
    s.update(string_to_list(ranges[0]))
    s.update(string_to_list(ranges[1]))
    return s


def run():
    f = open('../data/ex16.txt', 'r')
    lines = f.readlines()
    my_ticket = []
    other_tickets = []
    yt = False
    ot = False
    do_labels = True
    label_dict = dict()
    all_valid_values = set()
    labels = []
    label_possibilities = dict()
    label_answers = dict()

    for line in lines:
        line = line.replace('\n', '').strip()
        if line == '':
            continue
        elif 'your ticket' in line:
            do_labels = False
            yt = True
        elif yt:
            yt = False
            my_ticket = list(map(int, line.split(',')))
        elif 'nearby ticket' in line:
            ot = True
        elif ot:
            lst = list(map(int, line.split(',')))
            other_tickets.append(lst)
        elif do_labels:
            label = line.split(':')[0]
            labels.append(label)
            s = parse_ranges(line)
            label_dict[label] = s
            all_valid_values = all_valid_values.union(s)

    for label in labels:
        label_possibilities[label] = [True]*len(labels)

    score = 0
    valid_tickets = []
    for ticket in other_tickets:
        valid = True
        for t in ticket:
            if t not in all_valid_values:
                score += t
                valid = False
        if valid:
            valid_tickets.append(ticket)
    print(score)

    for ticket in valid_tickets:
        for i, t in enumerate(ticket):
            for label in labels:
                if t not in label_dict[label]:
                    label_possibilities[label][i] = False

    while len(label_answers.keys()) < len(labels):
        for label in labels:
            if label_possibilities[label].count(True) == 1:
                ix = label_possibilities[label].index(True)
                label_answers[label] = ix
                for label2 in labels:
                    if label == label2:
                        continue
                    label_possibilities[label2][ix] = False

    score = 1
    for label in labels:
        if 'departure' in label:
            score *= my_ticket[label_answers[label]]
    print(score)
run()
