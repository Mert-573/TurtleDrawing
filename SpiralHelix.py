import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("black")
turtle.title("Turtle Python")
turtle.speed(0)

turtle_instance = turtle.Turtle()
turtle_instance.color("red")

turtle_colors = ["purple","red","pink","blue","orange"]

for i in range(15):
    turtle_instance.color(turtle_colors[i % 5])
    turtle_instance.circle(10*i)
    turtle_instance.circle(-10*i)
    turtle_instance.left(i)

turtle.done()