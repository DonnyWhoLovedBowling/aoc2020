file = open('../data/ex1.txt', 'r')
lines = file.readlines()
nums = [int(x) for x in lines]

stop = False
for x in nums:
    if stop:
        break
    for y in nums:
        if x == y:
            continue
        if stop:
            break
        for z in nums:

            if stop:
                break
            if z == y or z == x:
                continue
            if x + y + z == 2020:
                print(x * y * z)
                stop = True
