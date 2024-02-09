def transform(value, _subject):
    value *= _subject
    return value % 20201227


if __name__ == '__main__':
    card = 17115212
    door = 3667832
    # card = 5764801
    # door = 17807724
    found, i, card_loop, door_loop, current_key = 0, 0, 0, 0, 1
    while found != 2:
        i += 1
        current_key = transform(current_key, 7)
        if current_key == card:
            card_loop = i
            found += 1
            print("found card! ", i)
        elif current_key == door:
            door_loop = i
            found += 1
            print("found door! ", i)

    subject = door
    current_key = 1
    for _ in range(card_loop):
        current_key = transform(current_key, subject)
    print(f"encryption key: {current_key}")
    subject = card
    current_key = 1
    for _ in range(door_loop):
        current_key = transform(current_key, subject)
    print(f"encryption key check: {current_key}")


