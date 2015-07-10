
import threading


def run_thread_dep(func):
    """
    If you put this decorator on a function, once the function is imported,
    it will run as a thread automatically.
    """

    thread = threading.Thread(target=func)
    thread.setDaemon(True)
    thread.start()

    def __inner():
        return thread

    return __inner


class run_thread(object):
    """
    A decorator to run a thread and allows arguments
    """

    def __init__(self, *args, **kwargs):
        self.thread = threading.Thread(
            target=args[0], args=tuple(args[1:]), kwargs=kwargs)
        self.thread.setDaemon(True)
        self.thread.start()

    def __call__(self):
        def __inner():
            return self.thread
        return __inner


class on_import(object):
    """
    If you put this decorator on a function, it will automatically be called
    once the module containing the function is imported
    """

    def __init__(self):
        self.already_imported = list()

    def __call__(self, func):
        global already_imported
        name = func.__name__ + " " + func.__module__
        if not name in self.already_imported:
            self.already_imported.append(name)
            func()


class check_attrs(object):
    """
    A decorator that checks that an input to a function contains
    certain attributes.

    Example:
        @check_attrs("x", "y", "z")
        def vec_sub(self, op):
            return Point(self.x - op.x, self.y - op.y, self.z - op.z)

    This means that you no longer need to check if the arguments contain
    those attributes.
    """

    def __init__(self, attrs):
        self.attrs = attrs

    def __call__(self, f):
        def __inner(*inputs):
            for ins in inputs:
                for attr in self.attrs:
                    if not hasattr(ins, attr):
                        raise AttributeError(
                            "{} does not have {}".format(repr(ins), attr))
            return f(*inputs)

        return __inner
