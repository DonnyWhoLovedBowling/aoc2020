cups = '389125467'
current = 0
for _ in range(10):
    current_label = int(cups[current])
    destination = cups.find(str(current_label-1))
    first = (current + 1) % len(cups)
    last = (current + 4) % len(cups)
    while first <= destination < last:
        destination_label = int(cups[destination])
        destination = cups.find(str(destination_label - 1))
        if destination == '0':
            destination = cups[-1]

    if last > first:
        pick_up = cups[first:last]
    else:
        pick_up = cups[first:] + cups[:last]

    new_current = last + 1 % len(cups)
    cups = cups[:min(first, last)] + cups[last] + cups[first:last] + cups[last]