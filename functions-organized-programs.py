def main():
    print("Make a selection by entering a number: ")
    print("[1] Computer Greeting, [2] factorization, 3[factorize_table")
    choice = input("Your selection: ")
    if choice == "1":
        computer_greeting()
    elif choice == "2":
        factorization()
    elif choice == "3":
        factorize_table()
    else:
        print("Invalid option")


def factorization():
    num = input("enter your num here")
    num = int(num)
    counter = 0
    for i in range(1, num + 1):
        if num % i == 0:
            print(str(i) + " is a factor")
            counter += 1
    if counter == 2:
        print(str(num) + " is a prime number")


def computer_greeting():
    print("Hello human what is your name?")
    name = input()
    if name == "Brian":
        print("Ahh, it's your again, Brian")
    elif name == "Bob":
        print("Hello Bob!")
    else:
        print("Nice to meet you " + name)


def factorize_table():
    num = input("Enter a number: ")
    num = int(num)
    print("here is your times table")
    for i in range(1, 101):
        print(num * i)


main()