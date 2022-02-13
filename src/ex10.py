import itertools

file = open('../data/ex10.txt', 'r')
lines = file.readlines()

def compute_combis(i):
    combs = 0
    test_list = list(range(1, i+1))
    for j in range(0, len(test_list)+1):
        comb_list = list(itertools.combinations(test_list, j))
        for comb in comb_list:
            combl = list(comb)
            combl.append(i+1)
            combl.append(0)
            combl.sort()
            correct = True
            last = 0

            for num in combl:
                if num - last > 3:
                    correct = False
                    break
                last = num
            if correct:
                combs += 1
    return combs


nums = [int(line) for line in lines]
nums.append(0)
nums.append(max(nums)+3)
nums.sort()
print(nums)
ones = 0
threes = 0
for i,num in enumerate(nums[1:]):
    if num - nums[i] == 1:
        ones += 1
    if num - nums[i] == 3:
        threes += 1
#part1
print(ones)
print(threes)
print(ones*threes)

ones_list = []
ones = 0
nums.append(0)
nums.sort()
for i,num in enumerate(nums):
    if i == 0:
        ones += 1
    elif num - nums[i-1] == 1:
        ones += 1
    elif num - nums[i-1] == 3:
        if ones > 1:
            ones_list.append(ones)
        ones = 1
        threes += 1
print(ones_list)

score = 1
for ones in ones_list:
    print(ones)
    score *= compute_combis(ones-2)
    print(score)

print(score)