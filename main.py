from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from border import Points
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Ping Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

l_point = Points((100, 250))
r_point = Points((-100, 250))

defalut_sleep = 0.1
fix_number = True
game_on = True
while game_on:
    screen.update()
    time.sleep(defalut_sleep)
    ball.goto(ball.xcor() + ball.x_move, ball.ycor() + ball.y_move)

    if ball.xcor() > 400:
        ball.goto(0 ,0)
        ball.x_move *= -1
        defalut_sleep = 0.1
        r_point.update()
        fix_number = not fix_number

    if ball.xcor() < -400:
        ball.goto(0 ,0)
        ball.x_move *= -1
        defalut_sleep = 0.1
        l_point.update()
        fix_number = not fix_number

    if ball.ycor() >= 280 or ball.ycor() <= -280:
            ball.y_move *= -1

#     if (ball.xcor() >= 330 and ball.distance(r_paddle) <= 50) or (ball.xcor() <= -330 and ball.distance(l_paddle) <= 50):
#             ball.x_move *= -1
#             defalut_sleep *= 0.9

    if (ball.xcor() >= 330 and ball.distance(r_paddle) <= 50 and fix_number and ball.xcor() <= 350):
            ball.x_move *= -1
            defalut_sleep *= 0.9
            fix_number = False
    if  (ball.xcor() <= -330 and ball.distance(l_paddle) <= 50 and not fix_number and ball.xcor() >= -350):
            ball.x_move *= -1
            defalut_sleep *= 0.9
            fix_number = True

    screen.onkey(screen.exitonclick, "o")



screen.exitonclick()
