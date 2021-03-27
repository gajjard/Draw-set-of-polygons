# import turtle module
import turtle as t

tu = t.Turtle()

# set starting coordinates.
tu.penup()
tu.goto(-50, 100)
tu.pendown()

# loop for drawing polygons
num_sides = 3

while num_sides != 11:
    for _ in range(num_sides):
        angle = 360 / num_sides
        tu.forward(100)
        tu.right(angle)
    num_sides += 1

# Screen() method in the turtle module is used to get the screen open.
screen = t.Screen()

# exit the screen after a single left click.
screen.exitonclick()

