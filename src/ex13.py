from math import prod
from copy import deepcopy as dc

file = open('../data/ex13.txt', 'r')
lines = file.readlines()
line2 = lines[1].replace('\n','')
line2_list = line2.split(',')
min_time = int(lines[0])
buses = [int(n) for n in line2_list if n.isnumeric()]


def next_bus_stop(now, bus_id):
    rem = (now % bus_id)
    nxt = now + (bus_id - rem)
    return nxt


def check(bus_times):
    global dists
    correct = 0
    real_dists = []
    for i, dist in enumerate(dists):
        this_dist = bus_times[i+1]-bus_times[i]
        real_dists.append(this_dist)
        if this_dist == dist:
            correct += 1
    return correct


def calc_result():
    global buses
    times = [0]*len(buses)
    n_correct = 0
    increment = buses[0]
    itr = 0
    while True:
        itr += 1
        # if itr > 40:
        #     break
        n_correct_new = check(times)
        if n_correct_new > n_correct:
            n_correct = n_correct_new

            increment = prod(buses[0:n_correct+1])
            print('new increment: ' + str(increment))
            if n_correct == len(buses)-1:
                print(itr)
                print(times)
                break
        times[0] += increment
        for i in range(1, n_correct+2):
            times[i] = next_bus_stop(times[i-1], buses[i])

print(prod(buses))

best_bus = 999
best_wait_time = 999
for bus in buses:
    wait_time = (min_time % bus)
    if wait_time > 0:
        wait_time = bus-wait_time
    if wait_time < best_wait_time:
        best_wait_time = wait_time
        best_bus = bus

print(best_wait_time)
print(best_bus)
print(best_bus*best_wait_time)

dists = []
last_i = 0
for i, b in enumerate(line2_list[1:]):
    if b.isnumeric():
        dists.append((i-last_i)+1)
        last_i = i+1


print(buses)
print(dists)
calc_result()
