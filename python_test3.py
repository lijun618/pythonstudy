# turtle_draw
# turtle介绍https://blog.csdn.net/Silvester123/article/details/82944769
# turtle坐标资料https://blog.csdn.net/weixin_39526564/article/details/109916044



import turtle
import random

turtle.setup(600,600,80,80)#setup(width,height,startx,starty)画布窗体的大小，位置坐标

turtle.colormode(255) #画笔的颜色
# turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
# turtle.circle(50) #circle() 画一个半径50的圆
# radius = 50
turtle.speed(20)
def circle(radius):
    # global radius
    if radius >400:
        return
    # radius += 1
    turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))    
    # turtle.fd(20)  #fd\forward 向前（即向右方向）移动20
    turtle.circle(radius)
    turtle.right(5) # 顺时针旋转5度
    circle(radius + 2 )


circle(50)
turtle.done() # 停笔
# 未完 待续......
