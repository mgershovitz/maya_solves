import random

from consts import *
from player import get_player_guess, check_player_guess


def generate_code():
    code = []
    for i in range(0, CODE_LENGTH):
        code.append(random.choice(COLORS))
    return code


def play():
    computer_code = generate_code()
    computer_code_set = set(computer_code)

    game_won = False
    rounds = 0
    while not game_won and rounds < TOTAL_ROUNDS:
        player_guess = get_player_guess()
        bul, pgia = check_player_guess(computer_code, computer_code_set, player_guess)
        if bul == CODE_LENGTH:
            game_won = True
            break
        else:
            print(USER_SCORE.format(bul, pgia))
            rounds += 1

    if game_won:
        print(USER_WON)
    else:
        print(USER_LOST)


if __name__ == '__main__':
    play()
