import turtle

# Background setup
window = turtle.Screen()
window.title("Pong by jsandragadomska")
window.bgcolor("pink")
window.setup(width=800, height=600)
window.tracer(0)

# Paddle A
paddle_a =  turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.shapesize(stretch_wid = 5, stretch_len= 1)
paddle_a.penup()
paddle_a.goto(-350, 0)


# Paddle B
paddle_b =  turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.shapesize(stretch_wid = 5, stretch_len= 1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0, 0)
# every time while ball moves it moves by 2 pixels
ball.dx = 2
ball.dy = 2

# Move paddles function
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 240:
        y += 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 240:
        y += 20
    paddle_b.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -230:
        y -= 20
    paddle_a.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -230:
        y -= 20
    paddle_b.sety(y)

# Keybord binding
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_b_up, "o")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_down, "l")

# Main game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    # top
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    # bottom
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # right
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    # left
    if ball.xcor() <  -390:
        ball.goto(0, 0)
        ball.dx *= -1