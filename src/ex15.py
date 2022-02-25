starting = [1, 20, 11, 6, 12, 0]
# starting = [0, 3, 6]

last_occurrence = dict()

last_number = starting[0]

for i in range(1, 30000000):
    if i < len(starting):
        new_number = starting[i]
        # print('starting: ' + str(last_number))
    elif last_number in last_occurrence.keys():
        lc = last_occurrence[last_number]
        ln = last_number
        new_number = i-lc-1
        # print(str(ln) + ' in keys, i= ' + str(i) + ' last occurrence: ' + str(lc) + ' new number: ' + str(new_number))
    else:
        new_number = 0
        last_occurrence[last_number] = i-1
        # print('not in keys: ' + str(last_number))
    last_occurrence[last_number] = i-1
    last_number = new_number

print(last_occurrence)
print(new_number)

