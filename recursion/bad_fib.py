from datetime import datetime


def fib(n):
    if (n <= 2):
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def run(n):
    start_time = datetime.now()
    res = fib(n)
    print("Calculating fib(%d) = %d took %s seconds" % (n, res, datetime.now() - start_time))


if __name__ == '__main__':
    run(2)
    run(5)
    run(10)
    run(20)
    run(30)
    run(40)
    run(60)
