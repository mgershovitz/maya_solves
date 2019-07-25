def find_single_number(arr):
    result = arr[0]
    for n in arr[1:]:
        result = result ^ n
    return result


def run_tests():
    arr = [0]
    assert find_single_number(arr) == 0

    arr = [1, 1, 2, 3, 3]
    assert find_single_number(arr) == 2

    arr = [2, 1, 1, 3, 3, 1, 1]
    assert find_single_number(arr) == 2


if __name__ == '__main__':
    run_tests()
