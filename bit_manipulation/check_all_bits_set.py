def exact_bit_set(x, y, z):
    n1 = 1 << (x - 1)
    n2 = 1 << (y - 1)
    N = n1 | n2
    return z == N


def run_tests():
    assert exact_bit_set(2, 8, 20) is False
    assert exact_bit_set(1, 3, 20) is False
    assert exact_bit_set(1, 3, 5) is True
    assert exact_bit_set(1, 11, 1025) is True


if __name__ == '__main__':
    run_tests()
