def hello():
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")


def greet(person):
    print("Hello, " + person)


greet("Brian Ruff")


def add_nums(num1, num2):
    return num1 + num2


print(add_nums(5, 5))


def get_factors(num):
    for i in range(1, num + 1):
        if num % i == 0:
            print(str(i) + " is a factor")


get_factors(1000)