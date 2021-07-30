import re

def str_calc(str_val: str) -> float: 
    p = re.compile('[\*,\+,\-,\/]')
    notation = p.search(str_val).group()
    num_lst = [float(i) for i in str_val.split(notation)]
    
    if notation == '+':
        return num_lst[0] + num_lst[1]
    elif notation == '-':
        return num_lst[0] - num_lst[1]
    elif notation == '*':
        return num_lst[0] * num_lst[1]
    elif notation == '/':
        try:
            return num_lst[0] / num_lst[1]
        except ZeroDivisionError as z:
            return z


if __name__ == '__main__':
    print(str_calc('1/5'))