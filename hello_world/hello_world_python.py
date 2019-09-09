def hello_world():
    space_counter = 0
    s = "Hello World"
    for c in s:
        print(" " * space_counter + c)
        space_counter += 1


if __name__ == '__main__':
    hello_world()