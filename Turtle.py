import turtle
s=turtle.Screen()
t=turtle.Turtle()

t.speed(1000)

def square():
    for i in range(3):
        t.forward(120)
        t.right(236)

square()

for i in range(360):
    square()
    t.left(7)
