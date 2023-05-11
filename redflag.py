# 1. 画一个长方形，填充红色，
# 2. 画一个大的五角星
# 3. 画4个小的五角星
import turtle as t 
# 长方形旗面
t.speed(10)
t.setup(800, 700, 0,0)
'''
t.fillcolor("red")
t.begin_fill()
t.up()
t.goto(-300, -200)

t.down()
t.fd(600)
t.left(90)
t.fd(400)
t.left(90)
t.fd(600)
t.left(90)
t.fd(400)
t.ht()
t.end_fill()
'''
def draw_rectangle(x, y, width, height):
    """绘制矩形"""
    t.up()
    t.goto(x, y)
    t.pencolor('white')
    t.fillcolor('red')
    t.begin_fill()
    for i in range(2):
        t.down()
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()
draw_rectangle(-400, -200, 800,600)
# 第一个大五角星
t.fillcolor('yellow')
t.begin_fill()
t.up()
t.goto(-350, 230)
# t.left(90)
t.down()
for i in range(5):
    t.pencolor("yellow")
    t.fd(100)
    t.right(180-180/5)

t.end_fill()

#右一星
t.up()
t.fillcolor("yellow")
t.begin_fill()
t.goto(-200, 280)
t.down()
for i in range(5):
    t.pencolor("yellow")
    t.fd(50)
    t.left(180-180/5)

t.end_fill()
# 右二星
t.up()
t.fillcolor("yellow")
t.begin_fill()
t.goto(-160,230)
t.down()
for i in range(5):
    t.pencolor("yellow")
    t.fd(50)
    t.left(180-180/5)

t.end_fill()


#右三星
t.up()
t.fillcolor()
t.begin_fill()
t.goto(-160, 180)
t.down()
for i in range(5):
    t.pencolor("yellow")
    t.fd(50)
    t.left(180-180/5)
t.end_fill()


# 右四星
t.up()
t.fillcolor('yellow')
t.begin_fill()
t.goto(-200, 130)
t.down()
for i in range(5):
    t.pencolor("yellow")
    t.fd(50)
    t.left(180-180/5)



t.ht()
t.end_fill()
t.done()

