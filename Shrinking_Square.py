import turtle

turtle_screen = turtle.Screen()

turtle_screen.bgcolor("light green")
turtle.title("Turtle Python")

turtle_instance = turtle.Turtle()
turtle_instance.color("blue")

def ShrinkingSquare(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size = size - 5

ShrinkingSquare(150)
ShrinkingSquare(130)
ShrinkingSquare(110)
ShrinkingSquare(90)
ShrinkingSquare(70)
ShrinkingSquare(50)
ShrinkingSquare(40)
ShrinkingSquare(20)
ShrinkingSquare(10)

turtle.done()

