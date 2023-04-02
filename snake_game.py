import turtle as t
import time
import random


delay = 0.1
score = 0
highestscore = 0


# snakebodies

bodies = []

# canvas
s = t.Screen()
s.title("Snake Game")
s.bgcolor("green")
s.setup(600, 600)

# create Snake head
head = t.Turtle()
head.speed(0)
head.shape("circle")
head.color("red")
head.fillcolor("black")
head.penup()
head.goto(0, 0)
head.shapesize(1,0.90)
head.direction = "stop"

# snake food
food = t.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.fillcolor("red")
food.penup()
food.ht()
food.goto(0, 200)
food.shapesize(0.60,0.60)
food.st()

# score board
sb = t.Turtle()
sb.shape("square")
sb.fillcolor("black")
sb.penup()
sb.ht()
sb.goto(-290, 280)
sb.write("Your Score: 0     |       HighestScore: 0")

# snake controls


def moveup():
    if head.direction != "down":
        head.direction = "up"


def movedown():
    if head.direction != "up":
        head.direction = "down"


def moveright():
    if head.direction != "left":
        head.direction = "right"


def moveleft():
    if head.direction != "right":
        head.direction = "left"


def movestop():
    head.direction = "stop"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)


# key mapping
s.listen()
s.onkey(moveup, "Up")
s.onkey(movedown, "Down")
s.onkey(moveleft, "Left")
s.onkey(moveright, "Right")
s.onkey(movestop, "space")

# driver code

while True:
    s.update()
    if head.xcor() > 290:
        head.setx(-290)
    if head.xcor() < -290:
        head.setx(290)
    if head.ycor() > 290:
        head.sety(-290)
    if head.ycor() < -290:
        head.sety(290)

    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        body = t.Turtle()
        body.speed(0)
        body.penup()
        body.shape("circle")
        body.color("blue")
        body.fillcolor("yellow")
        bodies.append(body)

        score += 10

        delay -= 0.001

        if score > highestscore:
            highestscore = score

        sb.clear()
        sb.write("Your Score: {}        |       HighestScore: {}".format(score, highestscore))

    for index in range(len(bodies)-1, 0, -1):
        x = bodies[index-1].xcor()
        y = bodies[index-1].ycor()
        bodies[index].goto(x, y)

    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)
    move()

    for body in bodies:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # hide bodies
            for body in bodies:
                body.ht()
            bodies.clear()

            score = 0
            delay = 0.1

            # update Score board
            sb.clear()
            sb.write("Your Score: {}        |       HighestScore: {}".format(score, highestscore))
    time.sleep(delay)
# s.mainloop()
