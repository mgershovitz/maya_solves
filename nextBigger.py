# Related blog post - https://algoritmim.co.il/2020/05/24/next-bigger-number/


def nextBigger(n):
    digits = [int(d) for d in str(n)]
    for i in range(len(digits) - 2, -1, -1):
        for j in range(len(digits) - 1, i, -1):
            if digits[i] < digits[j]:
                digits[i], digits[j] = digits[j], digits[i]
                digits[i+1:] = sorted(digits[i+1:])
                return int(''.join([str(d) for d in digits]))
    return -1


def run_tests():
    assert nextBigger(12) == 21
    assert nextBigger(513) == 531
    assert nextBigger(111) == -1
    assert nextBigger(1144) == 1414
    assert nextBigger(1662) == 2166


if __name__ == '__main__':
    run_tests()
