def find_last_word(s):
    if len(s) == 0:
        return ""
    last_word = ""
    i = len(s) - 1
    while s[i] == " " and i >= 0:
        i -= 1
    while s[i] != " " and i >= 0:
        last_word = s[i] + last_word
        i -= 1
    return last_word

def run_tests():
    assert find_last_word("") == ""
    assert find_last_word(" ") == ""
    assert find_last_word("a") == "a"
    assert find_last_word("dog ") == "dog"
    assert find_last_word("hello world") == "world"


if __name__ == '__main__':
    run_tests()