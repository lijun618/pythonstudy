import turtle
import random
turtle.colormode(255)
turtle.setup(600, 600, 0, 60)

def draw_rect(num):
    for i in range(1, num + 1):

        turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        turtle.left(5)
        turtle.pensize(1)
        turtle.fd(100)
        turtle.left(90)
        turtle.fd(50)
        turtle.left(90)
        turtle.fd(100)
        turtle.left(90)
        turtle.fd(50)
        

turtle.ht()
draw_rect(100)

turtle.done()
