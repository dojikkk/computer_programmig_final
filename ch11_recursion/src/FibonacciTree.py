"""
Fibonacci tree visualization.
"""

import turtle


def drawFibTree(n, length, angle):
    turtle.forward(2 * length)
    drawLabel(n)
    if n == 0:
        pass  # do nothing
    elif n == 1:
        pass  # do nothing
    else:
        turtle.left(angle)
        drawFibTree(n - 1, length, angle)
        turtle.right(2 * angle)
        drawFibTree(n - 2, length, angle)
        turtle.left(angle)
    turtle.backward(2 * length)


def drawLabel(txt):
    x, y = turtle.position()
    turtle.penup()
    turtle.left(90)
    turtle.forward(5)
    turtle.write(txt, font=('Times New Roman', 15, 'bold'))
    turtle.setposition(x, y)
    turtle.right(90)
    turtle.pendown()


#
# Main program:
#
turtle.setup(800, 700)

n = 5
x, y = (-350, 0)
turtle.penup()
turtle.setposition(x, y)
turtle.pendown()
drawFibTree(n, 40, 25)
# turtle.tracer(0,0) # Switch off intermediate updates
# drawFibTree(15, 10, 10)
# turtle.update() # Ask for manual screen update (otherwise no output shown!)
# turtle.tracer(1, 20) # Restore default values

window = turtle.Screen()
window.exitonclick()
