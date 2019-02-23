from math import factorial
from check import error


def result_full(first: int, sec: int) -> float:
    """Get the full result in float."""
    pair = float(factorial(5 - first - sec) /
                 (factorial(3 - sec) * factorial((5 - (first + sec)) - (3 - first))))
    three = float(factorial(2 - sec) / (factorial(2 - sec) * factorial(0)))
    return ((pair * three) / pow(6, 5 - first - sec)) * 100


def full(value, list: [int]):
    """Full function."""
    if len(value) < 3:
        error()
    first_occur = list.count(int(value[1]))
    sec_occur = list.count(int(value[2]))

    if first_occur == 3 and sec_occur == 2:
        print('chances to get a ' + value[1] + ' full of ' +
              value[2] + ': 100.00%')
    else:
        3 if first_occur > 3 else first_occur
        2 if sec_occur > 2 else sec_occur
        print('chances to get a ' + value[1] + ' full of ' +
              value[2] + ':  ' + '%0.2f' % result_full(first_occur, sec_occur) + '%')


def get_digit(nb: int, list: [int]) -> int:
    """Return 1 if nb is in list, else 0"""
    for i in range(0, 5):
        if list[i] == nb:
            return 1
    return 0


def straight(value, list: [int]):
    """Straight function."""
    occur = 0
    if int(value[1]) != 5 and int(value[1]) != 6:
        error()
    elif int(value[1]) == 5:
        occur = get_digit(1, list) + get_digit(2, list) + get_digit(3, list)\
            + get_digit(4, list) + get_digit(5, list)
    elif int(value[1]) == 6:
        occur = get_digit(6, list) + get_digit(2, list) + get_digit(3, list)\
            + get_digit(4, list) + get_digit(5, list)
    print('chances to get a ' + value[1] + ' ' + value[0] + ':  ' +
          '%0.2f' % (factorial(5 - occur) / pow(6, 5 - occur) * 100) + '%')
