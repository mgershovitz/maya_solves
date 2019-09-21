# Related blog post - https://mayareads.blog/2019/06/23/jump-game/

class JumpGame(object):
    def __init__(self):
        self.jumps = {}
        self.arr = None

    def can_finish_from_index(self, i):
        if i >= len(self.arr):
            self.jumps[i] = False
        elif i == len(self.arr) - 1:
            self.jumps[i] = True
        elif self.arr[i] == 0:
            self.jumps[i] = False
        else:
            self.jumps[i] = False
            for jump_size in range(1, self.arr[i]+1):
                if i + jump_size not in self.jumps:
                    self.jumps[i + jump_size] = self.can_finish_from_index(i + jump_size)
                    self.jumps[i] = self.jumps[i] or self.jumps[i + jump_size]
        return self.jumps[i]

    def can_finish_game(self, arr):
        self.arr = arr
        return self.can_finish_from_index(0)

def run_tests():
    assert JumpGame().can_finish_game([]) is False
    assert JumpGame().can_finish_game([0]) is True
    assert JumpGame().can_finish_game([1, 2, 0, 3]) is True
    assert JumpGame().can_finish_game([2, 1, 0, 1]) is False


if __name__ == '__main__':
    run_tests()