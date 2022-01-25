from collections import Counter


def check_player_guess_no_duplicates(code, guess):
    code_set = set(code)
    bul = 0
    pgia = 0
    for i in range(0, len(guess)):
        color = guess[i]
        if color == code[i]:
            bul += 1
        elif color in code_set:
            pgia += 1

    return bul, pgia


def check_player_guess_with_duplicates(code, guess):
    code_counter = Counter(code)
    bul = 0
    pgia = 0
    for i in range(0, len(guess)):
        color = guess[i]
        if color == code[i]:
            bul += 1
            decrease_color(code_counter, color)

    for i in range(0, len(guess)):
        color = guess[i]
        if color in code_counter:
            pgia += 1
            decrease_color(code_counter, color)

    return bul, pgia


def decrease_color(code_counter, color):
    if color in code_counter:
        updated_color_count = code_counter.pop(color) - 1
        if updated_color_count > 0:
            code_counter[color] = updated_color_count
