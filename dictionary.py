# Dictionary - Unique keys with values in the form of pairs.

d = {}

print(d)

print(type(d))

d['banana'] = 'taste the fruit'

print(d)

d[4] = 'four'

print(d)

jane = {
    'name': 'Jane',
    'age': 29,
    'residence': 'Charlotte, NC, USA'
}

print(jane)


def checkPrime(n):
    is_prime = False
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        is_prime = True
    print(is_prime)

checkPrime(13)