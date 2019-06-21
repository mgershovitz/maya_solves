def find_last_word(s):
    last_word = ""
    i = len(s) - 1
    while i >= 0 and s[i] == " ":
        i -= 1
    while i >= 0 and s[i] != " ":
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