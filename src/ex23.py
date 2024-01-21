cups = '389125467'
current = 0
for _ in range(10):
    print(f"cups: {cups}")
    current_label = int(cups[current])
    print(f"current: {current_label}")
    destination = cups.find(str(current_label-1))
    first = (current + 1) % len(cups)
    last = (current + 4) % len(cups)
    destination_label = cups[destination]
    while first <= destination < last:
        destination_label = int(cups[destination])
        destination = cups.find(str(destination_label - 1))
        if destination == '0':
            destination_label = cups[-1]
            destination = len(cups) - 1

    if last > first:
        pick_up = cups[first:last]
        if destination >= last:
            cups = cups.replace(pick_up, '')
            destination = cups.find(str(destination_label))
            cups = cups[:destination+1] + pick_up + cups[destination+3:]
        elif destination < first:
            cups = cups[0:destination+1] + pick_up + cups[last:]
        else:
            print("ERROR: destination is in cups")
    else:
        pick_up = cups[first:] + cups[:last]
        cups = cups[last:destination+1] + pick_up + cups[destination+1:]

    new_current = last + 1 % len(cups)
    print(f"pickup: {pick_up}")
    print(f"destination: {destination_label}")
