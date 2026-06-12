import turtle


def drawFibTree(n, LenAngle):
    turtle.forward(2 * LenAngle)
    drawLabel(n)
    if n == 0:
        pass  # do nothing
    elif n == 1:
        pass  # do nothing
    else:
        turtle.left(LenAngle)
        drawFibTree(n - 1, LenAngle)
        turtle.right(2 * LenAngle)
        drawFibTree(n - 2, LenAngle)
        turtle.left(LenAngle)
    turtle.backward(2 * LenAngle)


def drawLabel(txt):
    x, y = turtle.position()
    turtle.penup()
    turtle.left(90)
    turtle.forward(5)
    turtle.write(txt, font=('Times New Roman', 7, 'bold'))
    turtle.setposition(x, y)
    turtle.right(90)
    turtle.pendown()


#
# Main program:
#
turtle.setup(800, 700)

StartPositions = [[-300, 250], [-150, 250], [-300, 110], [-80, 110],
                  [-300, -150], [50, -150]]


# For each start position, draw a tree, with n varying between 1 and 6:
n = 0
for pos in StartPositions:
    x, y = pos
    n = n + 1
    turtle.penup()
    turtle.setposition(x, y)
    turtle.pendown()
    drawFibTree(n, 20)


window = turtle.Screen()
window.exitonclick()
