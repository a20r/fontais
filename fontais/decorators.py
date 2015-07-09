
import threading


def run_thread(func):
    """
    If you put this decorator on a function, once the function is imported,
    it will run as a thread automatically.
    """

    thread = threading.Thread(target=func)
    thread.setDaemon(True)
    thread.start()


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
