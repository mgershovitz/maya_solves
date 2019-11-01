def print_diag(spaces, word):
    if len(word) > 0:
        print(spaces + word[0])
        print_diag(spaces + " ", word[1:])


if __name__ == '__main__':
    print_diag("", "Hello World!")
