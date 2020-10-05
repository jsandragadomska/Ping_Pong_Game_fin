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
paddle_a.penup()
paddle_a.goto(-350, 0)


# Paddle B
paddle_b =  turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0, 0)

# Main game loop
while True:
    window.update()