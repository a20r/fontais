

class memoize(object):

    args = dict()

    def __call__(self, f):
        def __inner(*args, **kwargs):
            if not (args, kwargs) in memoize.args:
                ret_val = f(*args, **kwargs)
                memoize.args[args, kwargs] = ret_val
            return memoize.args[args, kwargs]
        return __inner


class curry(object):

    def __call__(self, f):
        def __inner(*args, **kwargs):
            def __super_inner(*other_args, **other_kwargs):
                for k in kwargs:
                    other_kwargs[k] = kwargs[k]
                super_args = args + other_args
                return f(*super_args, **other_kwargs)
            return __super_inner
        return __inner
