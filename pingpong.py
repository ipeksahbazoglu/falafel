#this is a ping pong game

import turtle
import os
#create a window
ipek = turtle.Screen()

#title the window and other customizations
ipek.title("Ping Pong by Ipek")
ipek.bgcolor("black")
ipek.setup(width=800, height=600)

# add a tracer, it stops the window from updating so we manually update it aka make the game run faster
ipek.tracer(0)


#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #sets the animation speed, (0) max
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #sets the animation speed, (0) max
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0) #sets the animation speed, (0) max
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
#seperate the balls movement to two parts x and y
ball.dx = 2 #moves the ball two pixel at a time
ball.dy = 2

#scores
score_a = 0
score_b= 0


#create a pen for score purposes
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,270)
pen.write("Player A: 0 Player B: 0", align="center",font=("courier", 24, "normal"))

#need a function to play the game !!!!!

#move the paddle a up
def paddle_a_up():
    y = paddle_a.ycor() #returns the y coordinate of paddle a
    y +=20 #adds 20 to the y coordinate
    paddle_a.sety(y) #sets new value to y

def paddle_a_down():
    y = paddle_a.ycor() #returns the y coordinate of paddle a
    y -=20 #adds 20 to the y coordinate
    paddle_a.sety(y) #sets new value to y

def paddle_b_up():
        y = paddle_b.ycor()  # returns the y coordinate of paddle a
        y += 20  # adds 20 to the y coordinate
        paddle_b.sety(y)  # sets new value to y

def paddle_b_down():
        y = paddle_b.ycor()  # returns the y coordinate of paddle a
        y -= 20  # adds 20 to the y coordinate
        paddle_b.sety(y)  # sets new value to y

#keyboard binding

ipek.onkeypress(paddle_a_up,"w")
ipek.onkeypress(paddle_a_down,"s")

ipek.onkeypress(paddle_b_up,"Up")
ipek.onkeypress(paddle_b_down,"Down")

ipek.listen()

#Main Game Loop
while True:
    ipek.update()

    #Ball moves as the game loops
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    #Make sure the border does not fly off the screen
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 #reverses the direction of the ball
        os.system("afplay pong.wav&")
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay pong.wav&")
    if ball.xcor() > 390:
        ball.setx(0)
        ball.sety(0) #brings ball back to the center
        ball.dx *= -1
        score_a +=1
        os.system("afplay pong.wav&")
        pen.clear()
        pen.write("Player A: {}  Player B: {} ".format(score_a,score_b), align="center", font=("courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.setx(0)
        ball.sety(0) #brings ball back to the center
        ball.dx *= -1
        score_b +=1
        pen.clear()
        os.system("afplay pong.wav&")
        pen.write("Player A: {}  Player B: {} ".format(score_a, score_b), align="center",font=("courier", 24, "normal"))

    #paddle and ball colision set up
    if (ball.xcor() > 340 and ball.xcor()< 350) and ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40:
        ball.setx(340)
        ball.dx *= -1


    if (ball.xcor() < -340 and ball.xcor()> -350) and ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40:
        ball.setx (-340)
        ball.dx *= -1






