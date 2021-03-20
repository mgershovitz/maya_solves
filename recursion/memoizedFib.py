from datetime import datetime


def memoized_fib(n):
    results_cache = {}

    def fib(num):
        if num in results_cache:
            return results_cache[num]
        else:
            if num <= 2:
                res = 1
            else:
                res = fib(num - 1) + fib(num - 2)

            results_cache[num] = res
            return res

    return fib(n)


def run(n):
    start_time = datetime.now()
    res = memoized_fib(n)
    print("Calculating fib(%d) = %d took %s seconds" % (n, res, datetime.now() - start_time))


if __name__ == '__main__':
    run(2)
    run(5)
    run(10)
    run(50)
    run(100)
    run(500)
    run(1000)
