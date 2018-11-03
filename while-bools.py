import turtle

print("S or T")
polygon = input()

print("How many?")
count = input()
count = int(count)
if not count:
    count = 1

running = True

while running:
    if polygon == "T":
        for i in range(0, 3):
            turtle.forward(100)
            turtle.left(120)
    elif polygon == "S":
        for i in range(0, 4):
            turtle.forward(100)
            turtle.right(90)
    else:
        print("Invalid Choice")
    count -= 1
    if count == 0:
        running = False
    turtle.forward(10)