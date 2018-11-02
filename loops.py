# loop with step-by-2

# for i in range(0, 11, 2):
#     print(i)

# loop through string

string = "hello"

# for i in range(0, len(string)):
#     if(string[i] == "h"):
#         print("Found an H")
#         print("at " + str(i))

# for i in string:
#     if i == "h":
#         print("Found H")
#         print(i)


# sentence = "This is a multi-word string"
#
# for letter in sentence:
#     print(letter)

# arr = [1, 2, 3]
#
# for num in arr:
#     print(num)

person = {
    "name": "Brian",
    "age": 29,
    "height": 75,
    "eye color": "green"
}

for attr in person:
    print(str(attr) + ": " + str(person[attr]))
