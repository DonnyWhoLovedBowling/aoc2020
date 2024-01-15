lines = open('../data/ex21.txt', 'r').read().replace(')', '').split('\n')
products = [(set(line.split(' (contains ')[0].split(' ')).difference({''}), set(line.split(' (contains ')[1].split(', ')).difference({''})) for line in lines]


def run():
    allergens = {a.strip() for _, second_set in products for a in second_set}
    all_ingredients = {i.strip() for first_set, _ in products for i in first_set}
    could_be = {a: set.intersection(*[first_set for first_set, second_set in products for i in first_set if a in second_set and i != '']) for a in allergens}

    possible_ingredients = set.union(*could_be.values())
    impossible_ingredients = all_ingredients.difference(possible_ingredients)
    ans = sum([len(p[0].intersection(impossible_ingredients)) for p in products])
    print(f"ans pt1 = {ans}")

    ans2 = []
    matched_allergens = set()
    while len(matched_allergens) != len(allergens):
        for a, ingredients in could_be.items():
            if len(ingredients) == 1:
                ing = ingredients.pop()
                ans2.append((a, ing))
                matched_allergens.add(ing)
            else:
                could_be[a] = could_be[a].difference(matched_allergens)
    print(f"ans pt2 = {','.join([a[1] for a in sorted(ans2, key=lambda x: x[0])])}")


if __name__ == '__main__':
    run()
