def string_add(string_value):
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
    try:
        return int(num_lst[0]) / int(num_lst[1])
    except ZeroDivisionError as z:
        print("Error:",z)


if __name__ == '__main__':
    print(string_add('10 + 30'))
    print(string_substract('10- 30'))
    print(string_division('30/0'))