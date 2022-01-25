from collections import Counter

from app.game_logic.checkers import check_player_guess_with_duplicates


def test_check_duplicates_in_guess_not_scored_twice():
    code = ["red", "blue", "green"]

    guess1 = ["red", "red", "red"]
    assert check_player_guess_with_duplicates(code, guess1) == (1, 0)

    guess2 = ["blue", "blue", "blue"]
    assert check_player_guess_with_duplicates(code, guess2) == (1, 0)

    guess3 = ["blue", "blue", "red"]
    assert check_player_guess_with_duplicates(code, guess3) == (1, 1)
