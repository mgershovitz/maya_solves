def get_number_description(num):
    res = ""
    current_count = 1
    current_digit = num[0]
    for i in range(1, len(num)):
        if num[i] == current_digit:
            current_count += 1
        else:
            res = res + str(current_count) + current_digit
            current_digit = num[i]
            current_count = 1
    res = res + str(current_count) + current_digit
    return int(res)


def get_nth_descriptive(n):
    if n == 1:
        return 1
    else:
        i = 1
        current_number = 1
        while i < n:
            current_number = get_number_decription(str(current_number))
            i += 1

        return current_number

def run_tests():
    assert get_nth_descriptive(1) == 1
    assert get_nth_descriptive(2) == 11
    assert get_nth_descriptive(5) == 111221
    assert get_nth_descriptive(10) == 13211311123113112211


if __name__ == '__main__':
    run_tests()