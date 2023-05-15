# 画一个不断旋转并变大的长方形
import turtle, random


a= 90
def draw_rect(x, y, width, height):
    global a 
    turtle.up()
    turtle.goto(x, y)
    for i in range(100):

        #turtle.up()
        #turtle.goto(x, y)
        turtle.down()

        turtle.fd(width)
        width += 4
        turtle.left(a)
        turtle.fd(height)
        height += 2
        turtle.left(a)
draw_rect(0, 0, 6, 4)
turtle.done()





