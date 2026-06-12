import turtle

width = 700
height = 700

w = turtle.Screen()
w.setup(width, height)
w.title("Turtle exercise")
w.bgcolor("black")
w.tracer(0)

# Turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("cyan")
t.penup()
t.goto(-250, 0)
t.setheading(0)

# Enemies
enemy_start_positions = [
    (250, 0),
    (250, 150),
    (250, -150),
    (150, 0),
    (150, 150),
    (150, -150),
    (0, 0),
    (-50, 150),
    (-150, -150),
]

enemies = []

for x, y in enemy_start_positions:
    enemy = turtle.Turtle()
    enemy.shape("turtle")
    enemy.color("orange")
    enemy.penup()
    enemy.goto(x, y)
    enemy.setheading(180)
    enemies.append(enemy)

# Bullet
b = turtle.Turtle()
b.shape("circle")
b.color("red")
b.penup()
b.hideturtle()

player_score = 0
enemy_score = 0

# Scoreboard
score_writer = turtle.Turtle()
score_writer.color("white")
score_writer.penup()
score_writer.hideturtle()
score_writer.goto(0, height / 2 - 40)

def update_score():
    score_writer.clear()
    score_writer.write(
        "Player: " + str(player_score) + "     Enemy: " + str(enemy_score),
        align="center",
        font=("Arial", 18, "bold")
    )

def handler_1():
    t.forward(15)
    w.update()

def handler_2():
    t.left(15)
    w.update()

def handler_3():
    t.right(15)
    w.update()

def handler_4():
    t.backward(15)
    w.update()

def handler_5():
    w.bye()  # Close down the turtle window

def reset_player():
    t.goto(-250, 0)
    t.setheading(0)

def reset_enemy(enemy, start_position):
    enemy.goto(start_position)
    enemy.setheading(enemy.towards(t))

def reset_all_enemies():
    for i in range(len(enemies)):
        reset_enemy(enemies[i], enemy_start_positions[i])

def move_enemy():
    global enemy_score

    for enemy in enemies:
        enemy.setheading(enemy.towards(t))
        enemy.forward(5)

        if enemy.distance(t) < 25:
            print("Enemy caught the player!")
            enemy_score += 1
            update_score()
            reset_player()
            break

    w.update()
    w.ontimer(move_enemy, 100)

def fire():
    if not b.isvisible():
        b.goto(t.position())
        b.setheading(t.heading())
        b.showturtle()

def move_bullet():
    global player_score

    if b.isvisible():
        b.forward(20)
        w.update()

        for i in range(len(enemies)):
            enemy = enemies[i]

            if b.distance(enemy) < 25:
                print("Enemy hit!")
                player_score += 1
                update_score()
                b.hideturtle()
                reset_enemy(enemy, enemy_start_positions[i])
                break

        if abs(b.xcor()) > width/2 or abs(b.ycor()) > height/2:
            b.hideturtle()
    w.ontimer(move_bullet, 50)

w.onkey(handler_1, "Up")
w.onkey(handler_2, "Left")
w.onkey(handler_3, "Right")
w.onkey(handler_4, "Down")
w.onkey(handler_5, "q")
w.onkey(fire, "space")

update_score()
move_enemy()
move_bullet()

w.update()
w.listen()
w.mainloop()
