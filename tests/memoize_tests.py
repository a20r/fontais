
import fontais
import time


@fontais.memoize()
def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def fib_test():
    start = time.time()
    v = fib(200)
    end = time.time()
    print end - start

    start = time.time()
    v = fib(200)
    end = time.time()
    print end - start
