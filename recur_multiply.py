# Related blog post - https://mayareads.blog/2019/06/20/recur-multiply/

class Multiplier(object):
    def __init__(self):
        self.results_cache = {}

    def recur_multiply(self, a, b):
        if a == 0:
            return 0
        if b not in self.results_cache:
            if b == 0:
                self.results_cache[0] = 0
            elif b == 1:
                self.results_cache[1] = a
            elif b % 2 == 0:
                if b / 2 not in self.results_cache:
                    self.results_cache[b / 2] = self.recur_multiply(a, b / 2)
                self.results_cache[b] = self.results_cache[b / 2] + self.results_cache[b / 2]
            else:
                self.results_cache[(b - 1) / 2] = self.recur_multiply(a, (b - 1) / 2)
                self.results_cache[b] = self.results_cache[(b - 1) / 2] + \
                                        self.results_cache[(b - 1) / 2] + \
                                        self.recur_multiply(a, 1)
        return self.results_cache[b]

    def multiply(self, a, b):
        if a > b:
            return self.recur_multiply(a, b)
        else:
            return self.recur_multiply(b, a)

def run_tests():
    assert Multiplier().multiply(3, 10) == 30
    assert Multiplier().multiply(10, 3) == 30
    assert Multiplier().multiply(3, 0) == 0
    assert Multiplier().multiply(0, 10) == 0
    assert Multiplier().multiply(pow(2, 3), pow(2, 10)) == 8192


if __name__ == '__main__':
    run_tests()