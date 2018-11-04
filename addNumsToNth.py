import math


def add_numbers_up_to(n):
    result = 0
    for i in range(0, n+1):
        result += i
    print(result)


add_numbers_up_to(10)

print(math.pi)

print(math.pow(2, 3))


def rev_str(string):
    new_str = ''
    index = len(string)
    while index > 0:
        index -= 1
        new_str += string[index]
    print(new_str)


rev_str('asdf')