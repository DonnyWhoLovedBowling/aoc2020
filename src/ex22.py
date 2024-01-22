from copy import deepcopy as dc


def compare_decks(d1, d2):
    if len(d1) == len(d2):
        for i in range(len(d1)):
            if d1[i] != d2[i]:
                return False
        return True
    return False


def run(cards_p1, cards_p2, pt2=False, depth=0):
    memory = ([], [])
    p1_wins = False
    game_over = False
    while not game_over:
        if pt2:
            for d in memory[0]:
                if compare_decks(d, cards_p1):
                    game_over = True
                    break
            for d in memory[1]:
                if compare_decks(d, cards_p2):
                    game_over = True
                    break
            if game_over:
                break
            memory[0].append(dc(cards_p1))
            memory[1].append(dc(cards_p2))

        p1 = cards_p1.pop()
        p2 = cards_p2.pop()
        if p1 <= len(cards_p1) and p2 <= len(cards_p2) and pt2:
            p1_wins = run(cards_p1[-min(len(cards_p1), p1):], cards_p2[-min(len(cards_p2), p2):], True, depth+1)
        else:
            p1_wins = p1 > p2
        if p1_wins:
            cards_p1 = [p2, p1] + cards_p1
        else:
            cards_p2 = [p1, p2] + cards_p2
        game_over = not (cards_p1 and cards_p2)

    if depth == 0:
        print(cards_p1, cards_p2)
        win_cards = cards_p1 if cards_p1 else cards_p2
        total = 0
        for i, c in enumerate(win_cards):
            total += (i+1)*c
        print(f"ans pt1 = {total}")
    else:
        return len(cards_p1) > 0


if __name__ == '__main__':
    lines_p1, lines_p2 = [line.split('\n') for line in open('../data/ex22.txt', 'r').read().split('\n\n')]

    cards_p1_glob, cards_p2_glob = [], []
    for line in range(1, len(lines_p1)):
        cards_p1_glob.append(int(lines_p1[line]))
        cards_p2_glob.append(int(lines_p2[line]))

    cards_p1_glob = list(reversed(cards_p1_glob))
    cards_p2_glob = list(reversed(cards_p2_glob))

    run(dc(cards_p1_glob), dc(cards_p2_glob), False)
    run(dc(cards_p1_glob), dc(cards_p2_glob), True)
