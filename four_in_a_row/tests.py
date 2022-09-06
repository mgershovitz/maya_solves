# Related blog post - https://algoritmim.co.il/just-code/connect-four-game-in-python/

from four_in_a_row.board import Board, Color
from four_in_a_row.logic import add_disc, is_win


def test_add_disc():
    board = Board()
    for i in range(0, board.columns):
        add_disc(Color.BLUE, board, i)
        assert board.get(0, i) == Color.BLUE

    add_disc(Color.RED, board, 1)
    assert (board.get(1, 0)) is Color.EMPTY
    assert (board.get(1, 1)) is Color.RED
    assert (board.get(1, 2)) is Color.EMPTY


def test_is_win_basic():
    board = Board()
    for i in range(0, 4):
        add_disc(Color.BLUE, board, i)
    for i in range(0, 4):
        assert (is_win(board, 0, i) is True)

    board = Board()
    for _ in range(0, 4):
        add_disc(Color.RED, board, 3)
    for i in range(0, 4):
        assert (is_win(board, i, 3) is True)


def test_winning_boards():
    winning_boards_data = [
        {
            'board_state':
                [[0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [1, 1, 1, 1, 0]],
            'pos_r': 0,
            'pos_c': 3
        },
        {
            'board_state':
                [[0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 1, 1, 1, 1]],
            'pos_r': 0,
            'pos_c': 3
        },
        {
            'board_state':
                [[0, 2, 0, 0, 0],
                 [0, 2, 0, 0, 0],
                 [0, 2, 0, 0, 0],
                 [0, 2, 1, 1, 1]],
            'pos_r': 3,
            'pos_c': 1
        },
        {
            'board_state':
                [[0, 2, 0, 0, 2],
                 [0, 1, 0, 2, 2],
                 [0, 2, 2, 1, 2],
                 [0, 2, 1, 1, 1]],
            'pos_r': 1,
            'pos_c': 2
        },
        {
            'board_state':
                [[0, 1, 2, 0, 0],
                 [0, 2, 1, 0, 2],
                 [0, 1, 2, 1, 1],
                 [0, 2, 2, 1, 1]],
            'pos_r': 3,
            'pos_c': 1
        },
        {
            'board_state':
                [[0, 0, 0, 0, 2],
                 [2, 1, 0, 2, 2],
                 [1, 2, 1, 1, 2],
                 [2, 2, 1, 1, 2]],
            'pos_r': 3,
            'pos_c': 4
        }
    ]
    for entry in winning_boards_data:
        board = Board.read(4, 5, entry['board_state'])
        assert (is_win(board, entry['pos_r'], entry['pos_c']) is True)


def test_no_win_boards():
    winning_boards_data = [
        {
            'board_state':
                [[0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [1, 2, 1, 1, 1]],
            'pos_r': 0,
            'pos_c': 3
        },
        {
            'board_state':
                [[0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 1, 1, 1, 0]],
            'pos_r': 0,
            'pos_c': 3
        },
        {
            'board_state':
                [[0, 2, 0, 0, 0],
                 [0, 1, 0, 0, 0],
                 [0, 2, 0, 0, 0],
                 [0, 2, 1, 1, 1]],
            'pos_r': 3,
            'pos_c': 1
        },
        {
            'board_state':
                [[0, 2, 0, 0, 2],
                 [0, 1, 0, 2, 2],
                 [0, 2, 1, 1, 2],
                 [0, 2, 1, 1, 1]],
            'pos_r': 3,
            'pos_c': 4
        },
        {
            'board_state':
                [[0, 2, 0, 0, 2],
                 [2, 1, 0, 2, 2],
                 [1, 2, 1, 1, 2],
                 [2, 2, 1, 1, 1]],
            'pos_r': 2,
            'pos_c': 1
        },
        {
            'board_state':
                [[0, 0, 0, 0, 0],
                 [2, 1, 0, 2, 2],
                 [1, 2, 1, 1, 2],
                 [2, 2, 1, 1, 2]],
            'pos_r': 2,
            'pos_c': 4
        }
    ]
    for entry in winning_boards_data:
        board = Board.read(4, 5, entry['board_state'])
        assert (is_win(board, entry['pos_r'], entry['pos_c']) is False)


if __name__ == '__main__':
    test_add_disc()
    test_is_win_basic()
    test_winning_boards()
    test_no_win_boards()
