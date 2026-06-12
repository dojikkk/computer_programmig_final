import turtle

turtle.setup(400, 500) 
w = turtle.Screen()
t = turtle.Turtle()
t.resizemode('user')
t.turtlesize(4, 4)


def TurtleHandler():
    t.left(45)
    t.forward(55)
    # Timers are one-shot. To have periodic events, we need to set up the
    # next event inside the timer handler function:
    print('Before ontimer() setup')
    w.ontimer(TurtleHandler, 1500)  # ontimer returns immediately!
    print('After ontimer() setup')
    # w.ontimer(print, 250)  # Will go off after 250ms.


TurtleHandler()
w.mainloop()
