file = open('../data/ex9.txt', 'r')
lines = file.readlines()

nums = [int(line) for line in lines]
pt1 = 0
for i, num_ans in enumerate(nums[25:]):
    found = False
    for j, num1 in enumerate(nums[i:i+25]):
        if found:
            break
        for k, num2 in enumerate(nums[i:i + 25]):
            if(num1+num2 == num_ans):
                found = True
                break
    if not found:
        print((i+25, num_ans))
        pt1 = num_ans
        break

found = False
for i in range(0, len(nums)):
    num_list = []
    if found:
        break
    total = 0
    found = False
    for j, num1 in enumerate(nums[i:]):
        total += num1
        num_list.append(num1)
        if total == pt1:
            print('i = ' + str(i))
            print('j = ' + str(j))
            print(min(num_list)+max(num_list))
            found = True
            break

