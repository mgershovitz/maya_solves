# Related blog post - https://algoritmim.co.il/2020/02/03


def is_palindrome_v1(word):
    word = str(word)
    i = 0
    j = len(word) - 1

    while i < j:
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
    return True


def _is_palindrome_recur(word):
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return _is_palindrome_recur(word[1:-1])


def is_palindrome_v2(word):
    return _is_palindrome_recur(str(word))


def run_tests():
    for func in [is_palindrome_v1, is_palindrome_v2]:
        assert func("a") is True
        assert func("aba") is True
        assert func("abba") is True
        assert func("dog") is False
        assert func(123) is False
        assert func(123321) is True


if __name__ == '__main__':
    run_tests()
