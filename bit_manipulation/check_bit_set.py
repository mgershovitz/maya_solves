def bit_set(x, y):
    mask = 1 << (y - 1)
    return (x & mask) != 0


def run_tests():
    assert bit_set(5, 1) is True
    assert bit_set(5, 2) is False
    assert bit_set(5, 3) is True
    assert bit_set(15, 3) is True
    assert bit_set(0, 3) is False
    assert bit_set(0, 30) is False


if __name__ == '__main__':
    run_tests()
