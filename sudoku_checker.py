from math import sqrt


def check_valid_vector(vector):
    for i in range(1, 10):
        if vector.count(i) != 1:
            return False
    return True


def check_row_and_columns_are_valid(sudoku):
    for i in range(0, 9):
        row = sudoku[i]
        if not check_valid_vector(row):
            return False
        column = [sudoku[j][i] for j in range(0, 9)]
        if not check_valid_vector(column):
            return False
    return True


def check_cubes_are_valid(sudoku, board_size):
    cube_size = int(sqrt(board_size))
    for cube_row in range(0, cube_size):
        for cube_column in range(0, cube_size):
            cube = []
            for i in range(0, cube_size):
                for j in range(0, cube_size):
                    row = cube_row * cube_size + i
                    column = cube_column * cube_size + j
                    cube.append(sudoku[row][column])
            if not check_valid_vector(cube):
                return False
    return True


def check_sudoku_is_valid(sudoku):
    board_size = len(sudoku)
    return check_row_and_columns_are_valid(sudoku) and check_cubes_are_valid(sudoku, board_size)


def run_tests():
    valid_sudoku = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
                    [6, 7, 2, 1, 9, 5, 3, 4, 8],
                    [1, 9, 8, 3, 4, 2, 5, 6, 7],
                    [8, 5, 9, 7, 6, 1, 4, 2, 3],
                    [4, 2, 6, 8, 5, 3, 7, 9, 1],
                    [7, 1, 3, 9, 2, 4, 8, 5, 6],
                    [9, 6, 1, 5, 3, 7, 2, 8, 4],
                    [2, 8, 7, 4, 1, 9, 6, 3, 5],
                    [3, 4, 5, 2, 8, 6, 1, 7, 9]]
    assert check_sudoku_is_valid(valid_sudoku)

    not_valid_sudoku = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
                        [6, 7, 2, 1, 9, 5, 3, 4, 8],
                        [1, 9, 8, 3, 4, 2, 5, 6, 7],
                        [8, 5, 9, 7, 6, 1, 4, 2, 3],
                        [4, 2, 6, 8, 5, 3, 7, 9, 1],
                        [7, 1, 3, 9, 2, 4, 8, 5, 6],
                        [9, 6, 1, 5, 3, 7, 2, 8, 4],
                        [2, 8, 7, 4, 1, 9, 6, 3, 5],
                        [3, 4, 7, 2, 8, 6, 1, 5, 9]]

    assert not check_sudoku_is_valid(not_valid_sudoku)

if __name__ == '__main__':
    run_tests()
