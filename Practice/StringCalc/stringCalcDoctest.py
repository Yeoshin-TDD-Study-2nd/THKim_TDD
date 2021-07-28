import doctest

def string_add(string_value):
    """Return the string add
    >>> string_add('10+20')
    30

    >>> string_add('1+1')
    2
    """
    num_lst = string_value.split('+')
    return int(num_lst[0]) + int(num_lst[1])

def string_substract(string_value):
    num_lst = string_value.split('-')
    return int(num_lst[0]) - int(num_lst[1])

def string_multiply(string_value):
    num_lst = string_value.split('*')
    return int(num_lst[0]) * int(num_lst[1])

def string_division(string_value):
    num_lst = string_value.split('/')
    return int(num_lst[0]) / int(num_lst[1])


if __name__ == '__main__':
    doctest.testmod()