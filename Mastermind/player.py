from consts import *


def check_player_guess(code, code_set, guess):
    bul = 0
    pgia = 0
    for i in range(0, len(guess)):
        color = guess[i]
        if color == code[i]:
            bul += 1
        elif color in code_set:
            pgia += 1

    return bul, pgia


def validate_player_guess(player_guess):
    valid_input = True
    if len(player_guess) != CODE_LENGTH:
        print("Guess should be {} colors long".format(CODE_LENGTH))
        valid_input = False

    for item in player_guess:
        if item not in COLORS:
            print("Bad input: {}".format(item))
            valid_input = False

    return valid_input


def format_player_guess(player_guess):
    guess = player_guess.split(" ")
    formatted_guess = []
    for item in guess:
        if item in COLORS_DICT:
            formatted_guess.append(COLORS_DICT.get(item))
        else:
            formatted_guess.append(item)
    return formatted_guess


def get_player_guess():
    guess = format_player_guess(input(USER_INPUT_PROMPT))
    valid_input = validate_player_guess(guess)

    while not valid_input:
        guess = format_player_guess(input(USER_INPUT_PROMPT).split(" "))
        valid_input = validate_player_guess(guess)

    return guess

