from termcolor import colored

class Position(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_neighbours(self):
        return [
            Position(self.x - 1, self.y),
            Position(self.x + 1, self.y),
            Position(self.x, self.y - 1),
            Position(self.x, self.y + 1)
        ]


class Screen(object):
    def __init__(self, base_mat):
        self.mat = base_mat

    def get_color(self, pos):
        return self.mat[pos.x][pos.y]

    def set_color(self, pos, new_color):
        self.mat[pos.x][pos.y] = new_color

    def pos_in_bounds(self, pos):
        return 0 <= pos.x < len(self.mat) and 0 <= pos.y < len(self.mat[0])

    def get_neighbour(self, pos, old_color):
        possible_neighbours = pos.get_neighbours()
        for neighbour in possible_neighbours:
            if self.pos_in_bounds(neighbour) and self.get_color(neighbour) == old_color:
                return neighbour

    def print(self):
        for i in range(0, len(self.mat)):
            row = ""
            for j in range(0, len(self.mat[0])):
                row += colored("\u2588", self.get_color(Position(i, j)))
            print(row)

    def paint_and_fill_recur(self, pos, new_color, old_color):
        if self.get_color(pos) == old_color:
            self.set_color(pos, new_color)
            next_neighbour = self.get_neighbour(pos, old_color)
            if next_neighbour:
                self.paint_and_fill_recur(next_neighbour, new_color, old_color)

    def paint_and_fill(self, pos, new_color):
        self.paint_and_fill_recur(pos, new_color, self.get_color(pos))

class Colors(object):
    W = 'white'
    B = 'blue'
    G = 'green'
    M = 'magenta'
    R = 'red'

def run_tests():
    A = Screen([[Colors.W, Colors.W, Colors.R]])
    print("Before:")
    A.print()
    A.paint_and_fill(Position(0,0), Colors.B)
    print("Paint and fill from (0,0) in blue:")
    A.print()

    A = Screen([[Colors.R]])
    print("Before:")
    A.print()
    A.paint_and_fill(Position(0,0), Colors.B)
    print("Paint and fill from (0,0) in blue:")
    A.print()

    A = Screen([[Colors.W, Colors.W, Colors.W], [Colors.W, Colors.B, Colors.W], [Colors.W, Colors.W, Colors.W]])
    print("Before:")
    A.print()
    A.paint_and_fill(Position(0,0), Colors.B)
    print("Paint and fill from (0,0) in blue:")
    A.print()
    A.paint_and_fill(Position(1,1), Colors.M)
    print("Paint and fill from (1,1) in pink:")
    A.print()

    A = Screen([[Colors.W, Colors.W, Colors.W], [Colors.W, Colors.B, Colors.W], [Colors.W, Colors.W, Colors.W]])
    print("Before:")
    A.print()
    A.paint_and_fill(Position(2,2), Colors.M)
    print("Paint and fill from (2,2) in pink:")
    A.print()
    A.paint_and_fill(Position(1,1), Colors.W)
    print("Paint and fill from (1,1) in white:")
    A.print()


if __name__ == '__main__':
    run_tests()