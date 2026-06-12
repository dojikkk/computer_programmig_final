import turtle
#
# dir(turtle) to show all commands provided by the turtle module.
# dir(turtle.circle) to get help on the circle function of the turtle module.

#
# Square, absolute positioning:
#

# Set window title:
# window = turtle.Screen()
# window.title('Absolute Positioning')
#
# # Get default turtle and hide:
# the_turtle = turtle.getturtle()
# the_turtle.hideturtle()
#
# # Draw square using absolute positioning:
# the_turtle.setposition(100, 0)
# the_turtle.setposition(100, 100)
# the_turtle.setposition(0, 100)
# the_turtle.setposition(0, 0)


#
# Square, relative positioning:
#

# # Set window title:
# window = turtle.Screen()
# window.title('Relative Positioning')
#
# # Get default title and hide:
# the_turtle = turtle.getturtle()
# the_turtle.hideturtle()
#
# # Draw square using relative positioning:
# for move in range(0, 4):
#     the_turtle.forward(100)
#     the_turtle.left(90)


#
# Drawing disconnected lines:
#

# turtle.setup(800, 600)
# window = turtle.Screen()
# window.title('Drawing an A')
#
# the_turtle = turtle.getturtle()
# the_turtle.hideturtle()
# the_turtle.penup()
# the_turtle.setposition(-100, 0)
# the_turtle.pendown()
# the_turtle.setposition(0, 250)
# the_turtle.setposition(100, 0)
# the_turtle.penup()
# the_turtle.setposition(-64, 90)
# the_turtle.pendown()
# the_turtle.setposition(64, 90)


#
# Erase a turtle's drawing:
#

# turtle.setup(400, 400)
# window = turtle.Screen()
# window.title('Drawing an A')
#
# the_turtle = turtle.getturtle()
# the_turtle.setposition(100, 0)
# input('Press enter to continue')
# the_turtle.clear()
# input('Press enter to continue')


#
# Modifying the turtle's appearance:
#

# turtle.setup(800, 600)
# window = turtle.Screen()
# the_turtle = turtle.getturtle()
#
# # Enable programmer-supplied change of turtle size:
# the_turtle.resizemode('user')
#
# # Set a new turtle size:
# the_turtle.turtlesize(8, 8)
#
# the_turtle.shape('circle')
# the_turtle.fillcolor('green')


#
# Setting turtle to polygon shape:
#

# turtle.setup(430,430)
# window = turtle.Screen()
# window.title('My Polygon')
# the_turtle = turtle.getturtle()
#
# turtle.register_shape('mypolygon',
#     ((0,0), (100,0), (140, 40)) )
#
# the_turtle.shape('mypolygon')
# the_turtle.fillcolor('blue')


#
# Stamping turtle on screen:
#

# turtle.setup(430, 430)
# window = turtle.Screen()
# window.title('My stamps')
# the_turtle = turtle.getturtle()
#
# turtle.register_shape('mypolygon',
#  ((0,0), (100,0), (140, 40)))
#
# the_turtle.shape('mypolygon')
# the_turtle.fillcolor('white')
#
# for angle in range(0, 360, 10):
#     the_turtle.setheading(angle)
#     the_turtle.stamp()
#
# turtle.register_shape('flower.gif')
# the_turtle.shape('flower.gif')


#
# Creating multiple turtle objects:
#

# turtle.setup(430,430)
# window = turtle.Screen()
# window.title('Turtles everywhere...')
#
# t1 = turtle.Turtle()
# t2 = turtle.Turtle()
# t3 = turtle.Turtle()
#
# t1.fillcolor('red')
# t1.resizemode('user')
# t1.turtlesize(3, 3)
# t2.fillcolor('blue')
# t2.resizemode('user')
# t2.turtlesize(2, 2)
# t3.fillcolor('orange')
# t3.resizemode('user')
# t3.turtlesize(3, 3)
#
# t1.forward(100)
# t2.setheading(45)
# t2.forward(100)
# t3.setheading(70)
# t3.forward(100)


#
# Fun with functions:
#

# def square(t, length):
#     for s in range(4):
#         t.forward(length)
#         t.left(90)
#
#
# turtle.setup(650, 620)
#
# t = turtle.getturtle()
# t.resizemode('user')
# t.turtlesize(4, 4)
#
# t.speed(0) # set fastest turtle speed
# square(t, 50)
# square(t, 100)
# square(t, 150)
#
# #turtle.tracer(0, 0) # disable screen updates
#
# for l in range(50, 301, 50):
#     square(t, l)
#     turtle.update() # force screen update
#
# turtle.reset()
# t.speed(0)    # 0: fastest, 1-10 slower to faster
# t.circle(100) # counter-clockwise
# t.circle(-50, steps=620) # clock-wise
# t.setposition(-100, -100)
# t.left(90)
# t.circle(-50)


#
# Filled shapes:
#
# t.color("blue")
# t.begin_fill()
# square(t, 200)
# t.end_fill()

#
# Open filled shapes:
#

# turtle.reset()
# t.color("black")
# t.width(10)
# t.begin_fill()
# t.forward(45)
# t.setheading(45)
# t.forward(45)
# t.setheading(90)
# t.forward(45)
# t.color("blue")
# input("Press enter to continue: ")
# t.end_fill()


#
# Recap: higher-order functions
#

# import math

# def cco1100(f, x):
#     '''Higher-order function that applies f to x and returns the result. '''
#     return f(x)

# m = cco1100(abs, -2)
# n = cco1100(math.factorial, 3)
# o = cco1100(print, -2)
# p = cco1100(input, 'Enter a number: ')
# print(m, n, o, p)


window = turtle.Screen()
window.exitonclick()
