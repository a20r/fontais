
"""
A collection of list manipulation functions that I commonly use
"""


def k_max(l, k):
    """
    Gets the k largest elements in a list and their indices.
    """
    enum_l = list(enumerate(l))
    l_s = sorted(enum_l, key=lambda v: v[1])
    k_maxes = l_s[(len(l) - k):]
    return tuple(map(list, zip(*k_maxes)))


def k_argmax(l, k, func):
    """
    Gets the indices and values of the k-largest function results
    from func.
    """
    l_map = map(func, l)
    return k_max(l_map, k)


def k_min(l, k):
    """
    Gets the k smallest elements in a list and their indices.
    """
    enum_l = list(enumerate(l))
    l_s = sorted(enum_l, key=lambda v: v[1])
    k_mins = l_s[:k]
    return tuple(map(list, zip(*k_mins)))


def k_argmin(l, k, func):
    """
    Gets the indices and values of the k-smallest function results
    from func.
    """
    l_map = map(func, l)
    return k_min(l_map, k)
