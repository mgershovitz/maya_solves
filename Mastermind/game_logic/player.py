from consts import *


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
        guess = format_player_guess(input(USER_INPUT_PROMPT))
        valid_input = validate_player_guess(guess)

    return guess

