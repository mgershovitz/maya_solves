def longest_subsequence_length(arr):
    longest_length = 0
    seq = dict()
    for n in arr:
        if n - 1 in seq:
            seq_min = seq.pop(n - 1)[0]
        else:
            seq_min = n
        if n + 1 in seq:
            seq_max = seq.pop(n + 1)[1]
        else:
            seq_max = n
        current_seq = (seq_min, seq_max)
        seq[seq_min] = seq[seq_max] = current_seq
        longest_length = max(longest_length, current_seq[1]-current_seq[0] + 1)
    return longest_length

def run_tests():
    assert longest_subsequence_length([2, 5, 3, 10, 9, 4]) == 4
    assert longest_subsequence_length([2]) == 1
    assert longest_subsequence_length([2, 4, 7, 20, 0]) == 1
    assert longest_subsequence_length([101, 2, 3, 4, 5, 6, 100, 1]) == 6
    assert longest_subsequence_length([]) == 0


if __name__ == '__main__':
    run_tests()