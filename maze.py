# Related blog post - https://algoritmim.co.il/2019/06/18/maze-path/

class MazeCell(object):
    def __init__(self, i, j, is_wall=False, is_exit=False):
        self.i = i
        self.j = j
        self.visited = False
        self.is_wall = is_wall
        self.is_exit = is_exit

    def __eq__(self, other):
        return self.i == other.i and self.j == other.j

    def __repr__(self):
        repr = "%d,%d" % (self.i, self.j)
        if self.visited:
            repr += ',visited'
        if self.is_exit:
            repr += ' (EXIT)'
        return repr


class Maze(object):
    def __init__(self, maze_matrix):
        self.maze = maze_matrix
        self.cells_cache = {}
        self.rows = len(maze_matrix)
        self.columns = len(maze_matrix[0])

    def find_path_to_exit_in_maze(self, start_cell):
        path = [start_cell]
        while len(path) > 0:
            current_cell = path[-1]
            current_cell.visited = True

            adjacent_cell = self.get_available_adjacent_cell(current_cell)
            if adjacent_cell is None:
                path.pop()
            else:
                path.append(adjacent_cell)
                if adjacent_cell.is_exit:
                    return path
        return -1

    def get_cell(self, i, j):
        if (i,j) not in self.cells_cache:
            self.cells_cache[(i,j)] = MazeCell(i, j, self.maze[i][j] == 1, self.maze[i][j] == "EXIT")
        return self.cells_cache[(i,j)]

    def get_available_adjacent_cell(self, cell):
        for (i, j) in [(cell.i - 1, cell.j), (cell.i, cell.j - 1), (cell.i + 1, cell.j), (cell.i, cell.j + 1)]:
            if 0 <= i < self.rows and 0 <= j < self.columns:
                adj = self.get_cell(i,j)
                if adj.visited or adj.is_wall:
                    continue
                else:
                    return adj

        return None


def run_tests():
    maze_matrix = [[1, "ENTERANEC", 1, 1],
                   [1, 0, 0, 1],
                   [1, 0, 1, 1],
                   [1, 0, 0, 1],
                   [1, 1, "EXIT", 1]]
    maze = Maze(maze_matrix)
    expected_path = [MazeCell(0, 1), MazeCell(1, 1), MazeCell(2, 1), MazeCell(3, 1), MazeCell(3, 2),
                     MazeCell(4, 2, is_exit=True)]
    assert maze.find_path_to_exit_in_maze(MazeCell(0, 1)) == expected_path

    maze_matrix = [[1, "ENTERANEC", 1, 1],
                   [1, 0, 0, 1],
                   [1, 1, 1, 1],
                   [1, 0, 0, 1],
                   [1, 1, "EXIT", 1]]
    maze = Maze(maze_matrix)
    assert maze.find_path_to_exit_in_maze(MazeCell(0, 1)) == -1

    maze_matrix = [[1, "ENTERANEC", 1, 1],
                   [1, 1, "EXIT", 1]]
    maze = Maze(maze_matrix)
    assert maze.find_path_to_exit_in_maze(MazeCell(0, 1)) == -1

    maze_matrix = [[1, "ENTERANEC", 1, 1],
                   [1, "EXIT", 1, 1]]
    maze = Maze(maze_matrix)
    expected_path = [MazeCell(0, 1), MazeCell(1, 1, is_exit=True)]
    assert maze.find_path_to_exit_in_maze(MazeCell(0, 1)) == expected_path

    maze_matrix = [["ENTERANEC", 0, 0, "EXIT"]]
    maze = Maze(maze_matrix)
    expected_path = [MazeCell(0, 0), MazeCell(0, 1), MazeCell(0, 2), MazeCell(0,3, is_exit=True)]
    assert maze.find_path_to_exit_in_maze(MazeCell(0, 0)) == expected_path


if __name__ == '__main__':
    run_tests()
