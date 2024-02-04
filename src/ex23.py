def print_cups(links, current):
    cursor = 1
    ans = 'cups: '
    for _ in range(len(links)):
        cursor = links[cursor]
        if cursor == current:
            ans += f"({cursor})"
        else:
            ans += str(cursor)
    print(ans)


def do_run(pt2, test):
    size = 9
    n_rounds = 10
    if test:
        input = '389125467'
    else:
        input = '716892543'
        n_rounds = 100

    cups = [int(n) for n in list(input)]
    if pt2:
        size = 1000000

    if pt2 or test:
        extra_cups = list(range(10, size+1))
        cups += extra_cups
        n_rounds = size*10

    current = cups[0]
    links = dict()
    for i,  c in enumerate(cups):
        links[c] = cups[(i+1) % len(cups)]
    if not pt2:
        print_cups(links, current)

    for m in range(1, n_rounds+1):
        pickup = [links[current]]
        pickup.append(links[pickup[-1]])
        pickup.append(links[pickup[-1]])
        destination = current-1
        if destination == 0:
            destination = size
        while destination in pickup:
            destination -= 1
            if destination == 0:
                destination = size
        links[current] = links[pickup[-1]]
        buf = links[destination]
        links[destination] = pickup[0]
        links[pickup[-1]] = buf

        current = links[current]
    if pt2:
        first = links[1]
        second = links[first]
        print(f"ans pt2 = {first*second}")
    else:
        print("ans pt1 = ")
        print_cups(links, -1)


if __name__ == '__main__':
    do_run(False, False)
    do_run(True, False)
