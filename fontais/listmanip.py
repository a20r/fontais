
"""
A collection of list manipulation functions that I commonly use
"""


def k_max(l, k):
    """
    Gets the k largest elements in a list and their indices
    """
    enum_l = list(enumerate(l))
    l_s = sorted(enum_l, key=lambda v: v[1])
    k_maxes = l_s[(len(l) - k):]
    return tuple(zip(*k_maxes))
