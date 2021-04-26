def fibsum(N):
    if N == 0:
        return 0

    previous = 0
    current = 1
    while current <= N:
        tmp = current
        current = current + previous
        previous = tmp

    ########## here current >= A

    count = 0
    remain = N
    while remain >= previous:
        count += 1
        remain -= previous

    return count + fibsum(remain)


if __name__ == '__main__':
    assert fibsum(0) == 0
    assert fibsum(2) == 1
    assert fibsum(8) == 1
    assert fibsum(11) == 2
    assert fibsum(12) == 3
