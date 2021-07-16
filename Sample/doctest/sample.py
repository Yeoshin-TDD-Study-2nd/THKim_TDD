import doctest

def square(x):
    """Return the square of x.

    >>> square(2)
    4

    >>> square(-2)
    4
    """
    return x**2


if __name__ == '__main__':
    doctest.testmod()