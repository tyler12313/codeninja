import turtle

class ball(turtle.Turtle):
    def __init__(self):
        super().__init__()

gravity = -0.5
y_velocity = 1
x_velocity = 1
energyloss = 0.95

width = 600
height = 800
window = turtle.Screen()
window.setup(width, height)
window.tracer(0)
window = turtle.Screen()
window.tracer(0)

ball = turtle.Turtle()
ball.penup()
ball.color("green")
ball.shape("circle")
while True:
    ball.sety(ball.ycor() + y_velocity)
    ball.setx(ball.xcor() + x_velocity)
    y_velocity += gravity
    if ball.ycor() < -height / 2:
        y_velocity = -y_velocity * energyloss
    if ball.xcor() > width / 2 or ball.xcor() < -width / 2:
        x_velocity = -x_velocity
    window.update()
