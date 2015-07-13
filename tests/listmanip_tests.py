
import fontais


def random_list_setup(dmin, dmax, dtype, length, num_runs):
    for _ in xrange(num_runs):
        l = fontais.random_list(length, dmin=dmin, dmax=dmax, dtype=dtype)
        assert max(l) < dmax
        assert min(l) >= dmin
        assert all(map(lambda v: type(v) == dtype, l))


def random_list_positive_test():
    yield random_list_setup, 10, 100, int, 100, 10
    yield random_list_setup, 10, 100, float, 100, 10


def random_list_negative_test():
    yield random_list_setup, -10, 10, int, 100, 10
    yield random_list_setup, -10, 10, float, 100, 10
