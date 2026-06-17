import turtle
import random

turtle.setup(500, 500)
w = turtle.Screen()
t = turtle.Turtle()

colors = ["red", "blue", "green", "orange", "purple", "black"]


def move_up():
    # TODO: move forward 20
    t.forward(20)


def turn_left():
    # TODO
    t.left(90)


def turn_right():
    # TODO
    t.right(90)


def toggle_pen():
    # TODO: toggle up/down based on current pen state (hint: isdown())
    if t.isdown():
        t.penup()
    else:
        t.pendown()


def clear_screen():
    # TODO
    t.clear()


def quit_program():
    # TODO: close the window
    w.bye()


def auto_color():
    # TODO: change to a random color
    # TODO: schedule this same function to run again in 0.5s (periodic!)
    t.color(random.choice(colors))
    w.ontimer(auto_color, 1)


# --- wiring ---
# TODO: bind the handlers above to keys (Up, Left, Right, space, c, q)


# TODO: start the automatic color change (call it once)
# TODO: start listening for events
# TODO: enter the event loop
w.setup(700, 700)


w.onkey(move_up, 'Up')
w.onkey(turn_left, 'Left')
w.onkey(turn_right, 'Right')
w.onkey(toggle_pen, 'space')
w.onkey(clear_screen, 'c')
w.onkey(quit_program, 'q')

auto_color()

w.listen()
w.mainloop()