import turtle

turtle.setup(400, 500) 
w = turtle.Screen()
t = turtle.Turtle()
t.resizemode('user')
t.turtlesize(4, 4)
t.pensize(5)


# The next four functions are our "event handlers".
def handler_1():
    t.forward(30)


def handler_2():
    t.left(45)


def handler_3():
    t.right(45)


def handler_4():
    w.bye()  # Close down the turtle window


# These lines "wire up" keypresses to the handlers we've defined.
w.onkey(handler_1, "Up")
w.onkey(handler_2, "Left")
w.onkey(handler_3, "Right")
w.onkey(handler_4, "q")

# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its
# handler will be called.
w.listen()
w.mainloop()