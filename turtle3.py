import turtle as t
# t.bgcolor("white")
t.setup(800, 600)
t.pencolor("white")
t.fillcolor("red")
# 第一个心
t.begin_fill()
t.speed(5)
t.ht() #隐藏画笔
t.fd(-100)
t.left(135) # 旋转135
t.fd(100)  # 向前画100
t.right(180)# 旋转180
t.circle(50, -180) # 画半径为50，弧度为180 正数为顺着当前方向，负数为逆方向

t.left(90)
t.circle(50, -180)
t.right(180)
t.fd(100)
        
t.end_fill()

# 第二个心
t.begin_fill()
t.left(135)
t.fd(180)
t.left(135) # 旋转135
t.fd(100)  # 向前画100
t.right(180)# 旋转180
t.circle(50, -180) # 画半径为50，弧度为180 正数为顺着当前方向，负数为逆方向

t.left(90)
t.circle(50, -180)
t.right(180)
t.fd(100)
t.end_fill()

# 一箭穿心
t.pensize(3)

t.right(45)
t.fd(350)
t.up()
t.right(90)
t.fd(30)
t.right(80)
t.down()
t.pencolor("pink")
t.fd(500)
t.st()
t.done()








# "垃圾代码......"
