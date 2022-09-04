# Related blog post - https://algoritmim.co.il/just-code/connect-four-game-in-python/

from four_in_a_row.board import Color

from four_in_a_row.board import BoardUtils


def four_sequence_exists(discs_vector):
    longest_seq = 1
    current_seq = 1
    for i in range(1, len(discs_vector)):
        if discs_vector[i] == discs_vector[i - 1] and not (discs_vector[i] is Color.EMPTY.value):
            current_seq += 1
        if current_seq > longest_seq:
            longest_seq = current_seq
        else:
            current_seq = 1
    return longest_seq == 4


def add_disc(current_color, board, column):
    row = 0
    success = False
    while row < board.rows and not success:
        if board.get(row, column) is Color.EMPTY:
            board.set(row, column, current_color)
            success = True
        else:
            row += 1
    return success


def is_win(board, row, column):
    vector_getters = [BoardUtils.get_row_vector, BoardUtils.get_column_vector, BoardUtils.get_positive_diagonal_vector,
                      BoardUtils.get_negative_diagonal_vector
                      ]
    for getter in vector_getters:
        discs_vector = getter(board, row, column)
        if four_sequence_exists(discs_vector):
            return True
    return False
