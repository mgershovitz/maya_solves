def revers_bits(x):
    result = 0
    for i in range(0, 32):
        current_bit = x >> i & 1
        result = result | current_bit << (32 - i - 1)
    return result


def run_tests():
    assert revers_bits(0) == 0
    assert revers_bits(1) == pow(2, 31)
    assert revers_bits(pow(2, 31)) == 1
    assert revers_bits(pow(2, 31) + 1) == pow(2, 31) + 1



if __name__ == '__main__':
    run_tests()
