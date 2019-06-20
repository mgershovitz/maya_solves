def get_padded_bin(num, padded_length):
    format_str = '0%db' % padded_length
    return format(num, format_str)


def get_all_subsets(group):
    group = list(group)
    subsets = list()
    arr_size = len(group)
    max_num = pow(2, arr_size)
    for i in range(0, max_num):
        current_subset = set()
        bin_repr = get_padded_bin(i, arr_size)
        for j in range(0, arr_size):
            if bin_repr[j] == '1':
                current_subset.add(group[j])
        subsets.append(current_subset)
    return subsets

def run_tests():
    for group in [{}, {1, 2, 3}, {"dog", "cat", "mouse", "bird"}]:
        print("all the subsets of %s are - " % group)
        print(get_all_subsets(group))


if __name__ == '__main__':
    run_tests()