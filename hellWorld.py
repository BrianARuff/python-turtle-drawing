import turtle

for i in range(0, 1000):
   turtle.forward(i)
   turtle.right(90)
   if(i % 4 == 0):
      turtle.forward(i)
      turtle.right(90)

