def get_all_powers_of_two(x):
    res = []
    power_of_two = 1
    while power_of_two <= x:
        if power_of_two & x != 0:
            res.append(power_of_two)
        power_of_two = power_of_two << 1
    return res


def run_tests():
    assert get_all_powers_of_two(330) == [2, 8, 64, 256]
    assert get_all_powers_of_two(3) == [1, 2]
    assert get_all_powers_of_two(22) == [2, 4, 16]
    assert get_all_powers_of_two(0) == []
    assert get_all_powers_of_two(1) == [1]


if __name__ == '__main__':
    run_tests()
