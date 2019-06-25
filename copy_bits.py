def copy_bits(N, M, i, j):
    x = -1 << i
    y = (1 << j+1) - 1
    mask = ~(x & y)
    N = N & mask
    M = M << i
    return N | M

def run_tests():
    assert copy_bits(0, 0, 2, 6) == 0
    assert copy_bits(1, 0, 2, 6) == 1
    assert copy_bits(1, 0, 0, 1) == 0

    assert copy_bits(int('10001111100', 2), int('10011', 2), 2, 6) == int('10001001100', 2)
    assert copy_bits(int('11111111111', 2), int('0000', 2), 5, 8) == int('11000011111', 2)


if __name__ == '__main__':
    run_tests()