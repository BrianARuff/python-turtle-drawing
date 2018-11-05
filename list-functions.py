numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

letters = ['a', 'b', 'c', 'd', 'e']

# .append
numbers.append(500)
print(numbers)

numbers.extend(letters)

print(numbers)

numbers.pop()

print(numbers)

numbers.insert(0, 'e')

print(numbers)

limit = input("Upper Limit ")
limit = int(limit)

primes = []

for num in range(2, limit + 1):

    count = 0

    for i in range(1, num + 1, 2):
        if num % i == 0:
            count += 1

    if count == 2:
        primes.append(num)


print(primes)