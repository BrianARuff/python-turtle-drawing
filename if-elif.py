import turtle

# Demonstrate if-elif-else with Turtle drawing Library

print("Draw Sqaure or Triangle?")

polygon = input().lower().capitalize()

if polygon == "Triangle":
    for i in range(0, 3):
        turtle.forward(100)
        turtle.left(120)
elif polygon == "Square":
    for i in range(0, 4):
        turtle.forward(100)
        turtle.right(90)
else:
    print("Invalid option")
