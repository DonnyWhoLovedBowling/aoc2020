def in_range(_first, _last, _destination):
    if _first < _last:
        return _first <= _destination < _last
    else:
        return _destination >= _first or _destination < _last

destinations = []
currents = []
firsts = []
lasts = []

cups = '716892543'
current = 0
len_cups = len(cups)
for m in range(1, 101):
    for c in cups:
        if cups.count(c) > 1:
            print("ERROR", cups)
            exit()
    if len(cups) != len_cups:
        print("ERROR", cups)
        exit()
    current_label = cups[current]
    destination = cups.find(str(int(current_label)-1))
    if destination == -1:
        destination = cups.find('9')
    first = (current + 1) % len(cups)
    last = (current + 4) % len(cups)
    destination_label = cups[destination]

    while in_range(first, last, destination):
        destination_label = int(cups[destination])
        destination = cups.find(str(destination_label - 1))
        destination_label = destination_label - 1
        if destination == -1:
            if destination_label == 0:
                destination_label = 9
                destination = cups.find(str(destination_label))
            else:
                print("ERROR, strange destination situation", destination, destination_label)
                exit()
    destinations.append(destination)
    if last > first:
        pick_up = cups[first:last]
        if destination >= last:
            cups = cups.replace(pick_up, '')
            destination = cups.find(str(destination_label))
            cups = cups[:destination+1] + pick_up + cups[destination+1:]
        elif destination < first:
            cups = cups[0:destination+1] + pick_up + cups[destination+1:first] + cups[last:]
        else:
            print("ERROR: destination is in cups")
    else:
        pick_up = cups[first:] + cups[:last]
        # if destination >= last:
        #     cups = cups[last:destination+1] + pick_up + cups[:first]
        # else:
        cups = cups[last:destination+1] + pick_up + cups[destination+1:first]

    current = (cups.find(current_label)+1) % len(cups)
    print(f"pickup: {pick_up}")
    print(f"destination: {destination_label}")
    print()
    currents.append(current)
    firsts.append(first)
    lasts.append(last)

pivot = cups.find('1')
if pivot == len(cups)-1:
    final_cups = cups.replace('1', '')
else:
    final_cups = cups[pivot+1:] + cups[:pivot]
print(currents)
print(destinations)
print(firsts)
print(lasts)
print(final_cups)

