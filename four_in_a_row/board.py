# Related blog post - https://algoritmim.co.il/just-code/connect-four-game-in-python/

from enum import Enum

ROWS = 6
COLUMNS = 9


class Color(Enum):
    EMPTY = 0
    RED = 1
    BLUE = 2

    def __str__(self):
        return '%s' % self.value


class BoardUtils:

    @staticmethod
    def get_row_vector(board, row, column):
        start = max(0, column - 3)
        end = min(board.columns-1, column + 3)
        vector = []
        for c in range(start, end + 1):
            vector.append(board.get(row, c))
        return vector

    @staticmethod
    def get_column_vector(board, row, column):
        start = max(0, row - 3)
        end = min(board.rows-1, row + 3)
        vector = []
        for r in range(start, end + 1):
            vector.append(board.get(r, column))
        return vector

    @staticmethod
    def get_positive_diagonal_vector(board, row, column):
        start_row = row - 3
        start_column = column - 3

        end_row = row + 3
        end_column = column + 3
        vector = []

        r = start_row
        c = start_column
        while r <= end_row and c <= end_column:
            vector.append(board.get(r, c))
            r += 1
            c += 1
        return vector

    @staticmethod
    def get_negative_diagonal_vector(board, row, column):
        start_row = row + 3
        start_column = column - 3

        end_row = row - 3
        end_column = column + 3
        vector = []

        r = start_row
        c = start_column
        while r >= end_row and c <= end_column:
            vector.append(board.get(r, c))
            r -= 1
            c += 1
        return vector


class Board:
    def __init__(self, rows=ROWS, columns=COLUMNS, state=None):
        self.rows = rows
        self.columns = columns
        if state is None:
            self.init_empty_board()
        else:
            self.state = state

    def __repr__(self):
        result = ""
        for r in range(self.rows - 1, -1, -1):
            row = " ".join([str(self.state[r][c]) for c in range(0, self.columns)])
            result += row + '\n'
        return '\n' + result + '\n'

    def init_empty_board(self):
        self.state = [[Color.EMPTY for _ in range(0, self.columns)] for _ in range(0, self.rows)]

    @classmethod
    def read(cls, rows, columns, input_board):
        board_state = []
        for r in range(rows - 1, -1, -1):
            board_state.append(input_board[r])
        return Board(rows, columns, board_state)

    def get(self, r, c):
        return self.state[r][c] if r >=0 and r < self.rows and c >= 0 and c < self.columns else Color.EMPTY

    def set(self, r, c, val):
        self.state[r][c] = val
