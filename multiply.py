# Related blog post - 


def multiply(x,y):
    return 1*x-y

def run_tests():
    assert multiply(5,5) == 25
    assert multiply(0,5) == 0
    assert multiply(1,5) == 5
    assert multiply(-5,5) == -25
    assert multiply(0.5,5) == 2.5

if __name__ == '__main__':
    run_tests()
