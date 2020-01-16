# Related blog post - https://algoritmim.co.il/2019/07/17/anagrams/

import string
from collections import defaultdict


def get_word_key(word):
    hist = defaultdict(int)
    for c in word:
        hist[c] += 1
    str_hist = ""
    for c in string.ascii_letters:
        str_hist += "%s%d" % (c, hist[c])

    return ''.join(str_hist)


def find_anagrams(arr):
    results = defaultdict(list)
    for i in range(0, len(arr)):
        word = arr[i]
        word_key = get_word_key(word)
        results[word_key].append(i + 1)
    return list(results.values())

def run_tests():
    assert find_anagrams(["dog", "god", "odg"]) == [[1,2,3]]
    assert find_anagrams(["dog", "cat", "god", "odg"]) == [[1,3,4], [2]]
    assert find_anagrams(["dog"]) == [[1]]
    assert find_anagrams(["dog", "dog"]) == [[1, 2]]
    assert find_anagrams(["dog", "Dog"]) == [[1], [2]]
    assert find_anagrams(["dog", "cat", "toy", "boy"]) == [[1], [2], [3], [4]]


if __name__ == '__main__':
    run_tests()