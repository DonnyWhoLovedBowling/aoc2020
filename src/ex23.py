from pycharm_line_profiler import profile

def in_range(_first, _last, _destination):
    if _first < _last:
        return _first <= _destination < _last
    else:
        return _destination >= _first or _destination < _last



def do_run(pt2, test):
    debug_freq = 100
    size = 9
    largest = 0
    n_rounds = 10
    if test:
        size = 50
        input = '389125467'
        debug_freq = 1

    else:
        input = '716892543'
        n_rounds = 100
        largest = 4

    cups = [int(n) for n in list(input)]
    if pt2:
        size = 1000000

    if pt2 or test:
        extra_cups = list(range(10, size+1))
        cups += extra_cups
        largest = size - 1
        n_rounds = size*10

    current = 0
    len_cups = len(cups)
    if test or not pt2:
        print(cups)
    for m in range(1, n_rounds+1):
        if test:
            if largest != cups.index(size):
                print("ERROR: position of largest not correct", largest, cups.index(size), '\n', cups)
                exit()

        current_label = cups[current]
        destination_label = current_label-1
        if destination_label == 0:
            destination_label = size
            destination = largest
        else:
            destination = cups.index(destination_label)
        first = (current + 1) % len(cups)
        last = (current + 4) % len(cups)
        while in_range(first, last, destination):
            destination_label -= 1
            if destination_label == 0:
                destination = largest
                destination_label = size
            else:
                destination = cups.index(destination_label)

        if last > first:
            pick_up = cups[first:last]
            if destination >= last:
                # cups = cups.replace(pick_up, '')
                if largest < first or largest > destination:
                    pass
                elif largest >= last:
                    largest -= 3
                elif first <= largest < last:
                    largest = destination - 3 + (largest - first) + 1
                else:
                    print("ERROR: position of largest not clear", largest, destination, first, last)
                    exit()
                cups = cups[:first] + cups[last:destination+1] + pick_up + cups[destination+1:]

            elif destination < first:
                if largest <= destination or largest >= last:
                    pass
                elif destination < largest < first:
                    largest += 3
                elif first <= largest < last:
                    largest -= (first - destination) - 1
                else:
                    print("ERROR: position of largest not clear 2", largest, destination, first, last)
                    exit()
                cups = cups[:destination+1] + pick_up + cups[destination+1:first] + cups[last:]

            else:
                print("ERROR: destination is in cups")
                exit()
        else:
            pick_up = cups[first:] + cups[:last]
            # if destination >= last:
            #     cups = cups[last:destination+1] + pick_up + cups[:first]
            # else:
            if largest >= first:
                largest = destination + (largest - first) - last + 1
            elif largest < last:
                largest = destination + (size-first) + 1 - last + largest
            elif largest <= destination:
                largest -= last
            elif largest > destination:
                largest += (size-first)
            else:
                print("ERROR: position of largest not clear 3", largest, destination, first, last)
                exit()
            cups = cups[last:destination+1] + pick_up + cups[destination+1:first]

        largest = largest % len(cups)
        current = (cups.index(current_label)+1) % len(cups)
        if (m % debug_freq) == 0:
            print(f"pickup: {pick_up}")
            print(f"current: {current}")
            print(f"current label: {current_label}")

            print(f"destination: {destination}")
            print(f"destination label: {destination_label}")
            print(f"first: {first}")
            if test:
                print(cups)
            print(f"round: {m} \n")


    pivot = cups.index(1)
    if pivot == len(cups)-1:
        final_cups = cups[:-1]
    else:
        final_cups = cups[pivot+1:] + cups[:pivot]

    # print(currents)
    # print(destinations)
    # print(current_labels)
    # print(destination_labels)
    # print(firsts)
    # print(lasts)
    print(final_cups)

if __name__ == '__main__':
    do_run(False, True)