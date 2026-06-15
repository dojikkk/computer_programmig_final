import turtle

turtle.setup(300, 200)


def printXY(x, y):
    print(x, y)


# Register callback for mouse on-click events:
turtle.onscreenclick(printXY)

# Switch to the event processing loop of Python:
turtle.mainloop()