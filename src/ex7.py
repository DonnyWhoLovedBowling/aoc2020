file = open('../data/ex7.txt', 'r')
lines = file.readlines()

bagSet = set()
containsDict = dict()
containedDict = dict()
search = 'shiny gold bag'
total_sub_bags = 0

def count_bags(bag, cnt):
    global containsDict
    global total_sub_bags
    sub_bags = containsDict[bag].keys()
    if len(sub_bags) == 0:
        print('end of the line: ' + str(cnt) + ' ' +  bag )
        total_sub_bags += cnt
    for sub_bag in sub_bags:
        n = containsDict[bag][sub_bag]
        path_cnt = n*cnt
        print('adding ' + str(path_cnt) + '(' + str(n) + ') ' + sub_bag)
        count_bags(sub_bag, path_cnt)
        print('count is now: ' + str(cnt))
        total_sub_bags += cnt


def in_tree(bag, initChain):
    global containsDict
    chain = initChain
    sub_bags = containsDict[bag].keys()
    if search in sub_bags:
        return True, chain
    for sub_bag in sub_bags:
        if sub_bag not in containsDict.keys():
            print('error for sub_bag: ' + sub_bag)
        chain.append(sub_bag)
        success, res_chain = in_tree(sub_bag, chain)
        if success:
            return True, res_chain
    return False, []


for line in lines:
    line = line.replace('bags', 'bag')
    line = line.replace('contains', 'contain')
    line = line.strip('\n')
    line = line.strip('.')
    split = line.split('contain')
    read_bag = split[0].lstrip()
    read_bag = read_bag.rstrip()
    bagSet.add(read_bag)
    containsDict[read_bag] = dict()
    for c in split[1].split(','):
        if 'no other' in c:
            continue
        v = int(c[1])

        k = c[2:]
        k = k.lstrip()
        k = k.rstrip()

        containsDict[read_bag][k] = v
# part 1
# result_bags = set()
# for test_bag in bagSet:
#     if test_bag == search:
#         continue
#     found,result_chain = in_tree(test_bag, [test_bag])
#     if found:
#         print(result_chain)
#         result_bags.add(test_bag)
#
# print(len(result_bags))
count_bags(search, 1)
print(total_sub_bags)