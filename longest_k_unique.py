# Related blog post - https://mayareads.blog/2019/07/04/k-unique-sequence/

import copy
from collections import defaultdict

def find_longest_k_unique(arr, k):
    longest_k_uniuqe = []
    if len(arr) == 1:
        return arr
    else:
        i = j = 0
        current_k_unique = [arr[i]]
        current_range = defaultdict(int)
        current_range[arr[i]] += 1
        unique_count = len(current_range.keys())

        while j < len(arr)-1:
            if unique_count <= k:
                j += 1
                current_k_unique.append(arr[j])
                current_range[arr[j]] += 1
            else:
                del current_k_unique[0]

                current_range[arr[i]] -= 1
                if current_range[arr[i]] == 0:
                    current_range.pop(arr[i])
                i += 1
            unique_count = len(current_range.keys())
            if unique_count == k:
                if len(current_k_unique) > len(longest_k_uniuqe):
                    longest_k_uniuqe = copy.deepcopy(current_k_unique)

        return longest_k_uniuqe

def run_tests():
    arr = [1, 5, 3, 100, 3, 2, 2]
    k=1
    assert find_longest_k_unique(arr, k) == [2,2]

    k=2
    assert find_longest_k_unique(arr, k) == [3,100,3]

    k = 3
    assert find_longest_k_unique(arr, k) == [3,100,3,2,2]

    arr = [1, 2, 3, 4]
    k=1
    assert find_longest_k_unique(arr,k) == [2]

    k=2
    assert find_longest_k_unique(arr,k) == [1,2]


if __name__ == '__main__':
    run_tests()